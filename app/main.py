#!usr/bin/env python
# -*- coding:utf-8 _*-

from fastapi import FastAPI
import logging
from .core.fs_logging import CustomizeLogger
from .config.config import fs_config
from app.db import database #SessionLocal
#from app.celery.work import celery

#创建数据库
#metadata.create_all(engine)
logger = logging.getLogger(__name__)

#添加路由，类似flask 蓝图
from app.api.test.test import test_router
from app.api.user.user import user_router
from app.api.socket.test import socker_router
from app.api.test.test_tasks import task_router

def create_app() -> FastAPI:
    #定义app对象
    app = FastAPI() #FastAPI(title='CustomLogger', debug=False)
    app.config = fs_config

    #init config
    logger = CustomizeLogger.make_logger(app.config)
    app.logger = logger

    #注册路由
    app.include_router(user_router)
    app.include_router(socker_router)

    #测试路由
    app.include_router(test_router)
    app.include_router(task_router)

    #init db
    app.database = database
    return app

app = create_app()


# websocket
from fastapi import WebSocket,WebSocketDisconnect
from app.core.fs_socket import manager


@app.websocket("/ws/{client_id}")
async def websocket_endpoint(websocket: WebSocket, client_id: int):
    '''
    定义websocket
    :param websocket:
    :param client_id:
    :return:
    '''
    await manager.connect(websocket)
    try:
        while True:
            data = await websocket.receive_text()
            await manager.send_personal_message(f"You wrote: {data}", websocket)
            await manager.broadcast(f"Client #{client_id} says: {data}")
    except WebSocketDisconnect:
        manager.disconnect(websocket)
        await manager.broadcast(f"Client #{client_id} left the chat")

# 服务启动事件
@app.on_event("startup")
async def startup():
    await database.connect()

# 服务关闭事件
@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()
