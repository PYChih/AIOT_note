# python GPIO
###### tags: `AIOT`
[TOC]
## 知識點
- RaspberryPi GPIO函式庫
    - RPI.GPIO, pigpio, GPIOZero
- GPIO PWM控制LED
## 筆記
- RPI.GPIO
    - `apt update`
    - `apt install python3-rpi.gpio`
    - 單純只用pip3 install有時候會失敗
    - [參考官網](https://sourceforge.net/p/raspberry-gpio-python/wiki/install/)
- pigpio
    - [github](https://github.com/joan2937/pigpio)
    - 原始碼安裝
        - `wget https://github.com/joan2937/pigpio/archive/master.zip`
        - `unzip`
        - `make`
        - `sudo make install`
    - `sudo apt install python-setuptools python3-setuptools`
    - 執行`./x_pigpio`測試
- GPIOZero
    - GPIOZero使用了RPi.GPIO以及pigpio的函式庫為基礎，因此要先安裝RPi.GPIO以及pigpio
    - `pip3 install gpiozero`
- 比較
    - RPi.GPIO只能使用軟體的PWM，無法支援硬體PWM工作方式
    - pigpio由pigpio 函式庫移植至python，除了軟體還提供硬體PWM支援，對於LED以及伺服馬達的控制，相對因為提供硬體PWM支援，讓開發人員好寫很多
## 實作
- GPIOZero閃爍LED
    - LED(4)指的是GPIO4
- GPIOZero控制LED燈明亮
    - PWM主要是控制週期時間內GPIO開關的次數，來達成功率控制的效果(pulse width modulation)
## reference
## extension
- 在RPI使用python虛擬環境
    - [參考](https://dsalearning.github.io/aiot/raspberry-pip3-create-env/)
    - `pip3 install --upgrade pip`
    - `pip3 list`
    - `sudo pip3 install virtualenv`
        - 用sudo
    - `sudo virtualenv [envname]`
    - `sudo chown -R pi:pi [envname]`
        - 因為是root建的，之後用pi進去會沒權限
    - `cd [envdir]`
    - `source bin/activate`
        - `source /home/pi/Documents/envs/pygpio/bin/activate`
    - `deactivate`
    - 幾個常用命令:
        - 檢查已安裝程式
            - `pip3 list`
        - 刪除環境
            - 直接刪資料夾
- vscode遠程開發樹梅派
    - [參考](https://www.w3xue.com/exp/article/20204/82577.html)
    - [除錯](https://github.com/microsoft/vscode-remote-release/issues/2805)
        - remote-ssh:kill vscode server on host