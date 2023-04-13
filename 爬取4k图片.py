import requests
import json
from lxml import etree
import os


# 爬取4k图片

if __name__ == '__main__':
    pages = 1
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36'
    }
    #response.encoding = 'gbk'
    if not os.path.exists('./piclibs'):
        os.mkdir('./piclibs')
    while pages < 171:
        if pages == 1:
            url = 'https://pic.netbian.com/4kmeinv/'
            response = requests.get(url=url, headers=headers)
            page = response.text
            tree = etree.HTML(page)
            List = tree.xpath('//ul[@class="clearfix"]/li')
            for li in List:
                src = 'https://pic.netbian.com/'+li.xpath('./a/img/@src')[0]
                name = li.xpath('./a/img/@alt')[0]+'.jpg'
                # 通用解决处理中文乱码的解决方案
                name = name.encode('iso-8859-1').decode('gbk')
                print(src, name)
                img = requests.get(url=src, headers=headers).content
                img_path = 'piclibs/'+name
                with open(img_path, 'wb')as fp:
                    fp.write(img)
                    print('over')
                pages += 1
        if pages > 1:
            Spages = str(pages)
            url1 = 'https://pic.netbian.com/4kmeinv/'+'index_'+Spages+'.html'
            response = requests.get(url=url1, headers=headers)
            page = response.text
            tree = etree.HTML(page)
            List = tree.xpath('//ul[@class="clearfix"]/li')
            for li in List:
                src = 'https://pic.netbian.com/'+li.xpath('./a/img/@src')[0]
                name = li.xpath('./a/img/@alt')[0]+'.jpg'
                # 通用解决处理中文乱码的解决方案
                name = name.encode('iso-8859-1').decode('gbk')
                print(src, name)
                img = requests.get(url=src, headers=headers).content
                img_path = 'piclibs/'+name
                with open(img_path, 'ab')as fp:
                    fp.write(img)
                    print('over')
                pages += 1