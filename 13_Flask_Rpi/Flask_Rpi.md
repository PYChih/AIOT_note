# Rpi_flask
###### tags: `AIOT`
[TOC]
## 知識點
- 在樹梅派上建立flask Web
- 利用Web API控制GPIO達到控制周邊的目的
    - 網頁上點擊按鈕，讓樹梅派接收，並做響應的處理，實作網頁與樹梅派數據交換
    - 控制樹梅派周邊
## 筆記
- 在相同網域下可以由本機訪問樹梅派上的flask網頁
- [x] 樹梅派上執行flask，由PC端訪問(相同wifi)
### 規範網頁的文件架構
- 一個文進存儲HTML，一個放CSS(JS?)
- project
    - templates
        - index.html
            - 裡面對應點擊事件
    - static
### 設定並啟用index-
- 基於flask搭建web服務，樹梅派接收web傳過來的點擊事件，並做出相應動作
    - 使用get提交操作請求
    - 使用post處理gpio操作
- 範例:
    ```
    @app.route('/fopen', methods=['POST', 'GET'])
    def fopen():
        if request.method == 'GET':
            return render_template('index.html')
        else:
            single.flushOutput()
            single.write('1')
            return "open OK"
    ```
## 實作
- [x] 以flask實作接收一個點擊的網頁，跑在樹梅派上，如果PC端連上網頁並點擊按鈕，則樹梅派點亮LED燈
## reference
- [html預覽器](http://myweb.ncku.edu.tw/~arter/20171212/source.cgi)
- [實現參考: 樹梅派點亮LED](https://www.cnblogs.com/ttssrs/p/4890635.html)
## extension
- [GPIO.cleanup()](https://magic-panda-engineer.github.io/RaspberryPi/correct-way-to-use-GPIO-cleanup)
