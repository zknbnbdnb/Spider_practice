import requests
from lxml import etree
import random
from multiprocessing.dummy import Pool
if __name__ == '__main__':
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36'
    }
    url = 'https://www.pearvideo.com/category_5'
    page_text = requests.get(url=url, headers=headers).text
    tree = etree.HTML(page_text)
    lis = tree.xpath('//ul[@id="listvideoListUl"]/li')
    v_list = []
    for li in lis:
        herf = li.xpath('./div/a/@href')[0]
        name = li.xpath(
            './div/a//div[@class="vervideo-title"]/text()')[0]+'.mp4'
        referer = 'https://www.pearvideo.com/'+herf
        contid = herf.split('_')[-1]
        param = {
            'contid': contid,
            'mrd': random.random(),
        }
        O_headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36',
            'Referer': referer,
        }
        new_url = 'https://www.pearvideo.com/videoStatus.jsp'
        get = requests.get(url=new_url, headers=O_headers, params=param).json()
        dic_url=None
        for dic in get:
            head_url = get["videoInfo"]["videos"]["srcUrl"].rsplit('/',1)[0]+'/cont-'
            ass_url='-'+get["videoInfo"]["videos"]["srcUrl"].split('-',1)[-1]
            real_url=head_url+contid+ass_url
            dic_url=real_url
        dic={
            'name': name,
            'url':dic_url,
        }
        v_list.append(dic)
        def down_url(dic):
            with open(dic['name'],'wb')as fp:
                videos=requests.get(url=dic['url'],headers=headers).content
                fp.write(videos)
                print('over')
        pool=Pool(4)
        pool.map(down_url,v_list)
        pool.close()
        pool.join()
        
        
