#encoding=utf-8
import mysql.connector
from mysql.connector import Error

# 连接数据库
def connect_to_database():
    try:
        connection = mysql.connector.connect(
            host='localhost',
            port=3306,
            database='test',
            user='root',
            password=''
        )
        # connection = mysql.connector.connect(
        #     host='mysql.agrisaas.com.cn',
        #     port=3306,
        #     database='rpa_test',
        #     user='root',
        #     password='Ces123456'
        # )
        if connection.is_connected():
            print("Connected to MySQL database")
            return connection
    except Error as e:
        print(f"Error: {e}")
        return None

# 关闭数据库链接
def close_database_connection(connection):
    if connection.is_connected():
        connection.close()
        print("MySQL connection is closed")



# connect_to_database()