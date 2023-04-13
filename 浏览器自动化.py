from selenium import webdriver
from lxml import etree
from time import sleep
from selenium.webdriver import ActionChains
#import requests
'''bro = webdriver.Chrome(executable_path='D:/chromedriver')
bro.get('http://scxk.nmpa.gov.cn:81/xk/')
page_text = bro.page_source
tree = etree.HTML(page_text)
li_list = tree.xpath('//ul[@id="gzlist"]/li')
for li in li_list:
    name = li.xpath('./dl/@title')[0]
    print(name)
sleep(10)
bro.quit()'''

'''bro = webdriver.Chrome(executable_path='D:/chromedriver')
bro.get('https://www.runoob.com/try/try.php?filename=jqueryui-api-droppable')
bro.switch_to.frame('iframeResult')
div = bro.find_element_by_id('draggable')
action = ActionChains(bro)
action.click_and_hold(div)
for i in range(5):
    action.move_by_offset(50, 3).perform()
    sleep(0.1)
    action.release()'''
    
bro = webdriver.Chrome(executable_path='D:/chromedriver')
bro.get('https://qzone.qq.com/')
bro.switch_to.frame('login_frame')
tag= bro.find_element_by_id('switcher_plogin')
tag.click()

u=bro.find_element_by_id('u')
p=bro.find_element_by_id('p')
sleep(1)
u.send_keys('1307403902')
sleep(1)
p.send_keys('zknbnbdnb123.')
btn=bro.find_element_by_id('login_button')
btn.click()

#bro.quit()

