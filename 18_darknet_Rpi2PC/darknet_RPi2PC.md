# darknet_RPi2PC
###### tags: `AIOT`
[TOC]
## 知識點
- 在Rpi使用yolo inference`darknet.py`
- 將結果透過flask傳到WebAPI
## 筆記
### darknet環境
- 在Rpi上建置yolo環境
### darknet inference
- darknet_py_inference
    - 需求檔案:
        - 一張圖片:
            - `darknet/data/dog.jpg`
        - model cfg
            - tiny_v3: `darknet/cfg/yolov3-tiny.cfg`
            - tiny_v4: `darknet/cfg/yolov4-tiny.cfg`
        - weight:
            - [tiny_v3coco](https://pjreddie.com/media/files/yolov3-tiny.weights)
            - [tiny_v4coco](https://github.com/AlexeyAB/darknet/releases/download/darknet_yolo_v4_pre/yolov4-tiny.weights)
        - data:
            - `cfg/coco.data`
    - 使用darknet原始專案下的
        - `darknet_images.py`
        - `darknet.py`
### 結合Yolo和flask
- Rpi端:[flask_yolo](https://github.com/chihpy/AIOT/blob/main/D26_darknet_Rpi2PC/flask_yolo.py)
- PC端: [get_flask](https://github.com/chihpy/AIOT/blob/main/D26_darknet_Rpi2PC/get_flask.py)

## reference
- 舊版[performDetect](https://github.com/gengyanlei/fire-detect-yolov4/blob/master/yolov4/darknet.py)
## extension
- [static_shared_dynamically](https://blog.xuite.net/tzeng015/twblog/113272198)
    - libdarknet.so: Shared libraries
        - soname
            - 用來表示是一個特定library的名稱，像是libmylib.so.1
            - 以lib開頭，接著是library的名稱，然後是.so接著版號
        - real name
            - 實際放有library程式的檔案名稱，後面會再加上minor版號與release版號
            - 例子:libmylib.so.1.0.0
            - 尾碼release版號用於程式內容修正，介面沒有改變
            - 中間的minor用於有新增加介面，但舊介面沒改變，所以與舊版本相容
            - 最前面的version版號用於原介面有移除或改變，與舊版本不相容時
        - linker name
            - 用於連結時的名稱，是不含版號的soname，如libmylib.so
            - 通常linker name與real name是用ln只到對應的real name來提供彈性與維護性
- netstat: 
- ![](https://i.imgur.com/u4WOhCl.png)
