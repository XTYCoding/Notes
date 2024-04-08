# 字面量
# 整数 int float complex(复数) bool
666
13.14
"字符串"

print(666)
print(13.14)
print("字符串")

# 变量
a = 100

# 数据类型 用type()
print(type(a))
b = type(a)
print(b)
print(type(type(a)))


# 数据类型转换
num_str = str(11.45)
print(type(num_str))

str_num = float("11.45")
print(str_num,type(str_num))

str_num = int(11)
print(str_num,type(str_num))

str_num = int("11")
print(str_num,type(str_num))

# 运算符 + - * / // % **
print("1+1 = ",1+1)
print("2-1 = ",2-1)
print("3*3 = ",3*3)
print("4/2 = ",4/2)
print("11//2 = ",11//2)
print("9%2 = ",9%2)
print("3**3 = ",3**3)


# 字符串定义方式
name = '字符串'
print(type(name))
name = "字符串"
print(type(name))
# 三引号定义可以当作注释用
name = """字符串
          但是
          有很多
          行"""
print(type(name))

# 字符串包含引号的问题
name = '“字符串”'
print(name)

name = "'字符串'"
print(name)

name = "\"字符串\'"
print(name)

# 字符串拼接 字面量和字面量 字面量和变量 变量和变量 只能字符串之间
print("这是一条"+"字符串")
str1 = "这是一条"
str2 = "字符串"
print("\""+str1+str2+"\"")

# 字符串格式化
num1 = 123
num2 = 234.123
# %表示要占位 后面的s是所在的位置 %s转换成字符串 %d转换成整数 %f转换成浮点
message = "数字1: %s"%num1+"%"+"和数字2: %s"%num2
print(message)
message = "数字1: %d和数字2: %f"%(num1,num2)
print(message)

# 格式化精度控制 用m.n控制 m表示宽度 n表示精度同时四舍五入 m比数字小 不生效
num1 = 111
num2 = 11.345
print("宽度限制5:%5s"% num1)
print("宽度限制2:%2d"% num1)
print("宽度控制7,精度控制2:%7.2s"% num2)
print("精度控制2:%.2f"% num2)

# 快速格式化 不限制精度 原样输出
name = "两个数字"
num1 = 111
num2 = 123.45
print(f"这有{name},一个是:{num1},另一个是:{num2}")

# 表达式
print("1*1= %s"%(1*1))
print(f"1*1 = {1*1}")
print(f"字符串的类型名是:{type(name)}")

# 练习
name = "公司"
stock_price = 19.99
stock_code = "003032"
stock_price_daily_growth_factor = 1.2
growth_days = 7

print(f"公司:{name},股票代码:{stock_code},当前股价:{stock_price}")
print("每日增长系数是:%.2f"%stock_price_daily_growth_factor+",经过%d"%growth_days+"天的增长后,"+"股价达到了:%.2f"%(stock_price*1.2**7))

# 输入 input()语句 input()里可以写提示 输入的都当作字符串
name = input("请输入:")
print("你输入的是:%s"%name)
print("你输入的数据类型是: ",type(name))


