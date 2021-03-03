# Dockerfile
###### tags: `extension`
[TOC]
# 製作flask python docker
- [實作dockerfile+flask教學](https://www.maxlist.xyz/2020/01/11/docker-flask/)
## 寫dockerfile
- dockerfile一行指令對image來說就是一層的資料層(layer)
- 一個image就是靠一層一層的資料累加上去，最後編譯出自己想要的image
- 範例dockerfile
    ```
    FROM python:3.7.2-stretch
    WORKDIR /app
    ADD . /app
    RUN pip install -r requirements.txt
    CMD python main.py
    ```
- 參數:
    - FROM: 基底映像檔
    - WORKDIR: 工作目錄
    - ADD: 複製指定的檔案、目錄或遠端檔案URL，將其加入image的指定位置
    - RUN: 每一個RUN指令會在現有映像檔之上加入新的一層(layer)，是建立image的過程中會執行的指令
        - 如果有多行，使用&& \
        - 否則一個RUNcommand就會一個image
        ```
        RUN command && \
            command2
        ```
    - CMD: 在容器運行時所執行的指令
        - 只能有一個
## 把dockerfile打包成image
- `docker image build -t dockerfile_test .`
    - `docker build -t [image_name] [current_folder]`
## 透過image產生隔離的執行環境container
- `docker run -d -p 80:8888 --name docker123 dockerfile_test`
    - `-d`: 背景執行
    - `-p`: prot映射
    - `--name`: container名稱
## 測試
- 連線` 127.0.0.1:80`