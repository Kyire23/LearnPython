class TemperatureConverter:
    @staticmethod 
    def f2c(t_f): #华氏温度到摄氏温度的转换
            t_f = float(t_f)
            t_c = (t_f - 32) * 5 /9
            return t_c
#测试代码
t_f = float(input("请输入华氏温度： "))
t_c = TemperatureConverter.f2c(t_f)
print(t_c)

