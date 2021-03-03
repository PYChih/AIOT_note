import base64
from PIL import Image
from io import BytesIO
from pymongo import MongoClient  
import matplotlib.pyplot as plt


client = MongoClient(host = '127.0.0.1', port = 8080)
db = client['test_db']
coll = db['test_img']

img_name = 'dog.jpg'
_id = []
# find required id
with open("imageList.txt", "r") as f:
    lines = f.readlines()
    for i in range(len(lines)):
        if img_name in lines[i]:
            print(lines[i])
            print(lines[i].strip("\n").split(":")[1])
            _id.append(lines[i].strip("\n").split(":")[1])

# given id find image
img_base64 = []
for i in coll.find():
    if str(i['_id']) == _id[0]:
        img_base64.append(i['jpg_base64'])
        im = Image.open(BytesIO(base64.b64decode(img_base64[0])))
        im.save("load_img.jpg", "JPEG")
    else:
        print("img no find")