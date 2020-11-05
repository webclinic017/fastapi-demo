#!usr/bin/env python
# -*- coding:utf-8 _*-
# 参考文档
# https://www.encode.io/databases/database_queries/
# https://stackoverflow.com/questions/30992092/sqlalchemy-how-to-get-raw-sql-from-insert-update-statements-with-binded-p


# 数据库表的各种操作

from app.db.models import Users
from app.db import database
from sqlalchemy import text,insert
from sqlalchemy.sql import select
from sqlalchemy.dialects import postgresql

class UserDAO:
    @classmethod
    async def get(cls, id):
        #第一种查询方法
        query = select([Users]).where(Users.id ==id)
        sql = str(query.compile(compile_kwargs={"literal_binds": True}))
        user = await database.fetch_one(query=sql)

        # # 第二种查询方法
        # query = "select * from users where id = :id"
        # values = {"id": 1}
        # user = await database.fetch_one(query=query, values=values)
        return user

    @classmethod
    async def create(cls, **user):
        # await db.connect()
        # update(Test).where(Test.a == 1).values(b=2)
        insert_stmt = insert(Users).values(**user)
        #insert_stmt = insert(Users).values(first_name ='2')
        #带着主键，所以无法执行
        #insert_sql = insert_stmt.compile(dialect=postgresql.dialect(),compile_kwargs={"literal_binds": True})
        #user = Users(**user)
        #query = str(user)
        user_id = await database.execute(insert_stmt)
        return user_id


