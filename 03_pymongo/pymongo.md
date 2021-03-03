# pymongo
###### tags: `AIOT`
[TOC]
## 知識點
- python操作mongodb
    - 增、刪、改、查
    - 排序、限制資料筆數
## 筆記
- 在python中操作mongodb
    - `pip install pymongo`
## 實作
- 先把mogodb的docker server跑起來
    - `docker run -d --name mongo1 -p 8080:27017 mongo`
- 拿到一個mongo shell來確認資料的改變
    - `docker exec -it mongo1 mongo`
- [x] 基本操作
    - 建立database、collection
    - 新增資料
    - 新增多筆
    - 刪除資料
    - 刪除多筆
    - 修改資料
    - 修改多筆
    - 查詢資料
    - 查詢所有資料
- [x] 排序資料
- [x] 限制資料筆數
## reference
- [python mongoDB](https://www.w3schools.com/python/python_mongodb_getstarted.asp) w3school
- [python mongoDB](https://www.runoob.com/python3/python-mongodb.html) 菜鳥教程
## extension
