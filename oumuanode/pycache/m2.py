"""
@Author = oumuamuanode
@Time : 2022/10/20 16:27
"""


def num_complete(n):
    p_list = []
    for m in range(2, n + 1, 1):
        mf = 1
        for k in range(2, m):
            if m % k == 0:
                mf += k
        if m == mf:
            p_list.append(m)
    return p_list


# test
if __name__ == "__main__":
    p = num_complete(1000)
    print("显示素数列表:\n", p)
