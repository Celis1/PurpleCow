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
    #TODO - create and render the template for the webapp
    # return render_template('index.html')
    return "<p>Hello, World!</p>"



#this is the items page that we will be editing through the api
#TODO - add Variable Rules (only want the correct type of data coming in)
@app.route("/items",  methods=['GET','POST'])
def my_items():
    '''
    This is the items page that we will be editing through the api. This is an endpoint that 
    communicates with my items_api class.
    
    '''

    r = request
    #calling all the functions in another class
    return items_func.incoming_req(r)




if __name__ == "__main__":
    #setting the host to local setting the port to 3000 and disabling debug mode
    #TODO - disable debug mode
    app.run(host="localhost", port=3000, debug=True)