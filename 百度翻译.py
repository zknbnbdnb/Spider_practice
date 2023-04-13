import requests
import json
from lxml import etree
import os


# 百度翻译

if __name__ == '__main__':
    # UA伪装
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36'
    }
    # 指定URL
    url = 'https://fanyi.baidu.com/sug'
    # post请求参数处理
    kw = input('enter a word: ')
    data = {
        'kw': kw
    }
    # 请求发送
    response = requests.post(url=url, data=data, headers=headers)
    # 获取反映数据:json返回的是obj
    dicObj = response.json()
    # 进行持久化存储
    filename = kw+'.json'
    fp = open(filename, 'w', encoding='utf-8')
    json.dump(dicObj, fp=fp, ensure_ascii=False, indent=4)
    print('over')