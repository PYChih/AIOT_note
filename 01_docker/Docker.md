# Docker
###### tags: `AIOT`
[TOC]
## 知識點
- Docker基本架構
- 安裝、設定Docker
- 學習使用指令操作Docker
## 筆記
- Docker基本構成元素:
    - Image
    - Container
        - container和image就好像class和instance
    - Registry
## 實作
### docker基本操作:
- [x] 取得、查看、刪除image
    - 取得:
        - `docker pull ubuntu:18.04`
            - [ubuntu docker hub](https://hub.docker.com/_/ubuntu?tab=tags&page=1&ordering=last_updated)
        - `docker pull tensorflow/tensorflow:latest-gpu-jupyter`
            - [tensorflow docker hub](https://hub.docker.com/r/tensorflow/tensorflow)
    - 查看:
        - `docker images`
            - 會列出現有的docker images
    - 刪除:
        - `docker rmi <image id>`
- [x] 建立、啟動、進入、停止、刪除Container
    - 建立
        - `docker run [image name]:[image tag] [command]`
            - 預設tag是latest
    - 查看
        - `docker ps`
            - 查看running中的container
        - `docker ps -a`
            - 查看所有container(包含已停止的)
    - 啟動
        - docker run = docker create + docker start
    - 進入
        - `docker exec [container name] [command]`
            - `-it`: interactive and tty
    - 停止
        - `docker stop [container name/ id]`
    - 刪除
        - `docker rm [container name/id]`
        - `docker rm -f [container name/id]`
### container帶著走
- [x] 匯入Container
    - `cat [finename.tar] | docker import -[container name]:[tag]`
        - tag預設是latest
- [x] 匯出Container
    - `docker export [container name/id] > [filename.tar]`
### container與主機的資料共享
- [x] 直接指定實體主機路徑(bind mount)
    - `docker run -it -v [host dir]:[container dir] --name [container name] [image name] [command]`
        - 實體主機目錄必須是絕對路徑
- [x] 建立Volume
    - `docker volume create [volumename]`
    - `docker volume ls`
    - `docker volume inspece [volume name]`
- [x] 啟動Container並連結Volume
    - `docker run -v [volume name]:[container dir] [imagename]`
- [x] Container之間的資料共享
    - `docker run -it --volumes-from container1 --name container2 [imagename] [command]`
- [x] 外部存取Container內的服務
    - `docker run -d -P [imagename]`
    - `docker run -d -p [hostport]:[containerport] [imagename]`
- [x] Container互聯
    - `docker run -it --name container2 --link [container1] [imagename] [command]`
    - in cantainer1 ping container2
    - `ping container2`
## reference
- [Docker菜鳥教程](https://www.runoob.com/docker/docker-tutorial.html)
- [Docker入門到實踐](https://philipzheng.gitbook.io/docker_practice/)
## extension