from fastapi.testclient import TestClient
import pytest
from app.main import app

# @pytest.fixture(scope="module")
# def test_app():
#     client = TestClient(app)
#     yield client  # testing happens here

#整个测试执行一次
@pytest.fixture(scope='session')
def get_conf():
    #config
    return {
        'token':'11111',
        'rootUrl':'http://127.0.0.1:8091'
    }

#每个函数依赖都会被执行
@pytest.fixture(scope="function")
def test_login():
    #login
    pass

