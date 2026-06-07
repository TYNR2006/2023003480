import requests

url = "http://4.224.186.213/evaluation-service/auth"

payload = {
    "email": "yoganandha.reddy@gmail.com",
    "name": "yoganandha reddy thappeta",
    "rollNo": "2023003480",
    "accessCode": "wgKtgZ",
    "clientID": "e17daada-def5-4c1a-8ea1-fe46954696ec",
    "clientSecret": "NVCyfxsmxCCvnYTc"
}

response = requests.post(url, json=payload)
data = response.json()
# print(response.text)
print(data["access_token"])