import requests
from bs4 import BeautifulSoup
import os

i = 1

#Url管理器
def url_get(page):
    url = 'https://www.2717.com/ent/meinvtupian/2019/314862_'+str(page)+'.html'
    return url

#网页下载器
def request_img(url):
    try:
        response = requests.get(url)
        if (response.status_code == 200):
            return response.text
    except requests.RequestException:
        return None

#网页解析器
def save_to_files(soup):
    list = soup.find(class_='articleV4Body').find('p')
    img_addrs = list.find('a').find('img').get('src')
    print(img_addrs)
    pic = requests.get(img_addrs)

    global i

    fname = 'img'+str(i)
    with open('./image/'+ fname+ '.jpg','wb') as f:
        f.write(pic.content)
        i += 1
        f.close()

def main(page):
    url = url_get(page)
    html = request_img(url)
    soup = BeautifulSoup(html,'lxml')
    save_to_files(soup)

if not os.path.exists('image'):
    os.makedirs('image')

if __name__ == '__main__':
    for page in range(1,100):
        main(page)