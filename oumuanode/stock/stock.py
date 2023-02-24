# 库存类
import pymysql
# import os


class Stock:

    def __init__(self, host, user, password, db_name):
        self.host = host
        self.user = user
        self.password = password
        self.db_name = db_name

    def open(self):
        """打开数据库"""
        self.db = pymysql.connect(host = self.host, user = self.user, password = self.password, db = self.db_name)
        self.cursor = self.db.cursor()

    def exec(self, sql):
        """执行sql"""
        self.cursor.execute(sql)
        self.db.commit()

    def close(self):
        """关闭数据库"""
        self.db.close()  # 关闭数据库连接

    def add(self, product):
        """
        添加产品
            若添加的是新产品，直接添加到原有库存中
            若添加的不是新产品，则添加数量
        """
        self.open()
        sql = str.format(
            "select * from tb_product where product_id = '{0}'", product.product_id)
        try:
            self.cursor.execute(sql)
            rows = self.cursor.fetchall()
            if(not len(rows)):  # 插入的产品ID不存在，则添加产品
                sql = str.format("insert into tb_product values('{0}','{1}',{2},{3})", product.product_id,
                                 product.product_name, product.product_number, product.product_price)
                self.exec(sql)  # 执行sql
            else:  # 插入的产品ID存在且产品名称和产品价格都正确，则更新产品数量
                if(rows[0][1] == product.product_name and rows[0][3] == product.product_price):
                    sql = str.format(
                        "update tb_product set product_number = product_number + {0} where product_id = '{1}'", product.product_number, product.product_id)
                    self.exec(sql)
                else:
                    print('产品名称或产品价格输入有误，更新产品数量失败！\n')
        except:
            self.db.rollback()
        finally:
            self.db.close()

    def dele(self, product):
        """
        取出产品
        若库存中有产品
            若产品数量 < 所取数量
                则提示库存不足
            否则
                减少库存，并提示剩余库存数量
        否则库存中没有产品
            输出提示
        """

        self.open()
        sql = str.format(
            "select * from tb_product where product_id = '{0}'", product.product_id)
        try:
            self.cursor.execute(sql)
            rows = self.cursor.fetchall()
            if(len(rows)):  # 要取出的产品ID存在
                if(rows[0][1] == product.product_name and rows[0][3] == product.product_price):
                    if(rows[0][2] >= product.product_number):  # 库存够
                        sql = str.format(
                            "update tb_product set product_number = product_number - {0} where product_id = '{1}'", product.product_number, product.product_id)
                        self.exec(sql)
                        print(str.format(
                            '取出 {0} 个 {1} 后', product.product_number, product.product_name))
                        Stock.list_all(self)  # 调用类函数
                    else:
                        print('库存数量不足，取出失败！\n')
                else:
                    print('产品名称或产品价格输入有误，取出失败！\n')
            else:
                print('库存中没有该产品！\n')
        except:
            self.db.rollback()
        finally:
            self.db.close()

    def list(self, id):
        """
        查找产品
            若库存中有产品，则输出
            否则提示没有产品
        """
        self.open()
        sql = str.format(
            "select * from tb_product where product_id = '{0}'", id)
        try:
            print(str.format('\n查询产品ID为 {0} 的信息如下：', id))
            print(str.format(
                '{0:^6} | {1:^12} | {2:^6} | {3:^6}', '产品ID', '产品名称', '产品数量', '产品价格'))
            self.cursor.execute(sql)  # 执行SQL语句
            rows = self.cursor.fetchall()
            flag = 0
            for row in rows:
                product_id = row[0]
                product_name = row[1]
                product_number = row[2]
                product_price = row[3]
                print(str.format(
                    '{0:^8} | {1:^12} | {2:^10} | {3:^10}', product_id, product_name, product_number, product_price))
                flag = 1
            if(flag == 0):
                print('库存中没有该产品！')
            print()
        except:
            print("错误：不能获取数据！\n")

    def list_all(self):
        self.open()
        sql = "select * from tb_product"
        try:
            print('\n全部产品信息如下：')
            print(str.format(
                '{0:^6} | {1:^12} | {2:^6} | {3:^6}', '产品ID', '产品名称', '产品数量', '产品价格'))
            self.cursor.execute(sql)  # 执行SQL语句
            rows = self.cursor.fetchall()
            flag = 0
            for row in rows:
                product_id = row[0]
                product_name = row[1]
                product_number = row[2]
                product_price = row[3]
                print(str.format(
                    '{0:^8} | {1:^12} | {2:^10} | {3:^10}', product_id, product_name, product_number, product_price))
                flag = 1

            if(flag == 0):
                print('库存中没有产品！')
            else:
                sql = "select sum(product_number),sum(product_number*product_price) from tb_product"
                self.cursor.execute(sql)  # 执行SQL语句
                rows = self.cursor.fetchall()
                sum_product_number = rows[0][0]
                sum_product_price = rows[0][1]
                print('-'*60)
                print(str.format(
                    '总计:                 | 产品总数:{0:^4} | 产品总价:{1:^4}', sum_product_number, sum_product_price))
                print()
        except:
            print("错误：不能获取数据！")
