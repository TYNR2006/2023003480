# Stage 1

## Notification APIs

### Create Notification

POST /notifications

Request

```json
{
  "studentId": 1042,
  "type": "Placement",
  "message": "Google Hiring Drive"
}
```

Response

```json
{
  "notificationId": "uuid"
}
```

### Get Notifications

GET /notifications?page=1&limit=20

Response

```json
{
  "notifications": []
}
```

### Mark Notification As Read

PATCH /notifications/{id}/read

### Delete Notification

DELETE /notifications/{id}

## Real-Time Notifications

I would use WebSockets to provide real-time notifications. Once a user logs in, a persistent WebSocket connection will be established between the client and server. Whenever a new notification is created, the server immediately pushes the notification to the connected user without requiring repeated polling.

Benefits:

* Real-time updates
* Reduced network traffic
* Better user experience
* Lower server load compared to polling

---

# Stage 2

## Database Selection

I would choose PostgreSQL.

Reasons:

* ACID compliance
* Strong consistency
* Efficient indexing
* Reliable transactions
* Suitable for large-scale notification systems

### Schema

```sql
CREATE TABLE notifications (
    id UUID PRIMARY KEY,
    student_id BIGINT NOT NULL,
    notification_type VARCHAR(50) NOT NULL,
    message TEXT NOT NULL,
    is_read BOOLEAN DEFAULT FALSE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

### Index

```sql
CREATE INDEX idx_student_notifications
ON notifications(student_id, is_read, created_at DESC);
```

---

# Stage 3

The query becomes slow because the notifications table contains millions of records. Without proper indexing, the database performs a large scan before finding the matching unread notifications.

Current Query:

```sql
SELECT *
FROM notifications
WHERE studentId = 1042
AND isRead = false
ORDER BY createdAt DESC;
```

Optimized Index:

```sql
CREATE INDEX idx_student_read_created
ON notifications(student_id, is_read, created_at DESC);
```

This allows PostgreSQL to directly locate unread notifications for a student and return them in sorted order.

### Event Notifications Query

```sql
SELECT *
FROM notifications
WHERE notification_type = 'Event'
AND created_at > NOW() - INTERVAL '7 days';
```

Index:

```sql
CREATE INDEX idx_event_notifications
ON notifications(notification_type, created_at DESC);
```

---

# Stage 4

To reduce database load, I would introduce Redis caching.

Architecture:

Client
→ Redis
→ PostgreSQL

Workflow:

1. Check Redis for notifications.
2. If available, return cached data.
3. If not available, fetch from PostgreSQL.
4. Store the result in Redis.

Additional Improvements:

* Cursor based pagination
* Notification batching
* Cache invalidation after updates

Benefits:

* Faster response times
* Reduced database load
* Better scalability

---

# Stage 5

The proposed implementation is not reliable because email delivery failures can result in partial notification delivery.

I would redesign the system using a message queue.

Components:

* Notification Service
* RabbitMQ
* Email Worker
* Push Notification Worker

Workflow:

Notification API
↓
Save Notification In Database
↓
Publish Event To RabbitMQ
↓
Email Worker
↓
Push Notification Worker

Benefits:

* Retry support
* Fault tolerance
* Horizontal scalability
* Non-blocking operations

Revised Pseudocode:

```python
def notify_all(student_ids, message):
    notification_id = save_notification(message)

    publish_event({
        "notification_id": notification_id,
        "student_ids": student_ids
    })

    return True
```

Workers consume events independently and retry failed operations.

---

# Stage 6

## Priority Inbox

Priority Weights:

Placement = 3

Result = 2

Event = 1

Priority Score:

```python
score = (weight * 100000) + recency_score
```

To efficiently maintain the top notifications, I would use a Heap (Priority Queue).

Complexity:

```text
O(n log k)
```

where:

```text
k = 10
```

This approach efficiently returns the highest-priority unread notifications even when new notifications continue arriving.
