import traceback
from time import sleep

from celery import states

from .work import celery


# 注册一个测试的长耗时事件
@celery.task(name='hello.task', bind=True)
def hello_world(self, name):
    try:
        if name == 'error':
            k = 1 / 0
        for i in range(60):
            sleep(1)
            self.update_state(state='PROGRESS', meta={'done': i, 'total': 60})
        return {"result": "hello {}".format(str(name))}
    except Exception as ex:
        self.update_state(
            state=states.FAILURE,
            meta={
                'exc_type': type(ex).__name__,
                'exc_message': traceback.format_exc().split('\n')
            })
        raise ex



