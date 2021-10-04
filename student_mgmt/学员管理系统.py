# 定义功能界面的函数
from python_mysql import mysql_connect as mysql

def info_print():
    print('请选择功能*******************************')
    print('1、添加学员')
    print('2、删除学员')
    print('3、修改学员')
    print('4、查询学员')
    print('5、显示所有学员')
    print('6、退出系统')
    print('*'*40)

# 添加学员功能
# 等待存储所有学员的信息
# info = []
def add_info():
    """添加学员函数"""
    # 1、用户输入：学号、姓名、手机号
    new_id = input('请输入学员学号：')
    new_name = input('请输入学员姓名：')
    new_tel = input('请输入学员电话：')
    myresult = mysql.search_mysql()
    for i in myresult:
        if new_name == i[1]:
            print('该用户已经存在！')
            return #整个def结束
    mysql.insert_into_mysql("'" + new_id + "'", "'" + new_name + "'", "'" + new_tel + "'")
    print(f'新增学员信息为:{new_name}')
    # 2、判断是否添加这个学员：如果学院性能已经存在报错提示，如果姓名不存在则添加数据
    # global info
    # for i in info:
    #     if new_name == i['name']:
    #         print('该用户已经存在！')
    #         return #整个def结束
    # info_dict = {}
    # info_dict['id'] = new_id
    # info_dict['name'] = new_name
    # info_dict['tel'] = new_tel
    # print(f'新增学员信息为:{info_dict}')
    # info.append(info_dict)
    # print(f'学员信息列表为：{info}')

# 删除学员功能
def del_info():
    del_name = input('请输入需要删除的学员姓名：')
    myresult = mysql.search_mysql()
    for i in myresult:
        if del_name == i[1]:
            mysql.del_mysql("'" + del_name + "'")
            print(f'学员{del_name}删除成功')
            break #整个循环结束
    else:
        print('用户输入的学员姓名不存在')
    myresult2 = mysql.search_mysql()
    print(f'学员名单{myresult2}')
    # global info
    # for i in info:
    #     if i['name'] == del_name:
    #         info.remove(i)
    #         print(f'学员{del_name}删除成功')
    #         #系统不允许重名，删除成功后退出程序
    #         break #整个循环结束
    # else:
    #     print('用户输入的学员姓名不存在')
    # print(f'学员名单{info}')

# 修改学员
def modify_info():
    modify_name = input('请输入需要修改的学员姓名：')
    myresult = mysql.search_mysql()
    for i in myresult:
        if modify_name == i[1]:
            modify_tel = input('请输入新的tel：')
            mysql.modify_mysql("'"+modify_tel+"'", "'"+modify_name+"'")
            print(f'学员{modify_name}电话修改成功')
            break  # 整个循环结束
    else:
        print('用户输入的学员姓名不存在')
    myresult2 = mysql.search_mysql()
    print(f'学员名单{myresult2}')

    # global info
    # for i in info:
    #     if i['name'] == modify_name:
    #         modify_tel = input('请输入新的tel：')
    #         i['tel'] = modify_tel
    #         break #整个循环结束
    # else:
    #     print('用户输入的学员姓名不存在')
    # print(f'学员名单{info}')

# 查询学员信息
def search_info():
    search_name = input('请输入你的要搜索的学员名字：')
    myresult = mysql.search_mysql()
    for i in myresult:
        if search_name == i[1]:
            print(f'搜索结果如下：\n学员姓名：{i[1]}\n学员学号：{i[0]}\n学员电话：{i[2]}')
            break
    else:
        print('学员不存在')
    # for i in info:
    #     if search_name == i['name']:
    #         print(f'搜索结果如下：\n学员姓名：{i["name"]}\n学员学号：{i["id"]}\n学员电话：{i["tel"]}')
    #         break
    # else:
    #     print('学员不存在')

# 显示所有学员
def all_info():
    print('所有学员信息为：')
    print('学员学号\t学员姓名\t学员电话')
    myresult = mysql.search_mysql()
    for i in myresult:
        print(f'{i[0]}\t{i[1]}\t{i[2]}')
    # for i in info:
    #     print(f'{i["id"]}\t{i["name"]}\t{i["tel"]}')

# 系统功能需要循环使用，直到用户输入6，才退出系统
while True:
    # 1、显示功能界面
    info_print()
    # 2、用户输入功能序号
    user_num = int(input('请输入功能序号：'))
    # 3、按照用户输入的功能序号执行不同的功能（函数）
    # 如果用户输入1，执行添加；如果用户输入2，执行删除...
    if user_num == 1:
        # print('添加')
        add_info()
    elif user_num == 2:
        # print('删除')
        del_info()
    elif user_num == 3:
        # print('修改')
        modify_info()
    elif user_num == 4:
        # print('查询')
        search_info()
    elif user_num == 5:
        # print('显示所有')
        all_info()
    elif user_num == 6:
        exit_flag = input('确定要退出吗？yes or no : ')
        if exit_flag == 'yes':
            print('退出系统')
            break # 退出while true循环
    else:
        print('输入的功能序号有误')

