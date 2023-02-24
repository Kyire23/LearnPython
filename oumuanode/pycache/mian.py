"""
@Author = oumuamuanode
@Time : 2022/10/20 16:28
"""
import com.oumuanode.pycache.m1
import m2
import m3

my_list = []

# 调用m1模块
my_list = com.oumuanode.pycache.m1.num_prime(10)
length = len(my_list)
print("素数:")
for i in range(0, length, 1):
    print(my_list[i], end="\t")
print("\n完备数:")

# 调用m2
my_list = []
my_list = m2.num_complete(1000)
length = len(my_list)
for i in range(0, length, 1):
    print(my_list[i], end="\t")
print("\n完备数等式:")

# 调用m3
print(m3.const_1,"=1+2+3")
print(m3.const_2,"=1+2+4+7+14")
print(m3.const_3,"=1+2+4+8+16+31+62+124+248")