import requests
from time import sleep

'''
Initiale testing of accessing the API
'''


#website im accessing
website_name = "http://localhost:3000"


# -- get function testing
# payload = {'my_value': 'some_name'}
# r = requests.get(website_name + "/items", params=payload)
# print(r.text)

#--Manual testing of the api
temp_order = {"action": "get", "id": 3 , "name": "suzy"}
temp2 = {"action": "delete_all", "id": 4 , "name": "johny"}
temp3 = {"action": "post", "id": 123 , "name": "herold"}
# r = requests.get(website_name + "/items", params=temp_order)
r = requests.post(website_name + "/items", json=temp3)
print(r.text)

r = requests.post(website_name + "/items", json=temp3)
print(r.text)


