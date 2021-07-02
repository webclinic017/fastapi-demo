# fastapi-demo

fastapi tutorial and demo

*depends*:
python>=3.6

# runserver
0.setup

```
#利用python执行setup.py
python setup.py
```

*1.use python run server*

```buildoutcfg
python runserver.py
```

浏览器打开 http://127.0.0.1:8091/docs

*2.use uvicorn run server*  

```buildoutcfg
cd ./app
uvicorn main.app --host 0.0.0.0 --port 8091 --reload
```

# websocket
具体参考api/socket/test.py

# celery
具体参考task.py与test_tasks.py

celery运行后需要启动work,本项目使用主要参考
https://github.com/jitendrasinghiitg/docker-fastapi-celery

```
首先cd到task目录，然后执行命令启动celery的work
mac/linux用法如下：

cd ./app/task 
celery -A task.tasks worker -l info --logfile=w1.log
```

*todo:*  
windows启动,由于celery4.0以上版本  
```buildoutcfg
pip install eventlet
celery.exe -A  app.task.tasks worker -l info  -P eventlet --logfile=w1.log
```


# test
pytest进行接口的单元测试，分为以下两种：  
1.基于testClient进行启动服务测试  
2.用request模拟请求进行接口测试

# depoly

* **windows**

  * 执行setup.bat，指定源码包（修改setup.bat里边的python路径）

  * uvicorn运行

  ```
  D:\Python36-sim\Scripts\uvicorn.exe main:app --host "0.0.0.0" --port 8091 --reload
  ```

  ​	此时为单进程运行，稳定性较差

  * ~~gunicorn~~

     *** windows测试未通过，由于gunicorn暂时不支持windows

    ```
    #安装gunicorn
    pip install gunicorn
    #启动服务,开启守护进程
    D:\Python36-sim\Scripts\gunicorn main:app -b 0.0.0.0:8091  -w 4 -k uvicorn.workers.UvicornH11Worker --daemon  
    ```

  * circusd

    利用circusd开启守护进程

    * 配置curcus.ini文件

    ```
    [watcher:web]
    cmd = D:\Python36-sim\Scripts\uvicorn.exe --fd $(circus.sockets.web) main:app
    use_sockets = True
    numprocesses = 4
    
    [socket:web]
    host = 0.0.0.0
    port = 8092
    ```

    * circus启动

      ```
      D:\Python36-sim\Scripts\circusd.exe circus.ini
      
      ** 注意，windows上运行需要修改uvicorn的源码：
      查看uvicorn的安装目录，如d:\python36-sim\lib\site-packages\uvicorn，打开其中main.py，将其中socket.AF_UNIX修改成AF_INET
          # Use an existing socket, from a file descriptor.
          sock = socket.fromfd(config.fd, socket.AF_UNIX, socket.SOCK_STREAM)
          server = await loop.create_server(
          create_protocol, sock=sock, ssl=config.ssl, backlog=config.backlog
          )
          message = "Uvicorn running on socket %s (Press CTRL+C to quit)"
          logger.info(message % str(sock.getsockname()))
          self.servers = [server]
      ```

      

* **docker**

  ```
  #编译镜像
  cd fastapi-demo
  #利用depoly里边的Dockerfile进行构建镜像，具体参考Dock
  #*Dockerfile里边的目录是相对于当前命令行的，而不是Dockerfile文件的
  sudo docker build -t fastapi-demo -f ./depoly/Dockerfile .
  
  #启动容器
   sudo docker run -d --restart=always --name fastapi-demo -v /home/xyz/liearth/docker/fastapi_demo:/app -p 9071:80 fastapi-demo
  
  #具体参考https://github.com/tiangolo/uvicorn-gunicorn-fastapi-docker
  
  ```

  





