# Flask
###### tags: `AIOT`
[TOC]
## 知識點
- Http Method介紹
    - 使用Get Method取得網頁資料
    - 使用Post上傳檔案
    - 取得Server上的檔案
## 筆記
### Http method
- HTTP 1.1 的八種方法:
    - OPTIONS
    - GET:
        - 向指定資源發出顯示的請求
        - 帶參數必須加在網址後的Query-String
        - 所以通常GET只會用在讀取資料
    - HEAD
    - POST
        - POST不會把要傳送的資料放進網址中，而是放在message-body
    - PUT
    - DELETE
    - TRACE
    - CONNECT
### Http Method與資料操作對應
- C->create->POST
- R->Read->GET
- U->Update->PUT
- D->Delete->DELETE
## 實作
- 用flask實作read(get) Hello World
- 使用get取得request中的參數
- 使用post傳遞參數資料
- 使用Post檔案上傳單一檔案
- 使用Post檔案上傳多個檔案
- 取得Flask Server上的檔案
- 回傳HTML畫面

## reference
- [超文本傳輸協定HTTP](https://zh.wikipedia.org/wiki/%E8%B6%85%E6%96%87%E6%9C%AC%E4%BC%A0%E8%BE%93%E5%8D%8F%E8%AE%AE)維基
## extension