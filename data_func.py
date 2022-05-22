
from flask import request
from flask import Flask , render_template, jsonify



class items_api:
    """
    This class is for interacting with flasks requests and modifying the data in temp storage
    """

    def __init__(self):
        

        self.db = [ {'id': 1,'name': 'joe'},
                    {'id': 2,'name': 'anny'},
                    {'id': 3,'name': 'suzy'}]
        


    def get_data(self,id = None, name = None):
        print('--searching for data --')
        temp_data = []

        #they passed bad data
        if not name and not id:
            return []

        #looping through the list
        for i in range(len(self.db)):

            #if i have their id 
            if id == self.db[i]['id']:
                #if the 
                temp_data.append(self.db[i])

            if name == self.db[i]['name']:
                #serach through the values
                temp_data.append(self.db[i])

      
        return temp_data

    def post_data(self,id = None, name = None):
        #adding to the db
        if not name and not id:
            return 0

        #should include type checking
        self.db.append({'id': id, 'name': name})
        
        return 1 #bool value to know it was successful

    def delete_data(self,id = None, name = None):
        for i in range(len(self.db)):
            if self.db[i] == {'id': id, 'name': name}:
                self.db.pop(i)
                return 1
        
        return 0 #this means nothing was deleted

    def DELETE_ALL(self):
        #delete all items   
        self.db = []
        return 1

    def incoming_req(self, request):
        #this is the request that is coming in
        # print(request.method)
        if request.method == "GET":
            #-- only use this to look for data 

            #placeholder for more meaningful data
            # print(request.data , '--inc value')


            #--- I NEED TO SEARCH DEPENDING ON THE VALUE PASSED IN 
            data = request.args.get('my_value') #this is how i will be recieving the data
            # print(data)


            if isinstance(data, int):
                print('data was a string')
                #ill prob conver to a list and return the data

            elif isinstance(data, list):
                print('data was a list')
                # we want to keep this to enable multiple searches

            
            #now we will search the databse for the data
            self.get_data(data)



            return jsonify({'id': '111111',
                        'name': data})


        if request.method == "POST":
            pass




if __name__ == '__main__':
    # print(items_api.__list__())
    # print(items_api.search_data(id = '123', name = 'test')) 
    u = items_api()
    print(u.db)

    print()
    
    temp = u.get_data( name = 'suzy')
    print(temp)

    print()
    temp = u.post_data(id = 87, name = 'jacob')

    print(temp)
    print(u.db)


    # u.database_list = ['new', 'list']
    # print(u.database_list)

    # print('-----------')

    
