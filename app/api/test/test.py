from typing import Optional
from app.core.utils import return_msg
from app.core.utils import SERVER_STATUS

from app.api.route import get_router
test_router = get_router()

#https://fastapi.tiangolo.com/async/
#对于接口是否需要async 定义的理解
#对于调用方法提供需要await调用，则需要用async
#对于直接返回结果的，也需要用async
#对于需要长时间其他操作的，不用async
#如果不确定，不用async
from fastapi_cache.decorator import cache

@test_router.get('/hello')
@cache(expire=60)
async def hello():
    '''
    just for test
    :return:
    '''
    # 测试数据
    data = {
        'code': "200",
        'data': "test success",
    }
    #a=1/0
    return  return_msg(status=SERVER_STATUS.OK,data=data,msg="")

