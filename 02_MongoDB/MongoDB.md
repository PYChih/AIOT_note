# MongoDB
###### tags: `AIOT`
[TOC]
## 知識點
- 理解NoSQL特性、與SQL差異
- 了解MongoDB及其特色
- 利用指令、圖形化介面Robo3T操作MongoDB

## 筆記
- 基本單元
    - document
        - mongoDB中的基本單元
        - 類似關聯式中的row
        - 就是一個由key-value組成的集合
            - 一個dictionary
    - collection
        - 由一群document組成
        - 類似關聯式中的table
        - 動態模式是指可以把各式各樣的文檔存在同一個集合，不一定要有固定的schema
    - database
        - 等同於關聯式中的database
        - 一個database可以有零或多個collection
        - 一個monboDB可以有多個database
        - admin；local；config被保留
## 實作
- 開啟MongoDB server
    - `sudo mongod --dbpath [path]`
### Mongo Shell操作:
- 連線db
    - `mongo`
        - 開啟shell
        - 同時連線DB(預設127.0.0.1:27017)
        - 預設是連到test
- 連線資料庫
    - `mongo -nodb`
        - 只開啟shell沒有連線到DB
    - `conn = new Mongo()`
    - `db = conn.getDB("[dbname]")`
- 切換資料庫
    - `use [dbname]`
        - 若dbname不存在會自動建立
- 新增文檔
    - `db.collname.insert({dict})`
    - `db.collname.insert([{dict}, {dict}])`
    - `db.collname.insertMany([{dict}, {dict}])`
- 刪除資料
    - `db.collname.remove({})`
    - `db.collname.remove({cond})`
        - 這個刪會刪多筆喔
- 修改資料
    - `db.collname.find()`
    - `db.collname.update({dict}, {dict})`
        - first dict: query cond
        - second dict: update data
- 查詢資料
    - `db.member.find()`
    - `db.member.find().pretty()`
- 其他實用的指令
    - `db`: 查看現在在哪個資料庫
    - `db.stats`: 目前資料庫的詳細資訊
    - `show dbs`: 查看有多少資料庫在這個server上
    - `show collections`: 查看這個資料庫有多少集合
    - `db.version`: 查看資料庫版本
### docker安裝mongodb
- `docker pull mongo`
- `docker run -d --name mongo1 -p [hostport]:[containerport] [imagename]`
- 使用mongo shell連線
    - `mongo [hostip]:[hostport]`
- 使用container本身的mongo shell
    - `docker exec -it [imagename] [command]`
- [ ] 使用docker安裝mongoDB加上驗證機制
    - `docker run -d --name [name] -p [hostport]:[containerport] -e MONGO_INITDB_ROOT_USERNAME=[admin] -e MONGO_INITDB_ROOT_PASSWORD=[password] mongo (紅字的地方請自行決定輸入)`
## reference
- [MongoDB](https://www.runoob.com/mongodb/mongodb-tutorial.html)菜鳥教程
## extension
