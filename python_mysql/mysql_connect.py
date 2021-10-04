import pymysql

def insert_into_mysql(stu_id,stu_name,stu_tel):
    # 1. 连接数据库，
    mydb = pymysql.connect(
        host="localhost",  # 数据库主机地址
        user="root",  # 数据库用户名
        password="root",  # 数据库密码
        db="student_mgmt",
        charset="utf8mb4"
    )
    # print(mydb)
    # 2. 创建游标对象，
    cur = mydb.cursor()
    # 3.插入数据
    try:
        insert_sqli = f'insert into stu_info (id,name,tel) VALUES({stu_id},{stu_name},{stu_tel})'
        cur.execute(insert_sqli)
    except Exception as e:
        print("插入数据失败:", e)
    else:
        # 如果是插入数据， 一定要提交数据， 不然数据库中找不到要插入的数据;
        mydb.commit()
        print("插入数据成功;")
        mydb.close()

# 查询所有
def search_mysql():
    # 1. 连接数据库，
    mydb = pymysql.connect(
        host="localhost",  # 数据库主机地址
        user="root",  # 数据库用户名
        password="root",  # 数据库密码
        db="student_mgmt",
        charset="utf8mb4"
    )
    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM stu_info")
    myresult = mycursor.fetchall()  # fetchall() 获取所有记录
    # for x in myresult:
    #     print(x)
    # print("查询数据成功;")
    # print(myresult)
    return myresult
    mydb.close()

# 修改
def modify_mysql(tel,name):
    # 1. 连接数据库，
    mydb = pymysql.connect(
        host="localhost",  # 数据库主机地址
        user="root",  # 数据库用户名
        password="root",  # 数据库密码
        db="student_mgmt",
        charset="utf8mb4"
    )
    mycursor = mydb.cursor()
    sql = f"UPDATE stu_info SET tel = {tel} WHERE name = {name}"
    mycursor.execute(sql)
    mydb.commit()
    print(mycursor.rowcount, " 条记录被修改")

# 删除
def del_mysql(name):
    # 1. 连接数据库，
    mydb = pymysql.connect(
        host="localhost",  # 数据库主机地址
        user="root",  # 数据库用户名
        password="root",  # 数据库密码
        db="student_mgmt",
        charset="utf8mb4"
    )
    mycursor = mydb.cursor()
    sql = f"DELETE FROM stu_info WHERE name = {name}"
    mycursor.execute(sql)
    mydb.commit()
    print(mycursor.rowcount, " 条记录被删除")


