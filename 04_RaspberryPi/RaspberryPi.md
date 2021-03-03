# Raspberry_Pi
###### tags: `AIOT`
[TOC]
## 知識點
- Raspberry Pi開機
## 筆記
- [Pi Imager](https://www.raspberrypi.org/software/)
- [Pi OS](https://www.raspberrypi.org/software/operating-systems/)
- [sd卡燒錄軟體](https://www.balena.io/etcher/)balenaEtcher
- 步驟:
    - 下載Pi os
    - 把映像檔燒到sd卡
- 電源問題
    - 建議5V3A
## 實作
- 燒錄sd卡並開機
## reference
## extension
- [金屬散熱外殼](https://www.youtube.com/watch?v=O7odXGh9kgE)
- [ssh and vnc](https://ithelp.ithome.com.tw/articles/10235452)
    - 獲得pi的address:
        - `ifconfig`
        - `hostname -I`
    - 啟用樹梅派的ssh(預設關閉)
        - `sudo raspi-config`
        - Interfacing Options
        - SSH
        - `// 回到主機`
        - `ssh pi@ip address`
- vnc樹梅派
    - 啟用樹梅派的vnc
    - 在VNC Viewer輸入ip address