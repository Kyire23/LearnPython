from product import Product
from stock import Stock


host = 'localhost'
user = 'root'
password = '123456'
db_name = 'stock'

s = Stock(host, user, password, db_name)  # 定义类对象


def insert_data():
    is_quit = 'y'  # 设置变量is_quit，用于判断是否继续输入数据
    while(is_quit == 'y'):
        id = input('\n请输入产品ID:')
        name = input('请输入产品名称:')
        number = int(input('请输入产品数量:'))
        price = int(input('请输入产品价格:'))
        p = Product(id, name, number, price)
        s.add(p)
        is_quit = input('您要继续输入吗？y/n:')
        while(is_quit != 'y' and is_quit != 'n'):
            is_quit = input('只能输入 y/n ，请重新输入:')
    s.list_all()


def delete_data():
    id = input('\n请输入要取出的产品ID:')
    name = input('请输入要取出的产品名称:')
    number = int(input('请输入要取出的产品数量:'))
    price = int(input('请输入要取出的产品价格:'))
    p = Product(id, name, number, price)
    s.dele(p)


def select_data():
    id = input('\n请输入要查询的产品ID:')
    if id.strip() != '':  # strip()是去掉前后空格
        s.list(id.strip())
    else:
        s.list_all()


def menu():
    title = '库存管理系统'
    choose_menu='1 增加产品    2 取出产品    3 查询产品    4 退出系统'
    print('*'*60)
    print(str.format('{0:^56}\n', title))
    print(str.format('{0:^44}', choose_menu))
    print('*'*60)


def start():
    menu()
    choice = int(input('请输入:'))
    while(choice != 4):
        if(choice == 1):
            insert_data()
        elif(choice == 2):
            delete_data()
        elif(choice == 3):
            select_data()
        else:
            choice = int(input('只能输入 1,2,3,4 ，请重新输入:'))
            continue
        menu()
        choice = int(input('请输入:'))
        while(choice != 1 and choice != 2 and choice != 3 and choice != 4):
            choice = int(input('只能输入 1,2,3,4 ，请重新输入:'))

start()
