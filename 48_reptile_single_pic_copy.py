import requests,os
from bs4 import BeautifulSoup

def request_img(url):
    try:
        response = requests.get(url)
        if (response.status_code == 200):
            return response.text
    except requests.RequestException:
        return None

def save_to_files(soup):
    list = soup.find(class_='arcmain').find('p')
    img_addrs = list.find('a').find('img').get('src')
    print(img_addrs)
    pic = requests.get(img_addrs)

    with open('./image/a.jpg', 'wb') as f:
        f.write(pic.content)
        f.close()

if not os.path.exists('image'):
    os.makedirs('image')

# url = 'https://www.2717.com/ent/meinvtupian/2019/315005.html'
url = 'https://m.7160.com/meinv/68515/'
html = request_img(url)
soup = BeautifulSoup(html,'lxml')
save_to_files(soup)

