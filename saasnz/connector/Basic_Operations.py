import time
from datetime import datetime, timedelta
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from robot.libraries.BuiltIn import BuiltIn
import logging
from selenium import webdriver
import json
from selenium.webdriver.common.by import By
import database_operate
#


# driver = webdriver.Chrome()
# driver.implicitly_wait(10)
# driver.get('http://test.nz.agrisaas.com.cn/intelligent-agriculture/1.0.0/index/#/login')
# driver.maximize_window()
#
# driver.find_element('xpath', '//*[@id="app"]/div[1]/div/div/div[3]/form/div[1]/div/div/div/div/input').send_keys(
#     '17300000000')
# driver.find_element('xpath', '//*[@id="app"]/div[1]/div/div/div[3]/form/div[2]/div/div/div/div/input').send_keys(
#     '000000')
# driver.find_element('xpath', '/html/body/div[1]/div[1]/div/div/div[3]/div[1]/button').click()
# driver.find_element('xpath', '//*[@id="app"]/div[1]/div/div/div[7]/div/div[2]/div[2]/button/span').click()
#



#新增商品
def add_product(product_name):
    seleniumlib = BuiltIn().get_library_instance('SeleniumLibrary')
    driver = seleniumlib.driver
    driver.find_element('xpath','//*[@id="app"]/div[1]/div[5]/a[3]/i').click() #商品登记
    #先查找商品，如果已存在先删除商品，否则无法添加。
    try:
        driver.find_element('xpath','//*[@id="app"]/div[2]/div/div[2]/div[2]/div/div[1]/div/input').send_keys(product_name)
        driver.find_element('xpath','//*[@id="app"]/div[2]/div/div[2]/div[2]/div/div[2]/button/span').click()
        driver.find_element('xpath','//*[@id="app"]/div[2]/div/div[3]/div[2]/table/tr/td[12]/button[3]/span').click()
        driver.find_element('xpath','/html/body/div[3]/div/div[3]/button[2]/span').click()
    except:
        pass
    time.sleep(2)
    driver.find_element('xpath','/html/body/div[1]/div[2]/div/div[4]/div/a/button/span').click()#农资库添加
    driver.find_element('xpath','//*[@id="app"]/div[2]/div/div[2]/div[1]/div/input').send_keys(product_name)#输入商品名称
    driver.find_element('xpath','/html/body/div[1]/div[2]/div/div[2]/button[2]/span').click()#搜索
    driver.find_element('xpath','//*[@id="app"]/div[2]/div/div[4]/div[2]/table/tr[1]/td[9]/button/span').click()#登记path
    driver.find_element('xpath','//*[@id="app"]/div[2]/div/div[2]/form/div[5]/div/div/input').send_keys('10')#输入价格

    # 输入规格
    driver.find_element('xpath', '//*[@id="app"]/div[2]/div/div[2]/form/div[12]/div/div[1]/div/input').send_keys('2')
    driver.find_element('xpath','//*[@id="app"]/div[2]/div/div[2]/form/div[12]/div/div[3]/div/div/div/div[1]/input').click()
    # kg=WebDriverWait(driver, 10).until(EC.presence_of_element_located(('xpath','/html/body/div[3]/div/div[1]/ul/li[1]')))
    # kg.click()
    time.sleep(2)
    driver.find_element('xpath','/html/body/div[3]/div/div[1]/ul/li[1]').click()
    driver.find_element('xpath', '//*[@id="app"]/div[2]/div/div[2]/form/div[12]/div/div[5]/div/div/div/div[1]/input').click()
    # dai=WebDriverWait(driver,10).until(EC.presence_of_element_located(('xpath','/html/body/div[4]/div/div[1]/ul/li[1]/span')))
    # dai.click()
    time.sleep(2)
    driver.find_element('xpath','/html/body/div[4]/div/div[1]/ul/li[1]').click()
    driver.execute_script('''var button = document.querySelector('.el-icon-save');    if (button) {  
        button.click();  }''')  # 选择日期
    # driver.find_element('xpath', '//*[@id="app"]/div[2]/div/div[3]/button[2]/span').click()#确定登记

    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(('xpath', '/html/body/div[5]/div/div[3]/button[2]/span'))).click()#二次确认




#入库
def product_storage():
    seleniumlib = BuiltIn().get_library_instance('SeleniumLibrary')
    driver = seleniumlib.driver
    driver.find_element('xpath', '//*[@id="app"]/div[1]/div[5]/a[4]/i').click()  # 库存管理
    driver.find_element('xpath','//*[@id="app"]/div[2]/div/div[2]/div[1]/div[1]/div[1]/input').click()#点击选择供应商
    time.sleep(2)
    driver.find_element('xpath',"//div/ul/li/span[contains(text(), '贵阳中精科技有限公司')]").click()
    # driver.execute_script("document.elementFromPoint('10','30').click();") #点击空白区域
    driver.find_element('xpath', '//*[@id="app"]/div[2]/div/div[2]/div[1]/button[1]/span').click()  # 添加商品
    time.sleep(2)
    driver.find_element('xpath', '//*[@id="0"]').click()  # 点击商品
    driver.find_element('xpath', '//*[@id="app"]/div[2]/div/div[3]/div[2]/form/div[4]/div/div/input').click()#点击日期选择框
    time.sleep(3)
    driver.execute_script('''var button = document.querySelector('.available');    if (button) {  
    button.click();  }''') #选择日期
    time.sleep(2)
    driver.find_element('xpath',
                        '//*[@id="app"]/div[2]/div/div[3]/div[2]/form/div[5]/div[1]/div/div/div[1]/input').clear()
    driver.find_element('xpath','//*[@id="app"]/div[2]/div/div[3]/div[2]/form/div[5]/div[1]/div/div/div[1]/input').send_keys(2)#输入保质期
    time.sleep(1)
    driver.find_element('xpath',
                        '//*[@id="app"]/div[2]/div/div[3]/div[2]/form/div[6]/div/div[1]/input').clear()
    driver.find_element('xpath',
                        '//*[@id="app"]/div[2]/div/div[3]/div[2]/form/div[6]/div/div[1]/input').send_keys(5)#输入单价
    time.sleep(1)
    driver.find_element('xpath', '/html/body/div[1]/div[2]/div/div[3]/div[2]/form/div[7]/div/div[1]/input').send_keys(
         '1')  # 输入数量
    time.sleep(2)
    driver.find_element('xpath', '//*[@id="app"]/div[2]/div/div[3]/div[2]/div/button[2]/span').click()  # 点击添加
    driver.execute_script("document.elementFromPoint('1','3').click();") #点击空白区域
    time.sleep(3)
    driver.find_element('xpath', '//*[@id="app"]/div[2]/div/div[2]/div[2]/div/button').click()  # 确认入库






#销售出库
def sale():
    seleniumlib = BuiltIn().get_library_instance('SeleniumLibrary')
    driver = seleniumlib.driver
    driver.find_element('xpath','//*[@id="app"]/div[1]/div[5]/a[1]/i').click()
    driver.find_element('xpath','//*[@id="cashRegister"]/div[1]/div[2]/div[1]/div/input').send_keys('草铵膦')#搜索框输入
    driver.find_element('xpath', '//*[@id="cashRegister"]/div[1]/div[2]/div[1]/button/span').click()#点击搜索
    driver.find_element('xpath', '//*[@id="cashRegister"]/div[1]/div[2]/div[2]/div').click()#选择商品
    driver.find_element('xpath', '//*[@id="cashRegister"]/div[1]/div[3]/div[2]/div/div/span').click()#结账
    driver.find_element('xpath', '//*[@id="payForm"]/div/div[2]/div[2]/form/div/div[2]/div[3]/div/div[1]/input').send_keys('张三')
    driver.find_element('xpath', '//*[@id="payForm"]/div/div[2]/div[2]/form/div/div[2]/div[4]/div/div[1]/input').send_keys('13300000000')
    driver.find_element('xpath', '//*[@id="payForm"]/div/div[2]/div[3]/div[2]/div[2]').click()#确定
    driver.find_element('xpath','/html/body/div[3]/div/div[3]/button[2]').click()#二次确认
    driver.find_element('xpath','/html/body/div[3]/div/div[3]/button[1]/span').click()



# 获取我的库存数据
def get_inventory():
    seleniumlib = BuiltIn().get_library_instance('SeleniumLibrary')
    driver = seleniumlib.driver
    driver.find_element('xpath', '//*[@id="app"]/div[1]/div[5]/a[4]/i').click()  # 库存管理
    driver.find_element('xpath','//*[@id="app"]/div[2]/div/a[2]/div').click()#我的库存
    time.sleep(5)
    rows_data_text = driver.execute_script("""
        const rows_body = document.querySelectorAll('.page-loadmore-list.el-table.el-table--border tr');
        const rows = Array.from(rows_body, row => {
            return Array.from(row.children, cell => cell.innerText);
        });
        return rows;
    """)
    #
    # gather_data1 = json.dumps(rows_data_text, ensure_ascii=False).replace('\xa0\xa0', '')
    # gather_data=list(gather_data1)
    database_operate.insert_gather(rows_data_text)





def anhui():
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    driver.get('https://anhui.project.agrisaas.com.cn/new-agriculture/#/login')
    driver.maximize_window()

    driver.find_element('xpath', '//*[@id="apply"]/div/div[2]/form/div[1]/div/div/input').send_keys(
        '20240613')
    driver.find_element('xpath', '//*[@id="apply"]/div/div[2]/form/div[2]/div/div/input').send_keys(
        'Aa123456')
    driver.find_element('xpath', '//*[@id="apply"]/div/div[4]/button').click()
    driver.find_element('xpath', '//*[@id="app"]/div/div[5]/div/div[3]/span/button/span').click()
    driver.find_element('xpath','//*[@id="app"]/div/div[6]/div/div[2]/div/div[2]/div[2]/div[4]/div').click()
    driver.find_element('xpath','//*[@id="app"]/div/div[1]/div[6]/div/div[3]/span/button/span').click()
    driver.find_element('xpath','//*[@id="app"]/div/div[1]/div[2]/div[4]/span').click()
    time.sleep(5)
    rows_data_text = driver.execute_script("""
        const rows_body = document.querySelectorAll('table.el-table__body tbody tr');
        const rows = Array.from(rows_body, row => {
            return Array.from(row.children, cell => cell.innerText);
        });
        return rows;
    """)

    print (rows_data_text)

    gather_data = json.dumps(rows_data_text, ensure_ascii=False).replace('\xa0\xa0', '')
    print (gather_data)

# add_product('苄嘧磺隆')
# product_storage()
# sale()
# get_inventory()
# #
# anhui()

