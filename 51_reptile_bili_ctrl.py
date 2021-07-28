from selenium import webdriver
from selenium.common.exceptions import TimeoutException #一条命令在足够的时间内没有完成则会抛出异常
from selenium.webdriver.common.by import By #支持的定位器分类
from selenium.webdriver.support.ui import WebDriverWait  #等待页面加载完成，找到某个条件发生后再继续执行后续代码，如果超过设置时间检测不到则抛出异常
from selenium.webdriver.support import expected_conditions as EC #判断元素是否加载
from bs4 import BeautifulSoup
import xlwt


browser = webdriver.Chrome() #初始化浏览器对象
WAIT = WebDriverWait(browser,10)  #显式等待，等待的时间是固定的，这里为10秒 元素在指定时间内不可见就引发异常TimeoutException
browser.set_window_size(1400,900) #设置浏览器窗口大小


book=xlwt.Workbook(encoding='utf-8',style_compression=0) #创建excel文件，设置utf-8编码，这样就可以在excel中输出中文了
sheet=book.add_sheet('蔡徐坤篮球',cell_overwrite_ok=True) #添加一张工作表 cell_overwrite_ok=True 时可以覆盖原单元格中数据。
sheet.write(0,0,'名称')
sheet.write(0,1,'地址')
sheet.write(0,2,'描述')
sheet.write(0,3,'观看次数')
sheet.write(0,4,'弹幕数')
sheet.write(0,5,'发布时间')
n = 1

def search():
    try:
        print('开始访问b站....')
        browser.get('https://www.bilibili.com/')

        index = WAIT.until(EC.element_to_be_clickable((By.CSS_SELECTOR,'#primary_menu > ul > li.home > a')))
        # 配合WebDriverWait类的until()方法进行灵活判断 进行下一步操作
        # 通过EC进行判断某个元素中是否可见并且是enable的 这样的话叫clickable(可点击)
        # 使用CSS选择器选中页面中的 首页 进行点击 目的为了第一次有个登录弹窗 刷新就没有 那就点击下首页来实现刷新
        index.click() #点击！

        input = WAIT.until(EC.presence_of_element_located((By.CSS_SELECTOR,'#banner_link > div > div > form > input'))) #判断某个元素是否被加到DOM树里，并不代表该元素一定可见(元素可以是隐藏的)
        submit = WAIT.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="banner_link"]/div/div/form/button'))) #判断搜索按钮是否能点击，这里使用Xpath来寻找元素
        input.send_keys('蔡徐坤 篮球') #用send_keys()方法进行搜索输入框中输入内容
        submit.click() #点击搜索！

        print('跳转到新窗口')
        all_h = browser.window_handles #获取所有窗口句柄
        browser.switch_to.window(all_h[1]) #switch_to.window 标签页跳转

        get_source()
        total = WAIT.until(EC.presence_of_element_located((By.CSS_SELECTOR,"#server-search-app > div.contain > div.body-contain > div > div.page-wrap > div > ul > li.page-item.last > button"))) #等待加载后获取所有页数按钮
        return int(total.text) #返回页码数量
    except TimeoutException:
        return search()

def get_source():
    WAIT.until(EC.presence_of_element_located((By.CSS_SELECTOR,'#server-search-app > div.contain > div.body-contain > div > div.result-wrap.clearfix'))) #坚持是否加载完所有搜索结果
    html = browser.page_source #page_source方法可以获取到页面源码
    soup = BeautifulSoup(html,'lxml')
    save_to_excel(soup)

def save_to_excel(soup):
    #遍历所有搜索信息 并保存
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

        n = n + 1

def next_page(page_num):
    try:
        print('获取下一页数据')
        next_btn = WAIT.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#server-search-app > div.contain > div.body-contain > div > div.page-wrap > div > ul > li.page-item.next > button')))
        #等待加载 下一页 按钮
        next_btn.click() #点击下一页！
        WAIT.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR,'#server-search-app > div.contain > div.body-contain > div > div.page-wrap > div > ul > li.page-item.active > button'),str(page_num)))
        #判断某个元素中的text是否包含了预期的字符串
        get_source()

    except TimeoutException:
        browser.refresh() #刷新页面
        return next_page(page_num)

def main():
    try:
        total = search()

        for i in range(2,int(total+1)):
            next_page(i)

    finally:
        browser.close()
        browser.quit()

if __name__ == '__main__':
    main()
    book.save(u'蔡徐坤篮球.xls')