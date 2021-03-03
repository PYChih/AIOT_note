from pymongo import MongoClient  
import requests
import base64
"""
run mongo docker first

"""

# setting mongoDB
client = MongoClient(host = '127.0.0.1', port = 8080)
db = client['yolo_pred_db'] # database: yolo_pred_db
coll = db['test_collection'] # collection
url = 'http://192.168.0.103:8080'
target_file = "imageList.txt"
# get prediction
r = requests.get(url)
if r.status_code == requests.codes.ok:
    print(r.text)
yolo_result = r.text

# get image and save
index_url = url + '/index'
r = requests.get(index_url)
if r.status_code == requests.codes.ok:
    print('ok')
res = r.text
head = res.find('<img src=')
tail = head + res[head:].find('>')
img_url = url + res[head:tail].split('\"')[1]
print(img_url)
img_name = 'prediction.jpg'
html = requests.get(img_url)
with open(img_name, 'wb') as f:
    f.write(html.content)

# save image to mongodb
with open(img_name, "rb") as f:
    bin_pic = base64.b64encode(f.read()).decode('utf-8')
    mydata = {'yolo_result': yolo_result, 'image_data': bin_pic}
    result = coll.insert_one(mydata) # add mydata to coll
    print(result.inserted_id) # print id
    
with open(target_file, "a+") as f:
    content = "{}:{}\n".format(img_name, result.inserted_id)
    f.write(content) # write the new line