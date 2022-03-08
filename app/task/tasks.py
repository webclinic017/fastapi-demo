import traceback
from time import sleep

from celery import states

from .work import celery

from celery.contrib.abortable import AbortableTask,AbortableAsyncResult


# 注册一个测试的长耗时事件
@celery.task(name='hello.task', bind=True,base=AbortableTask)

def hello_world(self, name):
    try:
        if name == 'error':
            k = 1 / 0
        for i in range(300):

            task_id = self.request.id
            print(task_id)
            task = celery.AsyncResult(task_id)
            print(task.state)

            # check aborted 任务
            # task_id = self.request.id
            # #print(task_id)
            # task = AbortableAsyncResult(task_id)
            # #print('check', task.state)
            #
            # if task.state=='ABORTED':
            #     return {"result": "abort {}".format(str(name))}

            # # 判断任务是否revoked
            # if task.state == "REVOKED":
            #     self.update_state(state='SUCCESS')
            #     return {"result": "REVOKED {}".format(str(name))}

            sleep(1)
            #log info to celery.log
            #print('hello test')
            self.update_state(state='PROGRESS', meta={'done': i, 'total': 300})
        return {"result": "hello {}".format(str(name))}
    except Exception as ex:
        self.update_state(
            state=states.FAILURE,
            meta={
                'exc_type': type(ex).__name__,
                'exc_message': traceback.format_exc().split('\n')
            })
        raise ex



