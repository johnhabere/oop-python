import requests

# response = requests.get("https://httpbin.org/basic-auth/joe/testing", auth=("joe", "testing4"))

response = requests.get("https://httpbin.org/delay/3", timeout=2)

print(response)