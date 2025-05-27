import mysql.connector
import os
from dotenv import load_dotenv

# 加载 .env 文件中的环境变量
load_dotenv()

# 从环境变量获取数据库配置
MYSQL_HOST = os.getenv("MYSQL_HOST")
MYSQL_PORT = int(os.getenv("MYSQL_PORT"))
MYSQL_USER = os.getenv("MYSQL_USER")
MYSQL_PASSWORD = os.getenv("MYSQL_PASSWORD")
MYSQL_DATABASE = os.getenv("MYSQL_DATABASE")

# 数据库连接
try:
    connection = mysql.connector.connect(
        host=MYSQL_HOST,
        port=MYSQL_PORT,
        user=MYSQL_USER,
        password=MYSQL_PASSWORD,
        database=MYSQL_DATABASE
    )
    cursor = connection.cursor()

    # 创建 test 表（如果不存在）
    create_table_query = """
    CREATE TABLE IF NOT EXISTS test (
        id INT PRIMARY KEY,
        username VARCHAR(50),
        gender VARCHAR(10),
        password VARCHAR(32),
        email VARCHAR(100),
        phone VARCHAR(15),
        address VARCHAR(100),
        avatar VARCHAR(100)
    );
    """
    cursor.execute(create_table_query)

    # 插入数据
    insert_query = """
    INSERT INTO test (id, username, gender, password, email, phone, address, avatar)
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
    """
    data = [
        (101, 'admin', '女', '21232f297a57a5a743894a0e4a801fc3', '111111@qq.com', '13260161111', '昌平', 'upload/default.jpg'),
        (102, 'admin1', '男', '21232f297a57a5a743894a0e4a801fc3', '512111559@qq.com', '13260166090', '北京', 'upload/default.jpg'),
        (103, 'admin2', '男', '21232f297a57a5a743894a0e4a801fc3', '512111559@qq.com', '13260166090', '北京', 'upload/default.jpg'),
        (104, 'admin3', '男', '21232f297a57a5a743894a0e4a801fc3', '123456@qq.com', '13666666666', '宏福苑', 'upload/default.jpg'),
        (888, 'test', '女', 'test1', '111111@qq.com', '13260161111', '昌平', 'upload/default.jpg')
    ]
    cursor.executemany(insert_query, data)

    # 提交事务
    connection.commit()
    print("数据插入成功！")

except mysql.connector.Error as err:
    print(f"数据库错误: {err}")
finally:
    if cursor:
        cursor.close()
    if connection:
        connection.close()