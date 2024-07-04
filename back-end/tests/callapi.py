import requests

# url = "https://ef00-2001-b400-e35f-fa42-6df2-b7a9-85a8-4112.ngrok-free.app"
url = "http://127.0.0.1:5555/CAS/api/v1/patients"

payload = {}
headers = {}

response = requests.request("GET", url, headers=headers, data=payload)

print(type(response), response)