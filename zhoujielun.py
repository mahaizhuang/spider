import requests
import time
from requests.api import head
from tqdm import tqdm
from bs4 import BeautifulSoup
import re
import os
#
if __name__ == '__main__':
    target = 'http://www.kehuan.net.cn'
    server = 'http://www.kehuan.net.cn/book/santi.html'
    ser1 = requests.get(url=server)
    ser1.encoding = 'uft-8'
    html1 = ser1.text
    bs1 = BeautifulSoup(html1,'lxml')
    texts1 = bs1.find('div',id='main')
    texts1 = bs1.find_all('a')
    print (texts1)
    for tex in tqdm(texts1):
        url1 = tex.get('href')
        if "santi" in url1:
            target1 = target + url1
            print(target1)
            req = requests.get(url = target1)
            req.encoding = 'utf-8'
            html = req.text
            bs = BeautifulSoup(html, 'lxml')
            texts = bs.find('div', id='container')
            name_box = texts.find('div', attrs={'class': 'text'})
            name_box = name_box.text.strip()
            #
            title1 = tex.string
            path1 = os.path.abspath(os.path.dirname(__file__))
            path2 = path1 + "\三体"
            print (path2)
            if not os.path.exists(path2):
                   os.mkdir(path2)
            path3 = path2 + "\\" + " %s.txt"
            with open(path3 %(title1),"w+",encoding='UTF-8') as f:
                 f.write(name_box)
                 f.close()
            time.sleep(1)
#########################################################################################################################