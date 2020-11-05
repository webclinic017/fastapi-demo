#!usr/bin/env python
# -*- coding:utf-8 _*-

from enum import Enum
import sys
import traceback
from functools import wraps

def return_msg(status, msg='', data=None, log=None):
    """
    统一服务的返回结果
    :param status: 状态 0, 1, -1
    :param msg:  返回消息
    :param data: 服务成功时，返回数据
    :param log:  服务异常时，打印日志
    :return: dict
    """
    result = {
        "status": status,
        "msg": msg,
    }
    if data is not None:
        result["data"] = data
    if log is not None:
        log.error(log)
    return result


def try_exception(f):
    """
    A decorator that wraps the passed in function and logs
    exceptions should one occur
    """
    @wraps(f)
    def wrapper(*args, **kwargs):
        try:
            return f(*args, **kwargs)
        except Exception as e:
            exc_type, exc_instance, exc_traceback = sys.exc_info()
            formatted_tbtext = traceback.format_tb(exc_traceback.tb_next)
            error = '\n[Exception]:{0}-{1}'.format(formatted_tbtext, exc_instance)
            return return_msg(-1, msg='exception %s' % e, log=error)
    return wrapper


#
# def get_cur_fun_name():
#     return inspect.stack()[1][3]

class SERVER_STATUS(Enum):
    OK = 1
    ERROR = 0
    EXCEPTION = -1

if __name__ == '__main__':
    pass
