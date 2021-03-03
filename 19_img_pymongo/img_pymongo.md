# img_pymongo
###### tags: `AIOT`
[TOC]
## 知識點
- 將圖像上傳到 MongoDB 資料庫
- 從 MongoDB 資料庫下載圖像
## 筆記
## 實作
### mongoDB準備
- 先把mongodb的docker server跑起來
    - `docker run -d --name mongo1 -p 8080:27017 mongo`
- 拿到一個mongo shell來確認資料的改變
    - `docker exec -it mongo1 mongo`
### 把圖片存入mongodb
- [upload_image](https://github.com/chihpy/AIOT/blob/main/D27_img_pymongo/upload_image.py)
- 使用mongo shell察看結果
### 從mongodb下載圖像
- [load_image](https://github.com/chihpy/AIOT/blob/main/D27_img_pymongo/load_image.py)
## reference
## extension