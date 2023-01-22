from pymongo import MongoClient
  
# creation of MongoClient
client=MongoClient()
  
# Connect with the portnumber and host
client = MongoClient("mongodb://localhost:27017/")
  
# Access database
mydatabase = client['bharath']
  
# Access collection of the database
mycollection=mydatabase['testing']

mycollection.insert_one({'name': 'Kumar'})

for i in mycollection.find():
    print(i)