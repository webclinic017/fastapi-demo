#!usr/bin/env python
# -*- coding:utf-8 _*-

#数据库的model
from app.db import metadata
import sqlalchemy
from app.db import db_model
from sqlalchemy import Column, String, Integer

class Users(db_model):
    __tablename__ = 'users'
    __table_args__ = {"useexisting": True}
    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    age = Column(Integer)


# users = sqlalchemy.Table(
#     "test_users",
#     metadata,
#     sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
#     sqlalchemy.Column("first_name", sqlalchemy.String),
#     sqlalchemy.Column("last_name", sqlalchemy.String),
#     sqlalchemy.Column("age", sqlalchemy.Integer),
# )


if __name__ =="__main__":

    #test create 数据库,只在此处新建一次数据库
    #建表时注释__init__.py里边的以下两行
    #DATABASE_URL = os.environ.get("DATABASE_URL")
    #database = Database(DATABASE_URL)

    DATABASE_URL = "postgresql://postgres:123@127.0.0.1:5432/test"
    engine = sqlalchemy.create_engine(
        DATABASE_URL, #connect_args={"check_same_thread": False}
    )
    db_model.metadata.create_all(bind=engine)