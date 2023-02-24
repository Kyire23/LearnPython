"""
@Author = oumuamuanode
@Time : 2022/10/20 16:27
"""


def num_prime(n):
    p_list = []
    for m in range(2, n + 1, 1):
        k = 2
        flag = 0
        while k < m and flag == 0:
            if m % k == 0:
                flag = 1
            k += 1
        if flag == 0:
            p_list.append(m)
    return p_list

# test
if __name__ == "__main__":
    p = num_prime(10)
    print("显示素数列表:\n", p)
