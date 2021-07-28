import requests
from bs4 import BeautifulSoup
import xlwt

def url_get(page): #URL管理器（管理url的函数）
    url = 'https://movie.douban.com/top250?start='+str(page*25)+'&filter='
    return url

def request_douban(url): #网页下载器（通过url，获取响应text的函数）
    try:
        response = requests.get(url)
        if (response.status_code == 200):
            return response.text
    except requests.RequestException:
        return None

def save_to_excel(soup): #网页解析器（从源代码中提取有效数据的函数）[此处还包含将数据写入excel]
    list = soup.find(class_='grid_view').find_all('li')

    for item in list:
        item_name = item.find(class_='title').string
        item_img = item.find('a').find('img').get('src')
        item_index = item.find(class_='').string
        item_sorce = item.find(class_='rating_num').string
        item_author = item.find('p').text
        if(item.find(class_='inq') != None):
            item_iner = item.find(class_='inq').string

        print('爬取电影：'+item_index+'|'+item_name+'|'+item_sorce+'|'+item_iner)

        global n

        worksheet.write(n, 0, item_name)
        worksheet.write(n, 1, item_img)
        worksheet.write(n, 2, item_index)
        worksheet.write(n, 3, item_sorce)
        worksheet.write(n, 4, item_author)
        worksheet.write(n, 5, item_iner)

        n += 1

def main(page): #调度器（调度url管理器、网页下载器、网页解析器、应用程序的函数）
    url = url_get(page)
    response = request_douban(url)
    soup = BeautifulSoup(response,'lxml')
    save_to_excel(soup)

if __name__ == '__main__': #主函数

    workbook = xlwt.Workbook(encoding='utf-8')
    worksheet = workbook.add_sheet('豆瓣电影TOP250')
    worksheet.write(0, 0, '名字')
    worksheet.write(0, 1, '图片')
    worksheet.write(0, 2, '排名')
    worksheet.write(0, 3, '评分')
    worksheet.write(0, 4, '作者')
    worksheet.write(0, 5, '简介')

    n = 1

    for page in range(0,10):
        main(page)

    workbook.save(u'XXX爬取豆瓣前250电影数据19_05_16.xlsx')

