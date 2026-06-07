# Vehicle Maintenance Scheduler

## Overview

This project solves the Vehicle Maintenance Scheduling problem by selecting the optimal set of maintenance tasks that maximizes operational impact while staying within the available mechanic hours for each depot.

## Approach

The problem is modeled as a 0/1 Knapsack Problem.

* Duration → Weight
* Impact → Value
* Mechanic Hours → Capacity

Dynamic Programming is used to determine the optimal set of tasks.

## Project Structure

```text
logging_middleware/
vehicle_maintenance_scheduler/
notification_app_be/
auth.py
register.py
README.md
```

## Requirements

* Python 3.x
* Flask
* Requests

## Installation

```bash
pip install flask requests
```

## Running

```bash
python app.py
```

## API

### GET /schedule

Returns the optimized maintenance schedule for all depots.

## Complexity

Time Complexity:

```text
O(N × Capacity)
```

Space Complexity:

```text
O(N × Capacity)
```

## Technologies Used

* Python
* Flask
* REST APIs
* Dynamic Programming
* PostgreSQL Design Concepts
* Redis Design Concepts
* RabbitMQ Design Concepts
