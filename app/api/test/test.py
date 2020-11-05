from typing import Optional
from app.core.utils import return_msg
from app.core.utils import SERVER_STATUS

from app.api.route import get_router
test_router = get_router()

@test_router.get('/hello')
def hello():
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

