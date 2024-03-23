import  random

#输入及判断
while True:
    maxnum = input("输入最大值")
    minnum = input("输入最小值")
    total = input("题目总数")

    if not (maxnum.isdigit() and minnum.isdigit() and total.isdigit()):
        print("请输入数字！")
    else:
        maxnum = int(maxnum)
        minnum = int(minnum)
        total = int(total)
        break

    if maxnum == minnum or total <= 0:
        print ("认真的？")
    elif maxnum == minnum == 0:
        print ("这还要算吗？")
    elif maxnum < minnum :
        print ("大小搞反了哦！")
        break

# 定义运算符号和对应的操作
operations = {
    '+': lambda x, y: x + y,
    '-': lambda x, y: x - y,
    'x': lambda x, y: x * y,
    '÷': lambda x, y: y / x
}



while total >= 0 :
    num1 = random.randint(minnum,maxnum)
    num2 = random.randint(minnum,maxnum)

    # 从列表中抽取一个符号
    symbols = ['+', '-', 'x', '÷'] 
    chosen_symbol = random.choice(symbols)


    if chosen_symbol == '-' and num1 < num2:
        num1,num2 = num2,num1       
        #print ("-")
        pass
    elif chosen_symbol == '÷' and (num1 == 0 or num2 == 0):
        #print ("÷")
        continue
    else :
        pass

    result = int(operations[chosen_symbol](num1, num2))

    question = open('题目.txt','a')
    question.write((f"{num1} {chosen_symbol} {num2} = ") + '\n')
    
    answer = open('答案.txt','a')
    answer.write((f"{num1} {chosen_symbol} {num2} = {result}") + '\n')

    print(f"{num1} {chosen_symbol} {num2} = ")
    print(f"{num1} {chosen_symbol} {num2} = {result}")
    total = total - 1