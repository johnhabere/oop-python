import requests


# response = requests.get("https://httpbin.org/get?page=2&count=15")


# payload = {"page": 2, "count": 15}
# response = requests.get("https://httpbin.org/get",params=payload)

# print(response.url)

payload = {"username": "joe", "password": "testing"}
response = requests.post("https://httpbin.org/post",data=payload)

# print(response.json())

dct = response.json()

print(dct['form'])
