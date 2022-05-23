import requests
from time import sleep

'''
Initiale testing of accessing the API
'''


#website im accessing
website_name = "http://localhost:3000"

#retrieving the entire database
r = requests.get(website_name + "/all_items")
print(r.text)
sleep(2)

# -- get function testing
payload = {"action": "get", "id": 3 , "name": "suzy"}
r = requests.get(website_name + "/items", params=payload)
print(r.text)
sleep(2)

#--Manual testing of the api

# adding herold to the database
temp1 = {"action": "post", "id": 123 , "name": "herold"}
r = requests.post(website_name + "/items", json=temp1)
print(r.text)
sleep(2)

#adding jacob to the database
temp2 = {"action": "post", "id": 321 , "name": "jacob"}
r = requests.post(website_name + "/items", json=temp2)
print(r.text)
sleep(2)

#deletin joe from the database
temp3 = {"action": "delete", "id": 1 , "name": "joe"}
r = requests.post(website_name + "/items", json=temp3)
print(r.text)
sleep(2)

#requesting the entire database
r = requests.get(website_name + "/all_items")
print(r.text)
sleep(2)


#deleting the entire database
temp4 = {"action": "delete_all", "id": 4 , "name": "johny"}
r = requests.post(website_name + "/items", json=temp4)
print(r.text)
sleep(2)

#requesting the entire database
r = requests.get(website_name + "/all_items")
print(r.text)