import pymysql.cursors

# 连接MySQL数据库
connection = pymysql.connect(host='127.0.0.1', port=3306, user='Carl', password='a2020', db='icme', charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)

# 通过cursor创建游标
cursor = connection.cursor()

# 执行数据查询
sql = "SELECT `Info`, `materials` FROM `materials_info` WHERE `Name`='w'"
cursor.execute(sql)

#查询数据库单条数据
result = cursor.fetchone()
print(result)

# 关闭数据连接
connection.close()
