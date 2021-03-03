# Rpi GPIO
###### tags: `AIOT`
[TOC]
## 知識點
- 接腳說明
    - 5V、3.3V、RX、TX、SPI、I2C、GPIO
- `/sys/class/gpio`
- `/sys/kernel/debug/gpio`
## 筆記
- [RaspberryPi接腳說明](https://atceiling.blogspot.com/2014/01/raspberry-pigpio.html)
    - note: 第4個接腳是5v，第6個接腳是GND，所以風扇接這
- 接腳用途
    - GPIO:
        - 不啟動I2C、SPI等介面，可提供最多24個GPIO接腳進行數位訊號輸入輸出
    - I2C
        - 可以將3、5接腳(GPIO2、3)切換為I2C
    - SPI
        - 9個(19、21、23、24、26、35、36、38、40)
- sysfs介紹
    - sysfs把原本放在procfs關於裝置部分獨立出來，以裝置階層架構(device tree)型式呈現
    - 被加入driver model tree內的物件，包括驅動程式、裝置，以及class裝置，都會在sysfs檔案系統中以一個目錄呈現
    - 物件的屬性以檔案出現，符號連結代表物件間的關係，通常安裝在/sys目錄
        - recall: /sys跟/proc類似，只是比較針對硬體相關的參數方面
    - `ls sys`
        - ![](https://i.imgur.com/Q3cGoYd.png)
        - `/sys/class/input`: USB的滑鼠是輸入設備，應該會在這裡
        - `/sys/class/gpio`: GPIO在這
- 控制GPIO:
    - 啟動GPIO
        - echo 4> /sys/class/gpio/export
    - 設定GPIO4為輸出
        - echo out> /sys/class/gpio/gpio4/directions
    - 設定GPIO4輸出值為1(0:低電位，1:高電位)
        - echo 1> /sys/class/gpio/gpio4/value
    - 將GPIO4卸載，不用sysfs控制
        - echo 4> /sys/class/gpio/unexport
- debugfs觀察GPIO設定
    - `cat /sys/kernel/debug/gpio`
- SPI、I2C、Serial(TXRX)、RemoteGPIO都是在respi-config改
## 實作
- 使用sysfs點亮LED燈
## reference
- [x] [Raspberry Pi LEG閃爍](https://coldnew.github.io/f7349436/)
- [ ] [使用/sys訪問內核](https://www.ibm.com/developerworks/cn/linux/l-cn-sysfs/index.html)
- [ ] [procfs, sysfs, debugfs簡介](https://www.itread01.com/content/1549273141.html)
## extension