from bs4 import BeautifulSoup
import requests
#
url = 'http://c.biancheng.net/linux/chsh.html'
r = requests.get(url)
r.encoding = 'uft-8'
demo = r.text  # 服务器返回响应
soup = BeautifulSoup(demo, "html.parser")
#print(soup)  # 输出响应的html对象
#
def test1():   
    name_box = soup.find('li', attrs={'class': 'active'})
    name_box1 = name_box.text.strip()
    print (name_box)
    print (name_box1)
#
def test2():
    tes2 = soup.find('div', id='nice-arcs',attrs={'class': 'box-bottom'})
    tes3 = tes2.find_all('li')
    for tes4 in tes3:
        tes5 = tes4.get('href')
        print (tes5)
    #
    print (tes3)

#
if __name__ == '__main__':
    test2()

#
