import requests
import json
def test_hello(get_conf,test_login):
    '''
    curl -X GET "http://127.0.0.1:8091/hello" -H  "accept: application/json"
    :return:
    '''
    conf = get_conf

    headers = {
        'Content-type': 'application/json',
    }

    url = conf['rootUrl']+'/hello'

    res = requests.get(url=url, headers=headers)
    assert res.status_code ==200

    rs =res.json()
    assert  rs['status']==1


def test_add_user(get_conf,test_login):
    '''
        curl -X POST "http://127.0.0.1:8091/user/" -H  "accept: application/json" -H  "Content-Type: application/json" -d "{\"first_name\":\"333333\",\"last_name\":\"123444\",\"age\":0}"
    :return:
    '''
    test_request_payload = {"first_name": "12555", "last_name": "5555", "age": 0}

    conf = get_conf
    headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
    url = conf['rootUrl'] + '/pw/user/'

    #如果数据已经存在
    res = requests.post(url=url, headers=headers,data=json.dumps(test_request_payload))

    assert res.status_code == 200

