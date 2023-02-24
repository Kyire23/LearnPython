import csv
def readcsv2(csvfilepath):
    with open(csvfilepath, newline='') as f:  #打开文件
        f_csv = csv.DictReader(f)     #创建csv.DictReader对象
        for row in f_csv:             #循环打印各行（字典）
            print(row)
if __name__ == '__main__':
    readcsv2(r'scores.csv')
