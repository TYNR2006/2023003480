from flask import Flask, jsonify

from api_client import get_depots, get_vehicles
from scheduler import maximize_impact

app = Flask(__name__)

TOKEN = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJNYXBDbGFpbXMiOnsiYXVkIjoiaHR0cDovLzIwLjI0NC41Ni4xNDQvZXZhbHVhdGlvbi1zZXJ2aWNlIiwiZW1haWwiOiJ5b2dhbmFuZGhhLnJlZGR5QGdtYWlsLmNvbSIsImV4cCI6MTc4MDgxMzQ2OCwiaWF0IjoxNzgwODEyNTY4LCJpc3MiOiJBZmZvcmQgTWVkaWNhbCBUZWNobm9sb2dpZXMgUHJpdmF0ZSBMaW1pdGVkIiwianRpIjoiMzcxZDFiZWItOTllYi00NTExLTlkNzAtZjA2YTM5Yjk3MDM0IiwibG9jYWxlIjoiZW4tSU4iLCJuYW1lIjoieW9nYW5hbmRoYSByZWRkeSB0aGFwcGV0YSIsInN1YiI6ImUxN2RhYWRhLWRlZjUtNGMxYS04ZWExLWZlNDY5NTQ2OTZlYyJ9LCJlbWFpbCI6InlvZ2FuYW5kaGEucmVkZHlAZ21haWwuY29tIiwibmFtZSI6InlvZ2FuYW5kaGEgcmVkZHkgdGhhcHBldGEiLCJyb2xsTm8iOiIyMDIzMDAzNDgwIiwiYWNjZXNzQ29kZSI6IndnS3RnWiIsImNsaWVudElEIjoiZTE3ZGFhZGEtZGVmNS00YzFhLThlYTEtZmU0Njk1NDY5NmVjIiwiY2xpZW50U2VjcmV0IjoiTlZDeWZ4c214Q0N2bllUYyJ9.-q7h7aFZkygcTr3yy8Ejrobdlydrq2HMsfpbw-TiK5g"

@app.route("/schedule", methods=["GET"])
def schedule():

    depot_response = get_depots(TOKEN)
    print(depot_response)

    depots = depot_response["depots"]
    vehicles = get_vehicles(TOKEN)["vehicles"]

    result = []

    for depot in depots:
        data = maximize_impact(
            vehicles,
            depot["MechanicHours"]
        )

        result.append({
            "DepotID": depot["ID"],
            "MechanicHours": depot["MechanicHours"],
            "SelectedTasks": data["SelectedTasks"],
            "TotalImpact": data["TotalImpact"],
            "TotalDuration": data["TotalDuration"]
        })

    return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True)