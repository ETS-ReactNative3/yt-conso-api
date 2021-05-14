import json

with open('bot.json') as jfile:
    file = json.load(jfile)["0"]
for x in file:
    print(x)
print("--"*10)