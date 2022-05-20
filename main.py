from flask import Flask , render_template, request, jsonify
from flask_restful import Api #probably going to end up using flask_restful api class for this
import json

app = Flask(__name__)

#This is the main page
@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"



#this is the items page that we will be editing through the api
#TODO - add Variable Rules (only want the correct type of data coming in)
@app.route("/items",  methods=['GET','POST'])
def my_items():
    '''
    This is the items page that we will be editing through the api. 

    TODO - define the scope of the items and their interactions as an api. current prompt scope:
            The API includes endpoints on the `/items` resource that allow a client to retrieve the
            current items, set the list of items, and delete all of the items
    TODO - create post request to add items to the list.
    TODO - use json as the data that its recieving/sending.
    
    '''
    if request.method == "GET":
        #placeholder for more meaningful data
        return jsonify({'id': '111111',
                       'name': 'get_name'})

        #placeholder for more meaningful data
    if request.method == "POST":
       return jsonify({'id': '222222',
                       'name': 'post_name'}) 





if __name__ == "__main__":
    #setting the host to local setting the port to 3000 and disabling debug mode
    #TODO - disable debug mode
    app.run(host="localhost", port=3000, debug=True)