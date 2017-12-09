
#Python的 for 循环就可以依次把list或tuple的每个元素迭代出来
#注意:  name 这个变量是在 for 循环中定义的，意思是，依次取出list中的每一个元素，并把元素赋值给 name，然后执行for循环体（就是缩进的代码块）。
L = ['Adam', 'Lisa', 'Bart']
for name in L:
    print(name)