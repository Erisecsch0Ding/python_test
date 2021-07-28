from selenium import webdriver #@导入驱动器
from selenium.common.exceptions import TimeoutException #@导入一条命令在足够的时间内没有完成则抛出异常
from selenium.webdriver.common.by import By #@导入支持的定位器分类
from selenium.webdriver.support.ui import WebDriverWait #@导入等待页面加载完成，找到某个条件发生后则继续执行后续代码，否则超过设置时间检测不到则抛出异常
from selenium.webdriver.support import expected_conditions as EC #@判断元素是否加载
from bs4 import BeautifulSoup
import xlwt

browser = webdriver.PhantomJS() #浏览器实例化
WAIT = WebDriverWait(browser,10)
browser.set_window_size(1400,900)

book = xlwt.Workbook(encoding='utf-8',style_compression=0)
sheet = book.add_sheet('E-CUP',cell_overwrite_ok=True)
sheet.write(0,0,'名称')
sheet.write(0,1,'地址')
sheet.write(0,2,'描述')
sheet.write(0,3,'观看次数')
sheet.write(0,4,'弹幕数量')
sheet.write(0,5,'发布时间')
n = 1

def search():
    try:
        print('开始访问网站')
        browser.get('http://www.bilibili.com')

        index = WAIT.until(EC.element_to_be_clickable((By.CSS_SELECTOR,'#primary_menu > ul > li.home > a')))
        index.click()

        input = WAIT.until(EC.presence_of_element_located((By.CSS_SELECTOR,'#banner_link > div > div > form > input')))
        input.send_keys('E-CUP')
        submit = WAIT.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="banner_link"]/div/div/form/button')))
        submit.click()

        handles = browser.window_handles
        for handle in handles:
            if handle != browser.current_window_handle:
                print('跳转新页面')
                browser.close() ##关闭第一个页面
                browser.switch_to.window(handle)  ##跳转第二个页面

        ######第二种跳转新页面的方式######
        #print('跳转新页面')
        #all_h = browser.window_handles
        #browser.switch_to.window(all_h[1])

        get_source()
        total = WAIT.until(EC.presence_of_element_located((By.CSS_SELECTOR,'#server-search-app > div.contain > div.body-contain > div > div.page-wrap > div > ul > li.page-item.last')))
        return int(total.text)
    except TimeoutException:
        return search()

def get_source():
    WAIT.until(EC.presence_of_element_located((By.CSS_SELECTOR,'#server-search-app > div.contain > div.body-contain > div > div.result-wrap.clearfix')))
    html = browser.page_source
    soup = BeautifulSoup(html,'lxml')
    save_to_excel(soup)

def save_to_excel(soup):
    list = soup.find(class_='all-contain').find_all(class_='info')
    for item in list:
        item_title = item.find('a').get('title')
        item_link = item.find('a').get('href')
        item_dec = item.find(class_='des hide').text
        item_view = item.find(class_='so-icon watch-num').text
        item_biubiu = item.find(class_='so-icon hide').text
        item_date = item.find(class_='so-icon time').text

        print('爬取：' + item_title)

        global n
        sheet.write(n, 0, item_title)
        sheet.write(n, 1, item_link)
        sheet.write(n, 2, item_dec)
        sheet.write(n, 3, item_view)
        sheet.write(n, 4, item_biubiu)
        sheet.write(n, 5, item_date)
        n += 1

def next_page(page_num):
    try:
        print('获取下一页信息')
        next_button = WAIT.until(EC.element_to_be_clickable((By.CSS_SELECTOR,'#server-search-app > div.contain > div.body-contain > div > div.page-wrap > div > ul >li.page-item.next > button')))
        next_button.click()
        WAIT.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR,'#server-search-app > div.contain > div.body-contain > div > div.page-wrap > div > ul > li.page-item.active > button'),str(page_num)))
        get_source()
    except TimeoutException:
        browser.refresh()
        return next_page(page_num)

def main():
    try:
        total = search()
        for i in range(2,(total+1)):
            next_page(i)
    finally:
        browser.close()
        browser.quit()

if __name__ == '__main__':
    main()
    book.save(u'E-CUP.xls')
