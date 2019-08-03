# -*- coding: utf-8 -*- 
"""
    @Time : 2019/7/30 下午8:34 
    @Author : 黄任添 
    @File : test2.py
    @Software: PyCharm
    note:
        1. 输入输出以及基本数据类型
"""

"""
# 01 一句输入一句输出
test1 = input("请输入一句话:")
# 输出方式一:
print(test1)
# 输出方式二
print(test1, end='')
"""

# 02整数
# 默认是输入十进制,输出进制

# 02.1 十进制输入,十进制输出
test2_a = 12
print("十进制输入:", test2_a)

# 02.2 二进制输入,十进制输出
test2_b = 0b1010101
print("二进制输入:", test2_b)

# 02.3 八进制输入,十进制输出
test2_c = 0o123
print("八进制输入:", test2_c)

# 02.4 十六进制输入,十进制输出
test2_d = 0x1234
print("十六进制输入:", test2_d)

print("*" * 30)

# 02.5 十进制输入,二进制.八进制.十六进制输出
test2_e = 1234
print("二进制:", bin(test2_e))
print("八进制:", oct(test2_e))
print("十进制:", test2_e)
print("十六进制:", hex(test2_e))

print("*" * 30)

# 警告: 注意字符串数字是转换, 输入的格式一定要进制匹配
# 02.6 字符十进制输入,二进制.八进制.十六进制输出
print("二进制:", int('0b10010', base=2))
print("八进制:", int('0o12345', base=8))
print("十进制:", int('11234', base=10))
print("十六进制:", int('0x1123FAB', base=16))
