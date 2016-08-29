from json import load
with open('config.json','r') as f:
    data=load(f)
print(data['username'])
