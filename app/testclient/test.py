
from fastapi.testclient import TestClient

from app.testclient.app import app

data ={}


def setup_module():
    with TestClient(app) as client:
        data['client'] = client
    print("setup_module：当前py模块只执行一次")

# def test_1(test_app):
'''
无法调用startup事件
'''
#     response = test_app.get("/items/foo")
#     assert response.status_code == 200
#     assert response.json() == {"name": "Fighters"}


def test_read_items():
    '''
    可以调用startup事件的用法
    :return:
    '''
    client = data['client']
    #with TestClient(app) as client: #可以调用startup事件的用法
    response = client.get("/items/foo")
    assert response.status_code == 200
    assert response.json() == {"name": "Fighters"}
