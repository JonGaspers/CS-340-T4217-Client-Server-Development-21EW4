from pymongo import MongoClient
from bson.objectid import ObjectId

class AnimalShelter(object):
    """CRUD Operations for Animal Collection in MongoDB"""
    
    def __init__(self, username, password):
        #init MongoClient to access mongodb's and collections
        self.client = MongoClient('mongodb://%s:%s@localhost:43031/test?authSource=AAC' % ('aacuser', 'Password'))
        self.database = self.client['AAC']

#finish this to implement C in CRUD
    def create(self, data):
        if data is not None:
            create = self.database.animals.insert(data)
            if create != 0:
                return True
            else:
                return False
        else:
            raise Exception("Nothing to save, because data parameter was empty.")

#Method to implement R in CRUD
    def read(self, data=None):
        if data is not None: #If data provided then search and return that
            data = self.database.animals.find(data, {"_id":False})
        else: #if data not provided then all rows will be returned
            data = self.database.animals.find({}, {"_id":False})
        return data
    
#Method to implement U in CRUD    
    def update(self, OldData=None, UpdateData=None, many=False):
        if many is False:
                if OldData is not None:
                    if UpdateData is not None:
                        data = self.database.animals.update_one(OldData, UpdateData)
                    else:
                        raise Exception("Nothing to update, UpdateData parameter was empty.")
                else:
                    raise Exception("Nothing to update, OldData parameter was empty.")
                return data
        else:
            if OldData is not None:
                if UpdateData is not None:
                    data = self.database.animals.update_many(OldData, UpdateData)
                else:
                    raise Exception("Nothing to update, UpdateData parameter was empty.")
            else:
                raise Exception("Nothing to update, OldData parameter was empty.")
            return data
        
#Method to implement D in CRUD
    def delete(self, data, many=False):
        if many is False:
            if data is not None:
                data = self.database.animals.delete_one(data)
            else:
                raise Exception("Nothing to delete, because data parameter was empty.")
            return data
        else:
            if data is not None:
                data = self.database.animals.delete_many(data)
            else:
                raise Exception("Nothing to delete, because data parameter was empty.")
            return data