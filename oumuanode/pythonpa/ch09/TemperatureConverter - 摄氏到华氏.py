class TemperatureConverter:
    @staticmethod 
    def c2f(t_c): #摄氏温度到华氏温度的转换
            t_c = float(t_c)
            t_f = (t_c * 9/5) + 32
            return t_f
#测试代码
t_c = float(input("请输入摄氏温度： "))
t_f = TemperatureConverter.c2f(t_c)
print(t_f)
