# Rpi_inference_yolo
###### tags: `AIOT`
[TOC]
## 知識點
- inference yolo on RPi
- inference using python
## 筆記
- file prepare
- environment on RPi
- inference
- note:
    - `.sh`cp不了有時候是因為權限問題
### argparse的使用:
- 位置參數
- 可選參數
- 短選項
- flag
- count
- default
- 矛盾選項(add_mutually_exclusive_group())
## 實作
- yolo_v3_inference_Rpi4B_darknet_without_opencv
    - 大約70秒
![](https://i.imgur.com/TPNeKi8.png)

- [ ] tiny_yolo_v3_inference_Rpi4B_darknet_without_opencv
- [ ] yolo_v4_inference_Rpi4B_darknet_without_opencv
- [ ] tiny_yolo_v4_inference_Rpi4B_darknet_without_opencv
## reference
- [argparse教學](https://docs.python.org/zh-tw/3/howto/argparse.html)
## extension
- [ ] [darknet_nnpack](darknet-nnpack)
- [ ] [yolo_int8](https://github.com/AlexeyAB/yolo2_light) 