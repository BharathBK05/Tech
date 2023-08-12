from pymongo import MongoClient
import gridfs

def mongo_con():
    try:
        conn = MongoClient("mongodb://localhost:27017/")
        print("Connected")
        return conn.grid_file
    except:
        print("Exception")

#DB upload
db = mongo_con()
name = 'image.jpg'
file = open(name,'rb')
data = file.read()
fs = gridfs.GridFS(db)
fs.put(data, filename = name)
print("Upload completed")

#DB download
data = db.fs.files.find_one({'filename' : name})
id = data['_id']
outputdata = fs.get(id).read()
loc = 'download/' + name
output = open(loc,'wb')
output.write(outputdata)
print("Download completed")

