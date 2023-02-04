import requests

response = requests.get("https://ucu.ac.ug")

#print(response)
#print(dir(response))
#print(help(response))

print(response.text)