import mysql_database as mysql
from mysql.connector import Error
from selenium import webdriver
import time



gather_results=	[["1", "农药", "PD20140879", "草铵膦", "", "50千克/袋", "93", "91", "1.00", "3.00", "退货 盘点 详情 盘点记录"], ["2", "农药", "PD20095079", "氧乐果", "", "3.00斤/支", "5", "5", "0.00", "1.00", "退货 盘点 详情 盘点记录"], ["3", "农药", "PD20040391", "高效氯氰菊酯", "", "50.00斤/瓶", "1", "0", "1.00", "4.00", "退货 盘点 详情 盘点记录"], ["4", "农药", "PD20211079", "甲维·氯虫苯", "", "20.00克/袋", "253", "158", "18.00", "3.50", "退货 盘点 详情 盘点记录"]]



def insert_gather(gather_results):
    db_connection = mysql.connect_to_database()
    if db_connection is None:
        return
    try:
        for gather_result in gather_results:
            cursor=db_connection.cursor()
            gather_query = (f'insert into table2 values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)')
            gather_param=[]
            for i in range(10):
                gather_param.append(gather_result[i])
            gather_params=tuple(gather_param)
            print(gather_params)
            cursor.execute(gather_query,gather_params)
            db_connection.commit()
    except Error as e:
        print(f"Error while interacting with database: {e}")
    finally:
        mysql.close_database_connection(db_connection)

# insert_gather(gather_results)


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
    # rows_data_text = driver.execute_script("""
    #     const rows_body = document.querySelectorAll('table.el-table__body tbody tr');
    #     const rows = Array.from(rows_body, row => {
    #         return Array.from(row.children, cell => cell.innerText);
    #     });
    #     return rows;
    # """)
    rows_data_text = driver.execute_script("""
        const rows_body = document.querySelectorAll('table.el-table__body tbody tr');
        rows=rows_body.innerText
return rows
    """)

    print (rows_data_text)

    # gather_data = json.dumps(rows_data_text, ensure_ascii=False).replace('\xa0\xa0', '')
    # print (gather_data)


anhui()