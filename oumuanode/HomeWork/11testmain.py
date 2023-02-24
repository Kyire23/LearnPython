"""
@Author = oumuamuanode
@Time : 2022/11/10 14:27
"""
from homeWork11 import product
from homeWork11 import stock

s = stock()


def insert_data():
    is_quit = 'y'
    while is_quit == 'y':
        id = input('请输入产品id:')
        name = input('请输入产品名称:')
        number = int(input('请输入产品数量:'))
        price = int(input('请输入产品价格:'))
        p = product(id, name, number, price)
        s.add(p)
        is_quit = input('你要继续输入吗？y/n:')
        if is_quit == 'n':
            break
        while is_quit != 'y' and is_quit != 'n':
            is_quit = input('只能输入y/n，请重新输入:')
        s.list_all()


def delete_data():
    id = input('请输入产品id:')
    name = input('请输入产品名称:')
    number = int(input('请输入产品数量:'))
    price = int(input('请输入产品价格:'))
    p = product(id, name, number, price)
    s.dele(p)


def select_data():
    id = input('请输入产品id:')
    s.List(id)


print('请选择:1 增加产品; 2 取出产品; 3 查询产品; 4 退出;')
choice = int(input('请输入:'))
while choice != 4:
    if choice == 1:
        insert_data()
    elif choice == 2:
        delete_data()
    elif choice == 3:
        select_data()
    else:
        choice = int(input('只能输入 1,2,3,4 ,请重新输入:'))
        continue
    print('请选择:1 增加产品; 2 取出产品; 3 查询产品; 4 退出;')
    choice = int(input('请输入:'))
    while choice != 1 and choice != 2 and choice != 3 and choice != 4:
        choice = int(input('只能输入 1,2,3,4, 请重新输入:'))
