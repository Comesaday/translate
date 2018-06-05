import requests
import json

def translate(word=None):
    url='http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule'
    Form_data={
        'i':word,
        'from': 'AUTO',
        'to': 'AUTO',
        'smartresult': 'dict',
        'client': 'fanyideskweb',
        'salt': '1528199964615',
        'sign': 'f6cf55466c876c404ff85ea3fc8c453f',
        'doctype': 'json',
        'version': '2.1',
        'keyfrom': 'fanyi.web',
        'action': 'FY_BY_REALTIME',
        'typoResult': 'false'
    }
    response=requests.post(url=url,data=Form_data)
    content=json.loads(response.text)
    print(content['translateResult'][0][0]['tgt'])
    
if __name__ == '__main__':
    print("请输入单词或句子！")
    string=input()
    translate(string)
    