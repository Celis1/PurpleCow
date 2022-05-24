from flask import Flask , render_template, jsonify
from flask import request
from flask_restful import Api #probably going to end up using flask_restful api class for this
import json

from data_func import items_api #this is my own class for dealing with the data



app = Flask(__name__)

items_func = items_api()


#This is the main page
@app.route("/")
def hello_world():
    hello_world = '''<h1>Welcome to the dockerized web application</h1>
    <h3>This api service is for getting, posting, and deleting items in a list. </h3>
    <li>To view in browser navigate to the /all_items page to view the entire db in storage. </li>
    <li>You can also use get/post request to view, manipulate, or delete the data. </li>
    <li>both get and post methods have 3 params action, id, name. </li>
    <li>the param action are either get, post, delete, or delete_all. </li>
    <li>id is an integer and name is the casesensitive string. </li>
    
    <br>

    <form action="/all_items">
    <input type="submit" value="View database entries" />
    </form>'''
    return hello_world



#this is the items page that we will be editing through the api
@app.route("/items",  methods=['GET','POST'])
def my_items():
    '''
    This is the items page that we will be editing through the api. This is an endpoint that 
    communicates with my items_api class.
    '''
    
    r = request
    #calling all the functions in another class
    return items_func.incoming_req(r)

@app.route("/all_items",  methods=['GET'])
def all_items():
    '''
    View the entire db in storage
    '''
    return jsonify(items_func.db)


if __name__ == "__main__":
    #running the application
    app.run(debug=False)