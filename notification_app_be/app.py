from flask import Flask, request, jsonify
import uuid

app = Flask(__name__)

notifications = []


@app.route("/notifications", methods=["POST"])
def create_notification():
    data = request.json

    notification = {
        "id": str(uuid.uuid4()),
        "studentId": data["studentId"],
        "type": data["type"],
        "message": data["message"],
        "isRead": False
    }

    notifications.append(notification)

    return jsonify(notification), 201


@app.route("/notifications", methods=["GET"])
def get_notifications():
    return jsonify(notifications)


@app.route("/notifications/<notification_id>/read", methods=["PATCH"])
def mark_read(notification_id):
    for notification in notifications:
        if notification["id"] == notification_id:
            notification["isRead"] = True
            return jsonify(notification)

    return jsonify({"message": "Not Found"}), 404


@app.route("/notifications/<notification_id>", methods=["DELETE"])
def delete_notification(notification_id):
    global notifications

    notifications = [
        n for n in notifications
        if n["id"] != notification_id
    ]

    return jsonify({"message": "Deleted"})


if __name__ == "__main__":
    app.run(debug=True)