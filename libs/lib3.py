import requests

response = requests.get("https://i.stack.imgur.com/WyyDdl.png")

# with open("pyth.png", "wb") as fil:
#     fil.write(response.content)

print(response.ok)

# httpbin.org