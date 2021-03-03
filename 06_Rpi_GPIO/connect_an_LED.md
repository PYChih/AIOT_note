# 使用sysfs點亮LED燈
###### tags: `RPI`
[TOC]
- 電阻:
    - 需要一個470K歐姆的電阻:
        - 黃(4)
        - 紫(7)
        - 綜(10^1)
    - 棕1黑0黑0橙3金
        - 100k ohms 5%
    - 電阻的方向:
        - 通常金銀棕會是末尾色環
- 麵包板的背面
    - [認識麵包版](https://blog.jmaker.com.tw/breadboard/)
    ![](https://i.imgur.com/VREji52.png)
- 接腳用途
    ![](https://i.imgur.com/s5qR1Hl.png)
    - [參考](https://ithelp.ithome.com.tw/articles/10215294)
    - note: 除了右邊第3個以外，左邊第5個，右邊第七個也都是GND
    - 接腳對照圖
    ![](https://i.imgur.com/bVEQYmr.png)
## LED開關
- [參考](https://coldnew.github.io/f7349436/)
- gpio4接到麵包版(左邊第四)
- 接到電阻
- 接到LED
    - note: led的正極一般比較長
    - 長腳接正極，短腳接地
- 接到板子的GND(左邊第5)
### 使用指令控制
- 要用root
- `echo 4 > /sys/class/gpio/export`
    - 把gpio4開起來
    - 會在`/sys/class/gpio`看到gpio4的檔案
- `echo out > /sys/class/gpio/gpio4/direction`
    - 設定完out之後預設會是低電位
- `echo 1 > /sys/class/gpio/gpio4/value`
    - LED就亮了
- `echo 4 > /sys/class/gpio/unexport`
    - 關閉GPIO4