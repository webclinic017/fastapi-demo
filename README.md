# fastapi-demo

fastapi tutorial and demo

*depends*:
python>=3.6

# runserver
*1.use python*
```buildoutcfg
python runserver.py
```

浏览器打开 http://127.0.0.1:8091/docs

*2.use uvicorn* 
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
windows启动 **待验证**  
celery.exe -A  task.tasks worker -l info  -P eventlet

# test
pytest进行接口的单元测试，分为以下两种：  
1.基于testClient进行启动服务测试  
2.用request模拟请求进行接口测试

# docker
待添加测试



