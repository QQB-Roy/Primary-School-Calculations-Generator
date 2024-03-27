# -*- coding: utf-8 -*-
#小学计算题生成器
#Primary School Calculation Generator

import random,os,time

# 获取当前时间
current_time = time.localtime()

# 转换为指定格式的字符串，包含中文
t = time.strftime("%m月%d日 %H时%M分%S秒", current_time)

#符号
key_symbols = {1:['+'], 2:['-'], 3:['x'], 4:['÷'],
           12:['+','-'],13:['+','x'],14:['+','÷'],
           23:['-','x'],24:['-','÷'],
           34:['x','÷'],
           123:['+','-','x'],124:['+','-','÷'],134:['+','x','÷'],
           234:['-','x','÷'],
           1234:['+','-','x','÷']
           }

check_keys = set.union({(1), (2), (3), (4), (12), (13), (14), (23), (24), (34),
                         (123), (124), (134), (234), (1234)})


#输入及判断
while True:
    maxnum = input("输入最大值" + '\n')
    minnum = input("输入最小值" + '\n')
    total = input("题目总数" + '\n')
    key = input("请按顺序输入你想要的符号" + '\n' +
                "1:+, 2:-, 3:x, 4:÷" + '\n' +
                "例如+和÷输入14" + '\n')


    if not (maxnum.isdigit() and minnum.isdigit() and total.isdigit() and key.isdigit()):
        print("请输入数字！")
        continue
    else:
        maxnum = int(maxnum)
        minnum = int(minnum)
        total = int(total)
        key = int(key)
    
    if maxnum == minnum or total <= 0:
        print ("认真的？")
        continue
    elif maxnum == minnum == 0:
        print ("这还要算吗？")
        continue
    elif maxnum < minnum :
        print ("大小搞反了哦！")
        continue
    elif key not in check_keys:
         print("有这个数吗？")
         continue
    else:
        break


#选取列表
if key in key_symbols:
    symbols = key_symbols[key]

# 定义运算符号和对应的操作
operations = {
    '+': lambda x, y: x + y,
    '-': lambda x, y: x - y,
    'x': lambda x, y: x * y,
    '÷': lambda x, y: x / y
}

#新建文件夹
folder_name = './' + t
if not os.path.exists(folder_name):
    os.makedirs(folder_name)

question_file = folder_name + '/题目.txt'
answer_file = folder_name + '/答案.txt'

#输出部分
def output():
    with open(question_file, 'a', encoding='utf-8') as qf:
        qf.write(f"{num1} {chosen_symbol} {num2} = \n")

    with open(answer_file, 'a', encoding='utf-8') as af:
        af.write(f"{num1} {chosen_symbol} {num2} = {result}\n")

    print(f"{num1} {chosen_symbol} {num2} = ")
    print(f"{num1} {chosen_symbol} {num2} = {result}")

#公因数计算
def factors(number):
    factors = []
    for i in range(1, number + 1):
        if number % i == 0:
            factors.append(i)
    return factors


#运算
while total >= 0 :
    num1 = random.randint(minnum,maxnum)
    num2 = random.randint(minnum,maxnum)

    # 从列表中抽取一个符号 
    chosen_symbol = random.choice(symbols)


    if chosen_symbol in ('-','÷') and num1 < num2:
        num1,num2 = num2,num1       
        #print ("-")
        pass
    elif chosen_symbol == '÷' and (num1 == 0 or num2 == 0):
        #print ("÷")
        continue
    if chosen_symbol == '÷':
        num1_factors = factors(num1)
        num2 = random.choice(num1_factors)
        pass


    result = operations[chosen_symbol](num1, num2)
    output()

    total = total - 1

os.system("pause")