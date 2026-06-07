import requests

url = "http://4.224.186.213/evaluation-service/register"

payload = {
    "email": "yoganandha.reddy@gmail.com",
    "name": "Yoganandha Reddy Thappeta",
    "mobileNo": "8106655065",
    "githubUsername": "TYNR2006",
    "rollNo": "2023003480",
    "accessCode": "wgKtgZ"
}

response = requests.post(url, json=payload)

print(response.text)