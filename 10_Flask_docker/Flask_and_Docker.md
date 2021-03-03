# Flask and Docker
###### tags: `AIOT`
[TOC]
## 知識點
- 了解Flask框架
- 了解Docker、Image、Container概念
- 從Docker Hub取得image
- 撰寫自己的Docker image
## 筆記
- 第一個flask專案
    ```
    # 引用需要的套件, 若有多個套件要引用，可使用逗號隔開
    from flask import Flask, request

    app = Flask(__name__)

    # 設定網址路由，及接受的 method(預設是 GET)
    @app.route('/', methods=['GET'])
    def index():
        return "Hello World"
    
    if __name__ == '__main__':
        app.run()
    ```
## 實作
- 用flask寫一個hello world
- 使用docker佈署Flask
## reference
- [Docker常用指令](https://www.docker.com/sites/default/files/d8/2019-09/docker-cheat-sheet.pdf)
- [python web flask](https://blog.techbridge.cc/2017/06/03/python-web-flask101-tutorial-introduction-and-environment-setup/)
## extension
- [x] python的decorator
    - 在定義函數前加上`@`，就是把定義的函數當成參數傳給`@`的函數
    - `@`也可以是class
    - `@`可以帶參數
        - 直接在`@`後面的函數加入要傳的參數
        - 把`@`的參數包成兩層，外層接受要傳的參數，內層接受後面定義的函數
- 什麼是`127.0.0.1`
    - 有著特殊用途的IPv4地址，也叫環路地址或者本地主機localhost
    - 用來ping `127.0.0.1`來看本地`ip/tcp`正不正常
    - [x] [參考](https://kknews.cc/zh-tw/news/8xvjekn.html)
- [ ] [實作一個flask的dockerfile試試](https://www.maxlist.xyz/2020/01/11/docker-flask/)