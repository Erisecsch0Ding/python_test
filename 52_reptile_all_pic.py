import concurrent
import os
from concurrent.futures import ThreadPoolExecutor

import requests
from bs4 import BeautifulSoup

###headers
use_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36"
headers = {'User-Agent': use_agent}

def header(referer):
    headers = {
        'Host': 'i.meizitu.net',
        'Pragma': 'no-cache',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.8,en;q=0.6',
        'Cache-Control': 'no-cache',
        'Connection': 'keep-alive',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36',
        'Accept': 'image/webp,image/apng,image/*,*/*;q=0.8',
        'Referer': '{}'.format(referer),
    }
    return headers

###页面下载器
def request_page(url):
    try:
        response = requests.get(url,headers=headers)
        if response.status_code == 200:
            return response.text
    except requests.RequestException:
        return None

###url管理器（通过基础页面，获取响应文，解析后再抓取url），需传入https://www.mzitu.com/page/1或2、3、4...,返回名为urls的list
###【page_num-->base_url-->base_url_list】
###比如page_num是3（下载3页），遍历每页的组图（每个24个组图），抓取每个组图的页面储存到urls这个list里
def get_page_urls(page_num):
    try:
        urls = []  #创建一个list，用来储存所有的组图url（比如下载3页，每页24个组图，那么list就会储存72个url）
        for i in range(1,int(page_num)+1):
            #print('爬取页数{}'.format(i))
            base_url = 'https://www.mzitu.com/page/{}'.format(i)
            html = request_page(base_url)
            soup = BeautifulSoup(html, 'lxml')
            list = soup.find(class_='postlist').find_all('li')
            for item in list:
                url = item.find('span').find('a').get('href')
                print(url)
                urls.append(url)
        return urls
    except TimeoutError as e:
        print('TimeoutError:',e)

###图片下载写入器（通过图片链接，下载并写入图片到本地），需传入图片名称与图片链接，返回
###【title-->新建文件夹-(遍历)->新建图片（title+j)】
###【image_list(每个人对应的组图链接list)-(遍历)->
def download_pic(title,image_list):
    os.mkdir(title)    #创建title的文件夹
    j = 1
    for item in image_list:
        filename = '%s%s.jpg'%(title,str(j))   #创建title+j的图片文件
        print('下载...%s : NO.%s'%(title,str(j)))
        img = requests.get(item, headers=header(item)).content
        with open('./%s/%s'%(title,filename),'wb') as f:
            f.write(img)
        f.close()
        j += 1

###图片链接下载器（抓取每个人的图片总数、组图标题，遍历每人的子页面（url+i)->抓源代码->解析子页面图片链接->得到链接列表），调用download
###【url-(下载解析)->total、title-(遍历子页面+下载解析)->src(图片链接)-->image_list(每个人对应的组图链接list)】
def download(url):
    html = request_page(url)    #下载
    soup = BeautifulSoup(html,'lxml')   #变汤
    total = soup.find(class_='pagenavi').find_all('a')[-2].find('span').string  #解析图片总数
    title = soup.find('h2').string      #解析组图标题
    image_list = []
    for i in range(int(total)):
        html = request_page(url+'/%s'%(i+1))    #（url+i）遍历子页面，下载子页面源代码
        soup = BeautifulSoup(html,'lxml')   #变汤
        img_url = soup.find('img').get('src')   #解析图片链接
        # print(img_url)
        image_list.append(img_url)
    download_pic(title,image_list)   #图片下载写入器（通过图片链接，下载并写入图片到本地），需传入图片名称与图片链接

if __name__ == '__main__':
    page_num = input('请输入你要下载几页（每页有24个组图）：')
    # 获取每一页的链接和名称
    list_page_urls = get_page_urls(page_num)
    print('要下载{}个组图,耐心等待...'.format(len(list_page_urls)))
    for url in list_page_urls:
        download(url)