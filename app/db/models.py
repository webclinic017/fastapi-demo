#!usr/bin/env python
# -*- coding:utf-8 _*-

#数据库的model
from app.db import metadata
import sqlalchemy
from app.db import db_model
from sqlalchemy import Column, String, Integer

# class Citys(db_model):
#     __tablename__ = 'cities'
#     __table_args__ = {"useexisting": True}
#     id = Column(Integer, primary_key=True)
#     name  = Column(String)
#     population  = Column(Integer)
#
#
#
# class Capitals(db_model):
#     __tablename__ = 'capitals'
#     __table_args__ = {"useexisting": True}
#     id = Column(Integer, primary_key=True)
#     name = Column(String)
#     population = Column(Integer)
#     state = Column(String(2))


Users = sqlalchemy.Table(
    "test_users",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("first_name", sqlalchemy.String),
    sqlalchemy.Column("last_name", sqlalchemy.String),
    sqlalchemy.Column("age", sqlalchemy.Integer),
)


if __name__ =="__main__":

    #test create 数据库,只在此处新建一次数据库
    #建表时注释__init__.py里边的以下两行
    #DATABASE_URL = os.environ.get("DATABASE_URL")
    #database = Database(DATABASE_URL)
    # 新建数据库操作
    #pgadmin 新建数据库，编码选择utf-8,模板选择template0
    DATABASE_URL = "postgresql://test:test@127.0.0.1:5432/test"
    engine = sqlalchemy.create_engine(
        DATABASE_URL, #connect_args={"check_same_thread": False}
    )
    db_model.metadata.create_all(bind=engine)

    # #指定创建某些表
    # db_model.metadata.create_all(bind=engine,tables=[Citys.__table__])
    #
    # #创建一个继承的子表
    # str_sql = "CREATE TABLE capitals (state  char(2)) INHERITS (cities);"
    # from sqlalchemy.orm import Session
    # s = Session(engine)
    # s.execute(str_sql)
    # s.commit()
    # s.close()

