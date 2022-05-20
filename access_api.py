import requests
from time import sleep

'''
Initiale testing of accessing the API
'''


#website im accessing
website_name = "http://localhost:3000"


#get with payload params
payload = {'my_value': 'some_name'}
r = requests.get(website_name + "/items", params=payload)

print(r.text)

#get request 
r = requests.get(website_name + "/items") #wow

print(r.text)


#post request
r = requests.post(website_name + "/items" ,json={'my_value': 'post_name'})
print(r.text)


#post request with payload params
r = requests.post(website_name + "/items", json={"other_val": "test_name"})
print(r.text)
