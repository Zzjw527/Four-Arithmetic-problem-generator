import re
from fractions import Fraction


#处理算式
def processeFormula( formula ):

    par = formula.partition('.')
    test = par[2].partition('=')[0][:]

    formula = re.sub(' ', '', formula)
    l = list(filter(None, re.split('([\+\-\×\÷\(\)])', formula)))
    return l




#判断是否为操作符
def isOperator( element ):
    operators = ['+', '-', '×', '÷', '(', ')']
    if element in operators:
        return True
    else:
        return False


#判断该对栈进行什么操作，1 表示入栈， -1 表示出栈
def judgeOperation( top, current ):

    low_proxy = ['+', '-']
    mid_proxy = ['×', '÷']
    high_proxy = ['(']
    proxy = [')']


    if top in low_proxy:
        if current in mid_proxy or current in high_proxy:
            return 1
        else:#当两个操作符相等时进行出栈操作
            return -1

    #当 top 为乘除的时候都应出栈进行计算
    elif top in mid_proxy:
        return -1

    elif top in high_proxy:
        if current == ')':
            return 0
        else:
            return 1
    else:
        return 1


#对两个数进行计算
def calculate( num1, num2, op ):

    result = 0

    num1 = processeNumber(num1)
    num2 = processeNumber(num2)

    if op == '+':
        result = num1 + num2
    elif op == '-':
        result = num1 - num2
        if num2 < 0:
            return 'False'
    elif op == '×':
        result = num1 * num2
    elif op == '÷':
        if num2 == 0 or num1 > num2:
            return 'False'
        result = num1 / num2

    return str(result)


#将分数转换成真分数
def transformFractionToTrue(result):
    if '/' in result[0]:
        list = re.split('\/', result[0])
        if int(list[0]) > int(list[1]):
            m = int(int(list[0]) / int(list[1]))
            result = str(m) + "'" + str(int(list[0]) - m * int(list[1])) + '/' + list[1]
           # "".join(str(i) for i in result)
    return result


#对数字进行处理，例如将真分数转为假分数
def processeNumber( num ):

    if '/' not in num:
        return Fraction(int(num))

    elif '\'' in num:
        list_num1 = re.split('([\'\/])', num)
        molecule = int(list_num1[0]) * int(list_num1[4]) + int(list_num1[2])
        return Fraction(molecule, int(list_num1[4]))

    elif '/' in num:
        return Fraction(str(num))



#主要函数
def operate( formula ):

    processedFormula = processeFormula(formula)

    number_stack = []
    operator_stack = []

    for element in processedFormula:

        #判断是数字还是运算符
        op_tag = isOperator( element )

        if op_tag:
            # 如果是运算符
            while True:
                # 如果运算符栈为空和栈顶元素为'('，则入栈
                if len(operator_stack) == 0 or element == '(':
                    operator_stack.append( element )
                    break

                # decision 函数做决策
                tag = judgeOperation( operator_stack[-1], element )
                if tag == 1:
                    # 如果是-1压入运算符栈进入下一次循环
                    operator_stack.append(element)
                    break
                elif tag == 0:
                    # 如果是0弹出运算符栈内最后一个(, 丢掉当前)，进入下一次循环
                    operator_stack.pop()
                    break
                elif tag == -1:
                    # 如果是1弹出运算符栈内最后两个元素，弹出数字栈最后两位元素。
                    op = operator_stack.pop()
                    num2 = number_stack.pop()
                    num1 = number_stack.pop()

                    # 执行计算
                    final_result = calculate(num1, num2, op)

                    #判断算式中是否存在除数为零
                    if 'False' in final_result:
                        return [' ']

                    # 计算之后压入数字栈
                    number_stack.append(final_result)


        else:
            # 如果是数字则压入数字栈
            number_stack.append(element)
        # 处理大循环结束后 数字栈和运算符栈中可能还有元素 的情况
    while len(operator_stack) != 0:
        op = operator_stack.pop()
        num2 = number_stack.pop()
        num1 = number_stack.pop()

        # 执行计算
        final_result = calculate(num1, num2, op)

        # 判断算式中是否存在除数为零
        if 'False' in final_result:
            return [' ']

        number_stack.append(final_result)

    return transformFractionToTrue(number_stack)


