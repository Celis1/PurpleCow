
from flask import request



class items_api:
    """
    This class is for interacting with flasks requests and modifying the data in temp storage
    """

    def __init__(self, request):
        self.method = request #.method testing rn
        self.df = {'id': 'name'}
        


    def get_data(self,id = None, name = None):
        if not name or not id:
            #they passed bad data
            return []

        if id in self.database_list:
            #if the 
            return self.df[id]

        elif name in self.database_list:
            #serach through the values
            return 'name'
      

    def post_data(self):
        return 'post_data'

    def delete_data(self):
        #delete a particular item 
        return 'delete'

    def DELETE_ALL(self):
        #delete all items
        return 'delete_all'



if __name__ == '__main__':
    # print(items_api.__list__())
    # print(items_api.search_data(id = '123', name = 'test')) 
    u = items_api('get')
    print()

    u.database_list = ['new', 'list']
    print(u.database_list)

    print('-----------')

    # u.search_data(id = '123')

    print(u.__getitem__([0]))
