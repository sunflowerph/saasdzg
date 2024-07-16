#encoding=utf-8
import logging as logger
from datetime import datetime

from mysql.connector import Error

import mysql_database as mysql


# 查询
def search_gather():
    # 连接到数据库
    db_connection = mysql.connect_to_database()
    if db_connection is None:
        return
    try:
        cursor = db_connection.cursor()
        cursor.execute("SELECT * FROM test_rpa_gather")
        records = cursor.fetchall()

        for row in records:
            logger.info(f"Data from DB: {row}")
    except Error as e:
        logger.info(f"Error while interacting with database: {e}")
    finally:
        mysql.close_database_connection(db_connection)


# 修改
def update_gather():
    db_connection = mysql.connect_to_database()
    if db_connection is None:
        return
    try:
        cursor = db_connection.cursor()
        cursor.execute(
            "UPDATE test_rpa_gather SET gather_results = '{\"status\": 200, \"message\": \"执行成功\", \"time\": \"执行总耗时: 5.362534761428833 秒\",\"data\":\"数据已更新\"}' WHERE id = 1")
        db_connection.commit()
        logger.info("Updated data into database")
    except Error as e:
        logger.info(f"Error while interacting with database: {e}")
    finally:
        mysql.close_database_connection(db_connection)


#新增
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
# if __name__ == "__main__":
#     # search_gather()
#     # insert_gather('1000')
