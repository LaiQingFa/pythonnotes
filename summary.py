# 默认情况下，Python 3 源码文件以 UTF-8 编码，所有字符串都是 unicode 字符串

# python最具特色的就是使用缩进来表示代码块，不需要使用大括号({})。
# python中数有四种类型：整数、长整数、浮点数和复数
#函数之间或类的方法之间用空行分隔，表示一段新的代码的开始。类和函数入口之间也用一行空行分隔，以突出函数入口的开始。

#在 python 用 import 或者 from...import 来导入相应的模块。
#将整个模块(somemodule)导入，格式为： import somemodule
#从某个模块中导入某个函数,格式为： from somemodule import somefunction
#从某个模块中导入多个函数,格式为： from somemodule import firstfunc, secondfunc, thirdfunc
#将某个模块中的全部函数导入，格式为： from somemodule import *

#Python 中的变量不需要声明。每个变量在使用前都必须赋值，变量赋值以后该变量才会被创建。
#在 Python 中，变量就是变量，它没有类型，我们所说的"类型"是变量所指的内存中对象的类型。 Python允许你同时为多个变量赋值

#Python3 中有六个标准的数据类型：
#Number（数字）:

#Python3 支持 int、float、bool、complex（复数）。
#在Python 3里，只有一种整数类型 int，表示为长整型，没有 python2 中的 Long。
#在 Python2 中是没有布尔型的，它用数字 0 表示 False，用 1 表示 True。到 Python3 中，把 True 和 False 定义成关键字了，但它们的值还是 1 和 0，它们可以和数字相加
#   >>>5 + 4  # 加法
#   9
#   >>> 4.3 - 2 # 减法
#   2.3
#   >>> 3 * 7  # 乘法
#   21
#   >>> 2 / 4  # 除法，得到一个浮点数
#   0.5
#   >>> 2 // 4 # 除法，得到一个整数
#   0
#   >>> 17 % 3 # 取余
#   2
#   >>> 2 ** 5 # 乘方
#   32

#String（字符串）:

#   Python中的字符串用单引号(')或双引号(")括起来，同时使用反斜杠(\)转义特殊字符。
#   字符串的截取的语法格式如下：
#   变量[头下标:尾下标]

str = 'Runoob'

print(str)  # 输出字符串
print(str[0:-1])  # 输出第一个到倒数第二个的所有字符
print(str[0])  # 输出字符串第一个字符
print(str[2:5])  # 输出从第三个开始到第五个的字符
print(str[2:])  # 输出从第三个开始的后的所有字符
print(str * 2)  # 输出字符串两次
print(str + "TEST")  # 连接字符串

# 使用反斜杠(\)转义特殊字符，如果你不想让反斜杠发生转义，可以在字符串前面添加一个 r，表示原始字符串


#List（列表）:

#List（列表） 是 Python 中使用最频繁的数据类型。
#列表可以完成大多数集合类的数据结构实现。列表中元素的类型可以不相同，它支持数字，字符串甚至可以包含列表（所谓嵌套）。
#列表是写在方括号([])之间、用逗号分隔开的元素列表。
#和字符串一样，列表同样可以被索引和截取，列表被截取后返回一个包含所需元素的新列表。
#列表截取的语法格式如下：
#变量[头下标:尾下标]

#索引值以 0 为开始值，-1 为从末尾的开始位置。
#加号（+）是列表连接运算符，星号（*）是重复操作。如下实例：

list = ['abcd', 786, 2.23, 'runoob', 70.2]
tinylist = [123, 'runoob']

print(list)  # 输出完整列表
print(list[0])  # 输出列表第一个元素
print(list[1:3])  # 从第二个开始输出到第三个元素
print(list[2:])  # 输出从第三个元素开始的所有元素
print(tinylist * 2)  # 输出两次列表
print(list + tinylist)  # 连接列表

#与Python字符串不一样的是，列表中的元素是可以改变的：

#Tuple（元组）:

#元组（tuple）与列表类似，不同之处在于元组的元素不能修改。元组写在小括号(())里，元素之间用逗号隔开。
#元组中的元素类型也可以不相同：

tuple = ('abcd', 786, 2.23, 'runoob', 70.2)
tinytuple = (123, 'runoob')

print(tuple)  # 输出完整元组
print(tuple[0])  # 输出元组的第一个元素
print(tuple[1:3])  # 输出从第二个元素开始到第三个元素
print(tuple[2:])  # 输出从第三个元素开始的所有元素
print(tinytuple * 2)  # 输出两次元组
print(tuple + tinytuple)  # 连接元组

# 元组与字符串类似，可以被索引且下标索引从0开始，-1 为从末尾开始的位置。也可以进行截取
# 其实，可以把字符串看作一种特殊的元组。
# 虽然tuple的元素不可改变，但它可以包含可变的对象，比如list列表。
# 构造包含 0 个或 1 个元素的元组比较特殊，所以有一些额外的语法规则：
tup1 = ()    # 空元组
tup2 = (20,) # 一个元素，需要在元素后添加逗号

#Sets（集合）:

# 集合（set）是一个无序不重复元素的序列。
# 基本功能是进行成员关系测试和删除重复元素。
# 可以使用大括号 { } 或者 set() 函数创建集合，注意：创建一个空集合必须用 set() 而不是 { }，因为 { } 是用来创建一个空字典。
student = {'Tom', 'Jim', 'Mary', 'Tom', 'Jack', 'Rose'}

print(student)  # 输出集合，重复的元素被自动去掉

# 成员测试
if ('Rose' in student):
    print('Rose 在集合中')
else:
    print('Rose 不在集合中')

# set可以进行集合运算
a = set('abracadabra')
b = set('alacazam')

print(a)

print(a - b)  # a和b的差集

print(a | b)  # a和b的并集

print(a & b)  # a和b的交集

print(a ^ b)  # a和b中不同时存在的元素

#Dictionary（字典）:

# 字典（dictionary）是Python中另一个非常有用的内置数据类型。
# 列表是有序的对象结合，字典是无序的对象集合。两者之间的区别在于：字典当中的元素是通过键来存取的，而不是通过偏移存取。
# 字典是一种映射类型，字典用"{ }"标识，它是一个无序的键(key) : 值(value)对集合。类似java中的hashmap
# 键(key)必须使用不可变类型。
# 在同一个字典中，键(key)必须是唯一的。
dict = {}
dict['one'] = "1 - 菜鸟教程"
dict[2] = "2 - 菜鸟工具"

tinydict = {'name': 'runoob', 'code': 1, 'site': 'www.runoob.com'}

print(dict['one'])  # 输出键为 'one' 的值
print(dict[2])  # 输出键为 2 的值
print(tinydict)  # 输出完整的字典
print(tinydict.keys())  # 输出所有键
print(tinydict.values())  # 输出所有值

# Python数据类型转换 :http://www.runoob.com/python3/python3-data-type.html