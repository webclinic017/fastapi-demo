import json

def setup_module():
    print("setup_module：当前py模块只执行一次")

def teardown_module():
    print("teardown_module：当前py模块只执行一次")


def test_1():
    assert 1==1
# def test_create_user(test_app, monkeypatch):
#     test_request_payload ={"first_name":"555","last_name":"5555","age":0}
#     test_response_payload ={
#         "status": 1,
#         "msg": "",
#         "data": {
#             "user_id": 4
#         }
#     }
#
#     #async def mock_post(payload):
#         #await User.create(payload)
#         #return 1
#
#     #monkeypatch.setattr(User, "create", mock_post)
#
#     response = test_app.post("/pw/user/", data=json.dumps(test_request_payload))
#
#     assert response.status_code == 200
#     res = response.json()
#     assert res['status']== 1





