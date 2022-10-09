import requests

BASE = "http://127.0.0.1:5000/" 
response = requests.put(BASE + "advertising/1", {"customer_id":12, "opt_in":True, "inactivity_timer":1})
print(response.json())
response = requests.put(BASE + "advertising/1", {"customer_id":14, "opt_in":True, "inactivity_timer":1})
print(response.json())
response = requests.put(BASE + "advertising/1", {"customer_id":12, "opt_in":False, "inactivity_timer":1})
print(response.json())
response = requests.put(BASE + "advertising/1", {"customer_id":14, "opt_in":False, "inactivity_timer":4})
print(response.json())
# input()
# response = requests.get(BASE + "advertising/1")
# print(response.json())
