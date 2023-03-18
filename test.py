import requests

BASE = "http://127.0.0.1:5000/"

response = requests.post(BASE + "video/1", {"likes": 10, "views": 20, "name": "my-video"})
response = requests.get(BASE + "video/1")
print(response.json())