import math

# 输入半径长度
radius = float(input("请输入圆的半径长度："))

# 计算圆的面积
area = math.pi * radius ** 2

# 计算圆的周长
circumference = 2 * math.pi * radius

# 打印结果
print("圆的面积为：", area)
print("圆的周长为：", circumference)
