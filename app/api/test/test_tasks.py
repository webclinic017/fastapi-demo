import json

from pydantic import BaseModel

from app.api.route import get_router
from app.task.work import celery

task_router = get_router()

class Item(BaseModel):
    name: str

#from app.celery.tasks import hello_world

@task_router.post("/task_hello_world/")
async def create_item(item: Item):
    task_name = "hello.task"
    task = celery.send_task(task_name, args=[item.name])
    return dict(id=task.id, url='localhost:9003/check_task/{}'.format(task.id))


@task_router.get("/check_task/{id}")
def check_task(id: str):
    ins = celery.control.inspect()
    task = celery.AsyncResult(id)
    if task.state == 'SUCCESS':
        response = {
            'status': task.state,
            'result': task.result,
            'task_id': id
        }
    elif task.state == 'FAILURE':
        response = json.loads(task.backend.get(task.backend.get_key_for_task(task.id)).decode('utf-8'))
        del response['children']
        del response['traceback']
    else:
        response = {
            'status': task.state,
            'result': task.info,
            'task_id': id
        }
    return response
