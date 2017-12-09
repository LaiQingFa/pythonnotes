
#Python的 for 循环就可以依次把list或tuple的每个元素迭代出来
#注意:  name 这个变量是在 for 循环中定义的，意思是，依次取出list中的每一个元素，并把元素赋值给 name，然后执行for循环体（就是缩进的代码块）。
# L = ['Adam', 'Lisa', 'Bart']
# for name in L:
#     print(name)

#和 for 循环不同的另一种循环是 while 循环，while 循环不会迭代 list 或 tuple 的元素，而是根据表达式判断循环是否结束。
# N = 10
# x = 0
# while x < N:
#     print(x)
#     x = x + 1

#用 for 循环或者 while 循环时，如果要在循环体内直接退出循环，可以使用 break 语句。
# sum = 0
# x = 1
# while True:
#     sum = sum + x
#     x = x + 1
#     if x > 100:
#         break
# print(sum)

#在循环过程中，可以用break退出当前循环，还可以用continue跳过后续循环代码，继续下一次循环。
# L = [75, 98, 59, 81, 66, 43, 69, 85]
# sum = 0.0
# n = 0
# for x in L:
#     if x < 60:
#         continue
#     sum = sum + x
#     n = n + 1
# print(sum / n)

#在Python中，定义一个函数要使用 def 语句，依次写出函数名、括号、括号中的参数和冒号:，
# 然后，在缩进块中编写函数体，函数的返回值用 return 语句返回。
# def my_abs(x):
#     if x >= 0:
#         return x
#     else:
#         return -x
# print(my_abs(5))

# import math
# def move(x, y, step, angle):
#     nx = x + step * math.cos(angle)
#     ny = y - step * math.sin(angle)
#     return nx, ny
# x, y = move(100, 100, 60, math.pi / 6)
# print(x, y)
#在语法上，返回一个tuple可以省略括号，而多个变量可以同时接收一个tuple，
# 按位置赋给对应的值，所以，Python的函数返回多值其实就是返回一个tuple，

#对list进行切片 取前3个元素
L = ['Adam', 'Lisa', 'Bart', 'Paul']
print(L[0:3])
#L[0:3]表示，从索引0开始取，直到索引3为止，但不包括索引3。即索引0，1，2，正好是3个元素。
# 如果第一个索引是0，还可以省略;只用一个 : ，表示从头到尾



