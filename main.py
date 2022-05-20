from flask import Flask , render_template, jsonify
from flask import request
from flask_restful import Api #probably going to end up using flask_restful api class for this
import json

from data_func import items_api #this is my own class for dealing with the data

app = Flask(__name__)

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
    This is the items page that we will be editing through the api. 

    TODO - define the scope of the items and their interactions as an api. current prompt scope:
            The API includes endpoints on the `/items` resource that allow a client to retrieve the
            current items, set the list of items, and delete all of the items
    TODO - create post request to add items to the list.
    TODO - use json as the data that its recieving/sending.
    
    '''

    #TODO - this function will be an endpoint but all data functions and request function will be done through another class

    if request.method == "GET":
        #-- only use this to look for data 

        #placeholder for more meaningful data
        # print(request.data , '--inc value')

        data = request.args.get('my_value') #this is how i will be recieving the data
        print(data)



        return jsonify({'id': '111111',
                       'name': data})




        #placeholder for more meaningful data
    if request.method == "POST":
        #-- use this to modify delete
        
        print(request)

        
        data = request.get_json() #this is how i will be recieving the data
        print(data)

        other_data = request.get_json() #this is how i will be recieving the data
       
        print(other_data)


        return jsonify({'id': data,
                       'name': other_data}) 





if __name__ == "__main__":
    #setting the host to local setting the port to 3000 and disabling debug mode
    #TODO - disable debug mode
    app.run(host="localhost", port=3000, debug=True)