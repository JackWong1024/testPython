# !/usr/bin/python
#! /usr/bin/env python
# _*_encoding: utf-8 _*_
# print("hello,world");
# print("这是我编写的第一个py脚本")
# print("你好啊,我的世界")
# if True:
#     print("这是 true")
# else:
#     print("这是 false")
# total = "item1" + \
#         "item1" + \
#         "item3"
# number = 1
# a = 2
# number = a + number
# print(total)
# print(number)
# """为什么注释是这个样子的...有点反人类啊"""
# """行吧.这下面就开始等待输入了:"""
# input_str=input("按下enter退出,其他的任意键显示 \n")
# print(input_str)
######################################################标量类型
#列表允许更新
# print(a,number)
# list = [ 'a','b','c','d','e' ]
# print(len(list))
# print(list)
# print(list[1])
# print(list[2:])
# print(list[3:4:1]*2)
#元组不允许更新,列表和词典是可以更新的  等同于数据的固定数量
# tuple=('a','b','c','d','e' )
# tinytulple=()
# print(tuple[1])
# print(tuple[2:])
# print(tuple[1:3])
#词典是仅次于列表的内置数据结构组合  就是json串格式啊.这就是一个对象..map
# dict={}
# dict["杰克马"]="吹牛逼"
# dict["王健林"]="装逼犯"
# dict["周恩来"]="1976"
# print(dict['杰克马'])
# print(dict["王健林"])
# print(dict.keys())
# print(dict.values())
# print(len(dict["杰克马"]))
# #python数据类型的转换
# num=int(dict["周恩来"])
# print(num)
# print(type(num))

###############################运算符
#基本运算符
# a,b=10,5
# print(a*b)
# print(a*2+b)
# print(int(a/b))
# print(a%b)
# print(a**b)
# print(9//2)
# print(9//-2)
#比较运算符
#!= == >= <=
# a,b,c=3,10,'3'
# if a!=int(c):
#     print("不等于")
# else:
#     print("等于")
# #赋值运算符
# a-=b
# print(a)
#位运算符  这个后期再看
# a=0x00000000
# b=0x00000001
# c=0o00000000
# print(a & b)
# print(type(a))
# print(type(c))
# num=9
# if (num==8 or num==9):print(num)
# if (num==8 and num==9):print(num)
# else:print("判断有毛病")
# a=1
# while a<20:
#     if a%2==0:
#         print(a,"复数")
#     else:
#         print(a,"单数")
#     a+=1
# numberList=[12,44,33,42,421,21]
# even=[]
# odd=[]
# while len(numberList)>0 and 1:
#     """这里用0 标识 false,1 标识 true"""
#     number=numberList.pop()
#     if number%2==0:
#         even.append(number)
#     else:
#         odd.append(number)
#
# print(even)
# print(odd)
# print(numberList)
# even=[]
# odd=[]
##################################### ''''这里是while 和 else 的组合 使用'''
# while 1 and len(odd)<2 and len(even)<2:
#     number =int(input("输入一个数字:"))
#     if number%2==0:
#         even.append(number)
#     else:
#         odd.append(number)
# else:
#     print(even),print(odd)
########################################for 循环语句
# 以上实例我们使用了内置函数 len() 和 range(),函数 len() 返回列表的长度，即元素的个数。 range返回一个序列的数。
# list=[11,22,33,44]
# for i in list:
#     print(i)
# fruits = ['banana', 'apple', 'mango']
# for index in range(len(fruits)):
#     print('当前水果 :', fruits[index],index)
# else:
#     print("Good bye!")
#for else 和 while else 是一样的.都是 循环结束后 执行else
# str='angel'
# for i in str:
#     if  i=='e':
#         pass
#         print("pass")
# #     print(i)
# tuple=tuple('1234')
# print(tuple)
# list=list('1234')
# print(list)
# print(hex(15))
# cmath 模块的函数跟 math 模块函数基本一致，区别是 cmath 模块运算的是复数，math 模块运算的是数学运算。
# import math
# math.ceil("")
# math.floor()
# 随机数
# import random
#
# print(random.random())
# print(random.choice([1,2,3,4]))
# print(random.choice("abcdef"))
#######################################################格式化字符串
#原来的 str.format()  通过{} 和  : 代替   原来的 %
# print(str.format("%s and %d" % ('word',5)))
# print("{2} {1} {0}".format("a","b","c"))
# print("{name},{url}".format(name="个人主页",url="huanghe.live"))
# #通过字典设置参数
# dict={"name":"我的个人主页","url":"huanghe.live"}
# print("{name},{url}".format(**dict))
# #通过列表索引
# list=["这是主页","这是url"]
# print("{0[0]},{0[1]}".format(list))
#
# #向format中传入对象
# class AssignValue(object):
#     def __init__(self,value):
#         self.value=value
# my_value=AssignValue(6)
# print('{0.value}'.format(my_value))
# #数字的格式化
# print("{:,}".format(22222223.1415925))
# print("{:.3%}".format(2.33333333))
# import math
# print("{:.2%}".format(math.pi))
#######################################################列表
# list1 = ['physics', 'chemistry', 1997, 2000]
# list2 = [1, 2, 3, 4, 5, 6, 7 ]
# print(list1[0])
# print(list2[1:3])
# del list1[0]
# del list2[2]
# print(list1[0])
# print(list2[1:3])
# #列表的一些操作
# list3=["我"]*4
# print(list3)
# print(2000 in list1)
#列表函数和方法
# list1=["1","2"]
# list2=[1,2,3]
# list1.extend(list2)
# print(list1)
#按照第二个元素来排序
# def takeSecond(elem):
#     return elem[1]
# random = [(2, 2), (3, 4), (4, 1), (1, 3)]
# random.sort(key=takeSecond,reverse=False)
# print(random)
##############################################字典.同对象.map
# dict={'a':1,'b':2}
# print(dict.keys(),dict.values(),dict['a'])
# # print(dict['c'])
# dict['a']=123
# # del dict['a']
# # print(dict['a'])
# dict.clear()
# print(dict)
#字典的键不允许出现两次,如果赋值两次后一个值会被记住,键必须不可选,所以可以 用数字,字符串,元组.但是list就不行.
# 1	cmp(dict1, dict2)
# 比较两个字典元素。
# 2	len(dict)
# 计算字典元素个数，即键的总数。
# 3	str(dict)
# 输出字典可打印的字符串表示。
# 4	type(variable)
# 返回输入的变量类型，如果变量是字典就返回字典类型。
##################################################日期和时间
# import time
# time1=time.time()
# print("{:.1f}".format(time1))
# #获取时间元组
# timeTuply=time.localtime(time.time())
# print(timeTuply)
# localTime=time.asctime(timeTuply)
# print(localTime)
#
# #格式化时间
# print(time.strftime("%Y-%m-%d %H:%M:%S",time.localtime()))
# print(time.localtime())
# print(time.localtime())
# print(time.timezone)
##################################################函数
# def functionname(parameters):
#     "含糊文档字符串"
    # function_suite   函数组件
    # return [expression]  表达式
# str="aaaaaa"
# def printme(str):
#     "打印传入的字符串打印到控制台"
#     print(str)
#     return
# #函数的调用.
# printme(str)
# printme(input("输入的的东西:"))
#这里要注意  可变以及不可变对象:
# 主不能说传递还是引用传递.我们应该说传不可变对象和可变对象
# def changname(mylist):
#     '修改传入的列表'
#     mylist.append([1,2,3,4])
#     print("函数内的取值",mylist)
#     return
# mylist=[10,20]
# changname(mylist)
# print(mylist)
def printme(str):
    print("这里是一个小小的打印调用:",str)
    return
printme("{1} {1}".format("啊",123))

def testOrder(a,b):
    print(a)
    print(b)
testOrder(b=1,a=22)


# 可写函数说明 ..这里可以设置默认值
def printinfo(name, age=35):
    "打印任何传入的字符串"
    print("Name: ", name)
    print ("Age ", age)
    return
# 调用printinfo函数
# printinfo(age=50, name="miki")
printinfo(name="miki")