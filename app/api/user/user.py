#!usr/bin/env python
# -*- coding:utf-8 _*-
from app.core.utils import return_msg
from app.core.utils import SERVER_STATUS

from app.db.dao.user_dao import UserDAO
from app.db.schema import User as SchemaUser
from fastapi import Request

from app.api.route import get_router
user_router = get_router()

@user_router.post("/user/")
async def create_user(user: SchemaUser,request: Request):#,db: Session = Depends(check_db)
    #获取全局app的参数
    #print(request.app.config)
    user_id = await UserDAO.create(**user.dict())
    return return_msg(status=SERVER_STATUS.OK,data={"user_id": user_id})


@user_router.get("/user/{id}")
async def get_user(id: int):
    #用db执行
    #query = ModelUser.insert().values(first_name=SchemaUser.first_name)
    #last_record_id = await app.db.execute(query)
    user = await UserDAO.get(id)
    return return_msg(status=SERVER_STATUS.OK, data=SchemaUser(**user).dict())

