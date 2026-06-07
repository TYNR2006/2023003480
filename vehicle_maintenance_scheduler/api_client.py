import requests
BASE_URL = "http://4.224.186.213/evaluation-service"
def get_depots(token):
    headers = {
        "Authorization": f"Bearer {token}"
    }

    response = requests.get(
        f"{BASE_URL}/depots",
        headers=headers
    )

    return response.json()


def get_vehicles(token):
    headers = {
        "Authorization": f"Bearer {token}"
    }

    response = requests.get(
        f"{BASE_URL}/vehicles",
        headers=headers
    )

    return response.json()