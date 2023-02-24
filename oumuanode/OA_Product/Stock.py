import pymysql


# 数据库连接
def connect():
    conn = pymysql.connect(host='localhost',
                           port=3306,
                           user='root',
                           password='123456',
                           database='dbtest',  # 选择数据库
                           charset='utf8')
    # 获取操作游标
    cursor = conn.cursor()
    return {"conn": conn, "cursor": cursor}


# 管理员操作，插入商品
def add_goods():
    # 获取操作游标
    connection = connect()
    conn, cursor = connection['conn'], connection['cursor']
    stuID = int(input('请输入要插入的商品编号：'))
    stuName = input('请输入要插入的商品名字：')
    stuPrice = input('请输入要插入的商品价格：')
    add = cursor.execute('insert into fruits (stuID, stuName , stuPrice)\
                   values(%s,%s,%s)', (stuID, stuName, stuPrice))
    if add == 1:  # 利用游标查找数据表，如果数据库中有此表捕获，没有报异常
        conn.commit()  # 把数据传入数据库
        print('插入成功！')
    else:
        print('插入失败！')
    show_commend()  # 返回show_commend()类


# 删除商品记录
def delete_goods():
    # 获取操作游标
    connection = connect()
    conn, cursor = connection['conn'], connection['cursor']
    stuID = int(input('输入想要删除商品的编号：'))
    delete = cursor.execute('delete from fruits where stuID= {}'.format(stuID))
    if delete == 1:  # 利用游标查找数据表，如果数据库中有此表捕获，没有报异常
        conn.commit()  # 把数据传入数据库
        print('删除成功！')
    else:
        print('删除失败！')
    show_commend()  # 返回show_commend()类


# 管理员操作，查询单个商品之按商品编号查询
def g_by_id():
    # 获取操作游标
    connection = connect()
    conn, cursor = connection['conn'], connection['cursor']
    choice_id = int(input('请输入商品编号：'))
    cursor.execute('select * from fruits where stuID=%s', (choice_id))
    fruits = cursor.fetchall()  # 利用游标查找数据表，如果数据库中有此表捕获，没有报异常
    for j in fruits:
        print("==============================================")
        print('---商品编号:{}    商品名称:{}    商品价格:{}---'.format(j[0], j[1], j[2]))
        print('查询成功')
        print("==============================================")
        # 设计继续执行下一步操作代码
        re = input('是否继续查询(yes/no)：')
        if re == 'yes':  # 执行yes返回g_by_name，no返回到操作页面
            g_by_id()
        else:
            show_commend()  # 返回show_commend()类


# 管理员操作，查询单个商品之按商品名称查询（以防商品编号输入错误）
def g_by_name():
    # 获取操作游标
    connection = connect()
    conn, cursor = connection['conn'], connection['cursor']
    choose_name = input('请输入商品名称：')
    cursor.execute('select * from stu where name =%s', (choose_name))
    students = cursor.fetchall()  # 利用游标查找数据表，如果数据库中有此表捕获，没有报异常
    for j in students:
        print("==============================================")
        print('---商品编号:{}    商品名称:{}    商品价格:{}---'.format(j[0], j[1], j[2]))
        print('查询成功')
        print("==============================================")
        re = input('是否继续查询yes/no：')
        if re == 'yes':  # 执行yes返回g_by_name，no返回到操作页面
            g_by_name()
        else:
            show_commend()  # 返回show_commend()类


# 管理员操作，修改商品
def update_goods():
    # 获取操作游标
    connection = connect()
    conn, cursor = connection['conn'], connection['cursor']
    cur = int(input('请输入想要修改的商品编号：'))
    cursor.execute('select * from fruits where stuID = %s', (cur))
    if not cursor.fetchall():  # 利用游标查找数据表，如果数据库中有此表捕获，没有报异常
        print('未查找该商品的编号{}'.format(cur))
        # 设计继续执行下一步操作代码
        mc3 = input('是否重新查询？(yes/no)')
        if mc3 != 'no':  # 执行yes返回g_by_name，no返回到操作页面
            update_goods()
        else:
            show_commend()  # 返回show_commend()类

    else:
        print('==============')
        print('1、修改商品编号')
        print('2、修改商品名称')
        print('3、修改商品价格')
        print('==============')
        mc2 = int(input('请输入对应的操作号：'))
        if mc2 == 1:
            stuID = input('请输入修改后的商品编号：')
            a = cursor.execute('update fruits set stuID = %s where stuID= %s', (stuID, cur))
            if a == 1:  # 利用游标查找数据表，如果数据库中有此表捕获，没有报异常
                conn.commit()  # 把数据传入数据库
                print('修改成功！')
            else:
                print('修改失败！')
        elif mc2 == 2:
            stuName = input('请输入修改后的商品名称：')
            a = cursor.execute('update fruits set stuName = %s where stuID = %s', (stuName, cur))
            if a >= 1:  # 利用游标查找数据表，如果数据库中有此表捕获，没有报异常
                conn.commit()  # 把数据传入数据库
                print('修改成功！')
            else:
                print('修改失败！')
        elif mc2 == 3:
            stuPrice = int(input('请输入修改后的商品价格：'))
            a = cursor.execute('update fruits set stuPrice= %s where stuID = %s', (stuPrice, cur))
            if a >= 1:  # 利用游标查找数据表，如果数据库中有此表捕获，没有报异常
                conn.commit()  # 把数据传入数据库
                print('修改成功！')
            else:
                print('修改失败！')
        else:
            pass  # 占一个空位符
        show_commend()  # 返回show_commend()类


# 管理员操作，查询所有商品信息
def goods_all():
    # 获取操作游标
    connection = connect()
    conn, cursor = connection['conn'], connection['cursor']
    cursor.execute('select * from fruits')
    fruits = cursor.fetchall()  # 利用游标查找数据表，如果数据库中有此表捕获
    print("=============================================")
    print("商品表为：")
    print("=============================================")
    for j in fruits:
        print('---商品编号:{}---商品名称:{}---商品价格:{}---'.format(j[0], j[1], j[2]))
    print("=============================================")
    show_commend()


# 退出管理员商品管理系统
def end_goods():
    print("已提出！")
    exit()


goods_dict1 = {'a': g_by_name, 'b': g_by_id}


# 管理员操作，选择查询单个商品的方法
def show_querycondition():
    cmd = input("请输入操作指令：输入商品名称查询（a） 输入商品编号查询（b)\n")
    if cmd not in goods_dict1:
        print('输入错误！')
    else:
        goods_dict1[cmd]()  # 进入cmd对应的values输出的类中


goods_dict2 = {'a': goods_all, 'b': update_goods, 'c': add_goods, 'd': show_querycondition, 'e': delete_goods,
               'i': end_goods}


# 商场工作人员对商品的增删查改操作
def show_commend():
    cmd = input("请输入操作指令：查询全部商品（a） 修改商品（b)  插入商品（c)  查询单个商品（d)   删除商品（e)   退出（i)\n")
    if cmd not in goods_dict2:
        print('输入错误！')
        Start()
    else:
        goods_dict2[cmd]()  # 进入cmd对应的values输出的类中


def select_sql():
    # 获取操作游标
    connection = connect()
    conn, cursor = connection['conn'], connection['cursor']
    sql = "select * from fruits"
    try:  # 利用游标查找数据表，如果数据库中有此表捕获，没有报异常
        cursor.execute(sql)
        results = cursor.fetchall()
        results = list(results)
        return results
    except Exception as e:  # 捕获异常
        raise e
    finally:
        cursor.close()
        conn.close()


data = select_sql()  # 拿到selct_sql元组对象
goods = []  # 利用该空列表把数据转移出来
# 通过遍历把selct_sql元组对象转成字典，再转成列表加到goods列表里
for i in data:
    var = {'barcode': i[0], 'product': i[1], 'price': i[2]}  # 获取数据转成字典
    li = [var]
    goods.extend(li)  # 把数据加到goods列表里
goods_list = []  # 利用该空列表把数据转移出来


# 给顾客展示商店商品信息（进入商店首页）
def show_list():
    print('序号---------条形码---------商品名称---------单价---------数量---------小计')
    for j in range(len(goods_list)):
        print("{0:<12}{1:<15}{2:<14}{3:<12}{4:<12}{5:<12}".
              format(j, goods_list[j].get('barcode'), goods_list[j].get('product'),
                     goods_list[j].get('price'), goods_list[j].get('number_add'), goods_list[j].
                     get('sum_add')))


# 顾客操作，将商品添加到购物车
def add():
    barcode_add = int(input("请输入要添加商品的条形码："))
    for i in goods:
        if barcode_add == i['barcode']:
            goods_list.append(i)
            numbers_add = int(input("请输入要购买商品的数量"))
            sum_add = numbers_add * i.get('price')
            i['number_add'] = numbers_add
            i['sum_add'] = sum_add
    show_list()  # 返回show_list类


# 顾客操作，修改购物车中的商品信息
def edit():
    barcode_edit = int(input("请输入要修改商品的条形码："))
    numbers_edit = int(input("请输入要修改商品的数量"))
    for i in goods_list:
        if barcode_edit == i['barcode']:
            i['sum_add'] = numbers_edit * i.get('price')
            i['number_add'] = numbers_edit
    show_list()  # 返回show_list类


# 顾客操作，删除购物车中的商品
def delete():
    barcode_delete = int(input("请输入要修改商品的条形码："))
    for i in goods_list:
        if barcode_delete == i['barcode']:
            goods_list.remove(i)
    show_list()  # 返回show_list类


# 顾客操作，结算商品
def payment():
    print('-' * 100)
    show_list()
    print('-' * 100)
    sum = 0
    for i in goods_list:
        sum = sum + i['sum_add']
    print("总价为：", sum)
    print("请扫描！")
    print("欢迎下次光临")
    exit()


# 顾客操作，点击浏览商品信息
def show_goods():
    print("条码------------商品名称------------单价")
    for i in range(len(goods)):
        print("{0:<15}{1:<17}{2:<}".format(goods[i].get('barcode'), goods[i].get('product'), goods[i].get('price')))
    print('-' * 100)


cmd_dict = {'a': add, 'e': edit, 'd': delete, 'p': payment, 's': show_goods}


# 顾客操作指令
def shopping_commend():
    cmd = input("请输入操作指令：添加（a） 修改（e)  删除（d)  结算（p)  超市商品（s)\n")
    if cmd not in cmd_dict:
        print('输入错误！')
    else:
        cmd_dict[cmd]()  # 进入cmd对应的values输出的类中


# 商场管理员登录
def Administrator():
    print("=========================================")
    print("管理员登录页面：")
    print("=========================================")
    root = ['aaa', 'bbb', 'ccc', 'ddd', 'fff']
    root_password = ['123', '456', '789', '223', '245']
    a = list(zip(root, root_password))  # 转换为一一对应的列表
    num = 0  # 定义一个开始为0的计数变量
    while True:
        list_1 = input("请管理员姓名：")
        list_1 = ''.join(list_1.split())  # 把输入的空格去掉，保证在输入时不会因为名字或密码字符串里有多余空格而报错
        l = list_1.split(",")  # 字符串转列表
        list_2 = input("请输入密码：")  # 把输入的空格去掉，保证在输入时不会因为名字或密码字符串里有多余空格而报错
        list_2 = ''.join(list_2.split())
        k = list_2.split(",")
        t = list(zip(l, k))  # 转换为一一对应的列表
        c = []  # 定义一个空列表
        for i in range(len(t)):
            c.append(0)
        for i in range(len(a)):  # 对a列表进行遍历操作，如果a列表中的字符串有一个等于t列表，加入c中
            for j in range(len(t)):
                if a[i] == t[j]:
                    c[j] = c[j] + 1
        text1 = ''.join(str(i) for i in c)  # 由于join里面是字符串类型，让遍历和类型转换同步进行
        text1 = int(text1)  # 把text1类型转换为整型*（非0及1）
        if text1 == 1:
            print("登陆成功！")
            while True:
                show_commend()
        else:
            num += 1
            if num < 3:
                print("用户名或密码错误,请重新输入：")
            if num >= 3:
                print("用户名或密码已经错误3次，请稍后再试！")
                break


# 顾客登录
def Client():
    name = ['aaa', 'bbb', 'ccc', 'ddd', 'fff']
    name_password = ['123', '456', '789', '223', '245']
    a = list(zip(name, name_password))  # 转换为一一对应的列表
    num = 0  # 定义一个开始为0的计数变量
    print("=========================================")
    print("顾客登录页面：")
    print("=========================================")
    while True:
        list_1 = input("请你的姓名：")
        list_1 = ''.join(list_1.split())  # 把输入的空格去掉，保证在输入时不会因为名字或密码字符串里有多余空格而报错
        l = list_1.split(",")  # 字符串转列表
        list_2 = input("请输入密码：")
        list_2 = ''.join(list_2.split())  # 把输入的空格去掉，保证在输入时不会因为名字或密码字符串里有多余空格而报错
        k = list_2.split(",")
        t = list(zip(l, k))  # 转换为一一对应的列表
        c = []  # 定义一个空列表
        for i in range(len(t)):
            c.append(0)
        for i in range(len(a)):  # 对a列表进行遍历操作，如果a列表中的字符串有一个等于t列表，加入c中
            for j in range(len(t)):
                if a[i] == t[j]:
                    c[j] = c[j] + 1
        text1 = ''.join(str(i) for i in c)  # 由于join里面是字符串类型，让遍历和类型转换同步进行
        text1 = int(text1)  # 把text1类型转换为整型*（非0及1）
        if text1 == 1:
            print("登陆成功！")
            print("欢迎光临来到我的超市")
            print("以下是我的商品清单，请挑选：")
            show_goods()
            print("还未购买商品")
            while True:
                shopping_commend()
        else:
            num += 1
            if num < 3:
                print("用户名或密码错误,请重新输入：")
            if num >= 3:
                print("用户名或密码已经错误3次，请稍后再试！")
                break


# 起始页面
def Start():
    print("=========================================")
    print("欢迎来到XXX商场电子系统!")
    print("=========================================")
    use = int(input("顾客登录请按1,商场管理员登录请按2："))
    if use == 1:
        Client()
    else:
        Administrator()


Start()  # 执行Start类
