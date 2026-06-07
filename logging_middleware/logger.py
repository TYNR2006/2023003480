import requests

TOKEN = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJNYXBDbGFpbXMiOnsiYXVkIjoiaHR0cDovLzIwLjI0NC41Ni4xNDQvZXZhbHVhdGlvbi1zZXJ2aWNlIiwiZW1haWwiOiJ5b2dhbmFuZGhhLnJlZGR5QGdtYWlsLmNvbSIsImV4cCI6MTc4MDgxMTQzOSwiaWF0IjoxNzgwODEwNTM5LCJpc3MiOiJBZmZvcmQgTWVkaWNhbCBUZWNobm9sb2dpZXMgUHJpdmF0ZSBMaW1pdGVkIiwianRpIjoiOTk3ZTUwMTctMDgzYi00YzE2LWJkYzgtYzcxYjM2ZThhNWZiIiwibG9jYWxlIjoiZW4tSU4iLCJuYW1lIjoieW9nYW5hbmRoYSByZWRkeSB0aGFwcGV0YSIsInN1YiI6ImUxN2RhYWRhLWRlZjUtNGMxYS04ZWExLWZlNDY5NTQ2OTZlYyJ9LCJlbWFpbCI6InlvZ2FuYW5kaGEucmVkZHlAZ21haWwuY29tIiwibmFtZSI6InlvZ2FuYW5kaGEgcmVkZHkgdGhhcHBldGEiLCJyb2xsTm8iOiIyMDIzMDAzNDgwIiwiYWNjZXNzQ29kZSI6IndnS3RnWiIsImNsaWVudElEIjoiZTE3ZGFhZGEtZGVmNS00YzFhLThlYTEtZmU0Njk1NDY5NmVjIiwiY2xpZW50U2VjcmV0IjoiTlZDeWZ4c214Q0N2bllUYyJ9.-XYqMFRVskr7-ZO2Rq_h8DF9ic3j54dG_PGzWC16Mu8 "

def log(stack, level, package, message):

    url = "http://4.224.186.213/evaluation-service/logs"

    headers = {
        "Authorization": f"Bearer {TOKEN}"
    }

    payload = {
        "stack": stack,
        "level": level,
        "package": package,
        "message": message
    }

    response = requests.post(
        url,
        json=payload,
        headers=headers
    )

    print(response.text)
    print(response.status_code)

log(
    "backend",
    "info",
    "service",
    "logging middleware test"
)