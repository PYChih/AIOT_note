import base64
from pymongo import MongoClient  

img_name = 'dog.jpg'
target_file = "imageList.txt"

# connect to local MongoDB
client = MongoClient(host = '127.0.0.1', port = 8080)
db = client['test_db']
coll = db['test_img']
    
with open(img_name, "rb") as f:
    strpic = base64.b64encode(f.read()).decode('utf-8')
    mydata = {'jpg_base64': strpic}
    result = coll.insert_one(mydata) # add mydata to coll
    print(result.inserted_id) # print id
    
with open(target_file, "a+") as f:
    content = "{}:{}\n".format(img_name, result.inserted_id)
    f.write(content) # write the new line
