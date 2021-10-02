# 定义功能界面的函数
def info_print():
    print('请选择功能*******************************')
    print('1、添加学员')
    print('2、删除学员')
    print('3、修改学员')
    print('4、查询学员')
    print('5、显示所有学员')
    print('6、退出系统')
    print('*'*20)

# 1、显示功能界面
info_print()
# 2、用户输入功能序号
user_num = int(input('请输入功能序号：'))
# 3、按照用户输入的功能序号执行不同的功能（函数）
# 如果用户输入1，执行添加；如果用户输入2，执行删除...
if user_num == 1:
    print('添加')
elif user_num == 2:
    print('删除')
elif user_num == 3:
    print('修改')
