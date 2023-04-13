import requests
import json
from lxml import etree
import os

# 生产许可证

if __name__ == '__main__':
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36'
    }
    url = 'http://scxk.nmpa.gov.cn:81/xk/itownet/portalAction.do?method=getXkzsList'
    id_list = []

    for page in range(1, 21):
        page = str(page)
        data = {
            'on': 'true',
            'page': page,
            'ageSize': '15',
            'productName': '',
            'conditionType': '1',
            'applysn': '',
        }
        Id = requests.post(url=url, data=data, headers=headers).json()
        
        for dic in Id['list']:
            id_list.append(dic['ID'])

    info_url = 'http://scxk.nmpa.gov.cn:81/xk/itownet/portalAction.do?method=getXkzsById'
    all_info = []
    for ID in id_list:
        data = {
            'id': ID
        }
        response = requests.post(url=info_url, data=data, headers=headers)
        ai=response.json()
        all_info.append(ai)
    fp = open('./all_info.json', 'w', encoding='utf-8')
    json.dump(all_info, fp=fp, ensure_ascii=False, indent=4)
    print('over')