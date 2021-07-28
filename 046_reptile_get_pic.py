import requests
from bs4 import BeautifulSoup
import os

def request_img(url):#网页下载器（通过url，下载源代码，返回源代码的text）
    try:
        response = requests.get(url)
        if (response.status_code == 200):
            return response.text
    except requests.RequestException:
        return None

def save_to_files(soup):#网页解析器（通过soup，解析源代码，提取有效数据，返回相应格式的数据）[此处还包含：根据获取的图片链接下载图片到本地]
    list = soup.find(class_='pli').find_all('li')

    for item in list:
        item_img_addrs = 'http:'+item.find('a').find('img').get('src')
        print(item_img_addrs)
        pic = requests.get(item_img_addrs)

        global i

        fname = 'img'+str(i)
        with open('./image/'+fname+'.jpg','wb') as f:
            f.write(pic.content)
            i += 1
            f.close()

if not os.path.exists('image'):
    os.makedirs('image')
i = 0
url = 'https://www.ivsky.com/tupian/youcaihuatian_v52968/'#url管理器
req = request_img(url)
soup = BeautifulSoup(req,'lxml')
save_to_files(soup)
