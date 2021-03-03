# Flask-PyMongo
###### tags: `AIOT`
[TOC]
## 知識點
- API、RESTful概念
- GET、POST、PUT、DELETE
- 實作API操作MongoDB
## 筆記
- 套件:
    - `flask`: pip install flask
    - `Flask-PyMongo`: pip install Flask-PyMongo
    - `bson`: pip install bson
- API (Application Programming Interface):
    - 軟體間的溝通橋梁、規定
    - 前後端串接指的就是API串接，前後端討論好規格後依照該規格實作
- RESTful (Representational State Transfer)
    - 一種軟體架構風格，透過這種規範、約束，讓不同軟體、程式更方便溝通
    - 符合RESET風格的WebAPI，稱為RESTfulAPI
    - RESTful API
        - 對發送請求的方法有規範
        - 對請求的URI有規範
    - 若API符合這種規範就稱為RESTful API
    - RESTful URI的命名習慣
        - 使用/符號表試資源間的層次
        - 不要在結尾使用/
        - 使用-連字符號提高可讀性，不要使用_底線
        - 全部用小寫字母
        - 不要在URI中包含CRUD函數名稱
    - 正例:
        - `example.com/member-management/members`
        - `example.com/member-management/members/{id}`
    - 反例:
        - `example.com/member-management/delete_membber?id=3`
## 實作: 使用Flask操作MongoDB
### 取得
### 新增
### 刪除
### 修改
## reference
- [RESTful API Tutorial](https://www.restapitutorial.com/index.html)
- [Flask-PyMongo](https://flask-pymongo.readthedocs.io/en/latest/)
## extension