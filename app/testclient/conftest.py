from fastapi.testclient import TestClient
import pytest
from .app import app
'''
测试用TestClient自动化测试服务
'''

@pytest.fixture(scope="module")
def test_app():
    '''
    如果通过官方文档，继承该方法的用法，无法调研startup事件
    :return:
    '''
    client = TestClient(app)
    yield client  # testing happens here


