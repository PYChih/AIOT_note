# YOLO_train
###### tags: `AIOT`
[TOC]
## 知識點
- yolo_v3 with darknet
## 筆記
### colab workflow
- 由於實例釋放後所有數據會清空，所以記得訓練中要把backup寫到drive(日誌、ckpt等)
- data壓縮單文件到drive再mount進來
- 額外一個section安裝環境以及數據解壓

## 實作
- training a face detection model with yolo
- 把步驟寫成sh
### environment
- darknet
- google_drive
    - dataset路徑
    - backup路徑
### data_preprocessing
- data preprocessing
- training config
### training
- cp config
- train
    - training info:
## reference
- [AlexeyAB/darknet](https://github.com/AlexeyAB/darknet#how-to-train-to-detect-your-custom-objects)
- [yolo2_light_int8](https://github.com/AlexeyAB/yolo2_light)
- [yolov4_on_colab_only_inference](https://colab.research.google.com/drive/12QusaaRj_lUwCGDvQNfICpa7kA7_a2dE)
- [darknet cfg參數定義](https://zhuanlan.zhihu.com/p/59560109)
## extension
- [ ] yolo_v4_darknet
- [ ] tiny_yolo_v4_with_widerface
