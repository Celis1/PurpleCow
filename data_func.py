
from flask import request
from flask import Flask , render_template, jsonify



class items_api:
    """
    This class is for interacting with flasks requests and modifying the data in temp storage
    """

    def __init__(self):
        

        self.db = [ {'id': 1,'name': 'joe'},
                    {'id': 2,'name': 'anny'},
                    {'id': 3,'name': 'suzy'},
                    {'id': 10,'name': 'joe'} ]
        


    def get_data(self,id = None, name = None):
        ''' 
        Function for retrieving data from the database depending if an id or a name was search or both
        '''
        print(id)
        print(name)
        temp_data = []

        #they passed bad data
        if not name and not id:
            return []

        #looping through the list
        for i in range(len(self.db)):

            #if i have their id 
            if id == self.db[i]['id']:
                temp_data.append(self.db[i])

            #if i have their name
            elif name == self.db[i]['name']:
                #serach through the values
                temp_data.append(self.db[i])
        
        #checking if we found specific value
        if id and name:
            if {'id': id, 'name': name} in temp_data:
                print('found search')
                temp_data = [{'id': id, 'name': name}]

        return temp_data

    def post_data(self,id = None, name = None):
        '''
        Function for adding items to the storage
        '''
        #adding to the db
        if not name or not id:
            return 0

        #should include type checking
        self.db.append({'id': id, 'name': name})
        
        return 1 #bool value to know it was successful

    def delete_data(self,id = None, name = None):
        '''
        Function for deleting items from the storage
        '''
        for i in range(len(self.db)):
            if self.db[i] == {'id': id, 'name': name}:
                self.db.pop(i)
                return 1
        
        return 0 #this means nothing was deleted

    def DELETE_ALL(self):
        '''
        This function will delete all entries in the storage
        '''
        #delete all items   
        self.db = []
        return 1

    def incoming_req(self, request):
        '''
        Method for handling the incoming requests and accessing the storad data depending 
        on the values passed through the request.
        '''
        #this is the request that is coming in
        if request.method == "GET":

            action = request.args.get('action') #this is how i will be recieving the data
            id = request.args.get('id')
            name = request.args.get('name')

            if not action or action == 'get':
                try:
                    id = int(id)
                except:
                    id = None
                    print('id could not be converted to int')

                data = self.get_data(id,name)
                return jsonify(data)
            return []

        if request.method == "POST":
            return []




if __name__ == '__main__':
    # print(items_api.__list__())
    # print(items_api.search_data(id = '123', name = 'test')) 
    u = items_api()
    print(u.db)

    print()
    
    temp = u.get_data( name = 'suzy')
    print(temp)


    temp = u.post_data(id = 87, name = 'jacob')
    print(temp)
    print(u.db)


    temp = u.delete_data(id=3, name = 'suzy')
    print(temp)
    print(u.db)

    temp = u.delete_data(id = 2, name = 'anny')
    print(temp)
    print(u.db)

    temp = u.DELETE_ALL()
    print(temp)
    print(u.db)

