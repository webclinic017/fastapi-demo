#!usr/bin/env python
# -*- coding:utf-8 _*-

'''
初始化数据库定义
'''

import os
from databases import Database
from sqlalchemy import MetaData
DATABASE_URL = os.environ.get("DATABASE_URL")
if DATABASE_URL:
    database = Database(DATABASE_URL)
metadata = MetaData()
from sqlalchemy.ext.declarative import declarative_base
db_model = declarative_base()