from datetime import datetime
import requests
import os

APP_ID = os.getenv("APP_ID")
API_KEY = os.getenv("API_KEY")
SHEET_ENDPOINT = os.getenv("SHEET_ENDPOINT")
USERNAME = os.getenv("USERNAME")
PASSWORD = os.getenv("PASSWORD")
NUT_ENDPOINT = os.getenv("NUT_ENDPOINT")
TOKEN = os.getenv("TOKEN")

today = datetime.now().strftime("%Y:%m:%d")

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}

end_point = NUT_ENDPOINT
params = {
    "query": input("What did you do today? ")
}
response = requests.post(url=end_point, json=params, headers=headers)
response.raise_for_status()
data = response.json()
#print(data)

exercise = data["exercises"][0]["name"].title()
duration_minute = data["exercises"][0]["duration_min"]
calories = data["exercises"][0]["nf_calories"]

work_params = {
    "workout": {
        "date": today,
        "time": datetime.now().strftime("%H:%M:%S"),
        "exercise": exercise,
        "duration": duration_minute,
        "calories": calories,
    }
}

bearer_headers = {
    "Authorization": f"Bearer {TOKEN}"
}

sheety_response = requests.post(url=SHEET_ENDPOINT, json=work_params, headers=bearer_headers)

sheety_response.raise_for_status()
print(sheety_response.text)
print("Data added to Sheety successfully!")







