
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
L = [75, 98, 59, 81, 66, 43, 69, 85]
sum = 0.0
n = 0
for x in L:
    if x < 60:
        continue
    sum = sum + x
    n = n + 1
print(sum / n)