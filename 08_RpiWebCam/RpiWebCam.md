# RpiWebCam
###### tags: `AIOT`
[TOC]
## 知識點
- video4Linux
- fswebcam
- 透過python呼叫fswebcam
## 筆記
### video4Linux(V4L)
- Video4Linux(V4L)是視訊擷取及裝置輸出的API
- 兩層架構
    - 底層為影音設備在核心中的驅動程式
    - 上層為系統提供的API
- 當/dev內有某個檔案名稱出現時，代表作業系統與外部周邊裝置使用某一個方式來進行資料的存取
    - `/dev/videoX`, `/dev/vbiX`, `/dev/radioX`, `/dev/swradioX`, `/dev/v4l-subdevX`
    - recall: dev是device的縮寫，放置裝置檔，包括硬碟檔、鍵盤滑鼠檔案
- 安裝v4l2以python存取video4Linux
    - pip裝的有可能import會有錯
    - [fork v4l2 github page](https://github.com/antmicro/python3-v4l2)一個修正過的v4l2模組
### UVC
- USB Video Class(USB Video device class)
- 目的是提供視訊產品不需要安裝任何驅動程式即插即用
- Linux上如果有一個支援UVC的Webcam插到USB，就會向kernel註冊為Webcam設備，裝置節點為`/dev/videoX`
- V4L2用來管理UVC裝置
- 判斷視訊裝置是否支援UVC:
    - `lsusb`
    - `lsusb -v | grep 14 Video`
    - 如果相容UVC則會輸出
        - `bFunctionClass 14 Video`
        - `bInterfaceClass 14 Video`
### fswebcam
- 安裝: `sudo apt install fswebcam`
- 拍照: `fswebcam image.jpg`
- 設定影像解析度，忽略前10張，由/dev/video0裝置取得資料，儲存在webcam.jpg
    ```
    fswebcam -r 640x360 -S 10 -d /dev/vodeo0 webcam.jpg
    ```
- 可以透過crontab設定定時的執行來執行固定時間的拍照動作
    ```
    fswebcam -c fs.conf
    # fs.conf內容是fswebcam執行時所設定的參數
    ```
- `fswebcam -c fs.conf`
- `ps -e | grep fs`
- `kill -9 PID`
## 實作
## reference
- [Linux下Camera程式設計-V4L2](https://codertw.com/%E7%A8%8B%E5%BC%8F%E8%AA%9E%E8%A8%80/465905/)
- [fswebcam](https://github.com/fsphil/fswebcam)
## extension