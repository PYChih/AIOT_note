# Linux_command
###### tags: `AIOT`
[TOC]
## 知識點
- Raspberry PI 系統管理
    - sudo
    - raspi-config
    - apt
    - systemctl
    - cron
    - /etc/crontab
    - date

- Linux 的檔案管理、權限控制、裝置掛載、檔案下載
- Linux 檔案文字編輯器
- Linux 檔案壓縮
- Linux 網路設定
    - ip
    ```
    /etc/wpa_supplicant/wpa_supplicant.conf
    ```
## 筆記
- `/etc/sudoers`可以設定哪一個使用者可以採用sudo取得系統管理者權限
- recall: /etc裡面放的就是一堆系統設定檔
- raspi-config
    - 只有super user可以使用`sudo su`
    - 硬體接腳設定在Interfacing Options選項中
        - 啟動i2c
        - spi
        - RX/TX接腳介面的設定(Serial)
        - 1-Wire
        - Remote GPIO
- systemctl設定開機時自動啟動背景服務
- cron設定週期執行指令
    - cron透過systemctl可以設定開機之後就自動執行
    - 將`/etc/crontab`的設定載入至記憶體中
    - 透過`/etc/crontab`設定固定多少分鐘執行一次指令
- linux基礎指令
    - uptime: 目前從開機到現在已經經過多久的時間(可以觀察是否有不穩定重開機)
- wpa_supplicant
    - 按照格式修改 ssid (無線基地台名稱) 與 psk (無線基地台的密碼)，可以設定很多個基地台的資料，方便在不同場地自動登入。
## reference
- [ ] [systemctl](https://blog.gtwang.org/linux/linux-basic-systemctl-systemd-service-unit-tutorial-examples/)
- [ ] [crontab](https://blog.gtwang.org/linux/linux-crontab-cron-job-tutorial-and-examples/)
## extension