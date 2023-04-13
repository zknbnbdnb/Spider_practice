import requests
import json
from lxml import etree
import os

# KFC店铺

if __name__ == '__main__':
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36'
    }
    url = 'http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=keyword'
    kw= input('enter a word: ')
    data={
        'cname': '',
        'pid': '',
        'keyword': kw,
        'pageIndex': '1',  
        'pageSize': '10',
    }
    response=requests.post(url=url,data=data, headers=headers)
    pageText = response.text
    filename=kw+'.txt'
    with open(filename, 'w', encoding='utf-8') as fp:
        fp.write(pageText)
    print('over')