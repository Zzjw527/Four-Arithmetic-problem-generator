import random
from Include.check import checkFormula
import re
from Include.calculate import *
from Include.randomNumber import random_parameter


# 返回随机生成的操作符
def getRandomOperation(count):
    op = []
    for i in range(count):
        op_count = random.randint(0, 3)
        operation = ['+', '-', '×', '÷']
        op.append(operation[op_count])
    return op


# 返回无括号的算式
def getFormula(parameter_list, op_list):
    first_str = parameter_list[0]
    formula_list = []
    formula_list.append(first_str)
    for index in range(len(op_list)):
        formula_list.append(op_list[index])
        formula_list.append(parameter_list[index + 1])
    return " ".join(str(i) for i in formula_list)


# 返回带括号的算式
def getFormulaWithBracket(parameter_list, op_list, bracket_count):
    # global sub_tring
    # try:

    # 存储最终算式的数组
    formula_list = []

    # 当括号个数为1时
    if bracket_count == 1:

        # 随机获取左括号的位置，然后再根据左括号的位置来随机获取到右括号的位置
        left_bracket_index = random.randint(0, len(op_list) - 1)
        right_bracket_index = random.randint(left_bracket_index + 1, len(parameter_list) - 1)

        # 当左括号在最左边
        if left_bracket_index == 0:
            first_str = '(' + parameter_list[0]
        else:
            first_str = parameter_list[0]
        formula_list.append(first_str)

        for index in range(len(op_list)):

            formula_list.append(op_list[index])

            if index + 1 == left_bracket_index:
                formula_list.append('(')

            formula_list.append(parameter_list[index + 1])

            if index + 1 == right_bracket_index:
                formula_list.append(')')

    # 当括号个数为2时
    elif bracket_count == 2:

        # 随机生成两个括号的形式：0 表示并列的形式，例如（ A + B ）+(C + D), 1表示嵌套的括号，例如 ((A + B) * C) +D
        tag = random.randint(0, 1)

        # 生成并列形式的两个括号
        if tag == 0:
            formula_list.append('(' + parameter_list[0])
            for index in range(len(op_list)):

                formula_list.append(op_list[index])

                if index == 1:
                    formula_list.append('(')

                formula_list.append(parameter_list[index + 1])

                if index == 0 or index == 2:
                    formula_list.append(')')

        # 生成嵌套形式的括号
        else:

            # 随机确定外层括号的位置， 0表示 （A + B + C）+ D，1表示 A +( B + C+ D）
            random_str = random.randint(0, 1)
            subparameter_list = []
            suboperation_list = []

            if random_str == 0:

                subparameter_list.append(parameter_list[0])

                # 决定外层括号位置之后将里面的子字符串内容进行递归来决定内层括号位置
                # 先截取外层括号里的子字符串内容
                for index in range(len(op_list)):
                    if index == 2:
                        break
                    suboperation_list.append(op_list[index])
                    subparameter_list.append(parameter_list[index + 1])
                # 然后递归获得内层括号
                sub_tring = getFormulaWithBracket(subparameter_list, suboperation_list, bracket_count - 1)

                # 拼接最终算式
                formula_list.append('(' + sub_tring + ') ' + op_list[-1] + ' ' + parameter_list[-1])

            else:

                subparameter_list.append(parameter_list[1])

                # 决定外层括号位置之后将里面的子字符串内容进行递归来决定内层括号位置
                # 先截取外层括号里的子字符串内容
                for index in range(len(op_list)):
                    if index > 0:
                        suboperation_list.append(op_list[index])
                        subparameter_list.append(parameter_list[index + 1])
                # 然后递归获得内层括号
                sub_tring = getFormulaWithBracket(subparameter_list, suboperation_list, bracket_count - 1)

                # 拼接最终算式
                formula_list.append(parameter_list[0] + ' ' + op_list[0] + ' (' + sub_tring + ')')

    return " ".join(str(i) for i in formula_list)
    '''except BaseException:
        print(parameter_list)
        print(op_list)
       # a = sub_tring
        print(sub_tring)
        return'''


# 决定生成哪种算式
def randomFormula(maxNum):
    # 随机得到运算符个数
    op_count = random.randint(1, 3)
    # 随机得到运算符数组
    op_list = getRandomOperation(op_count)

    # 括号最多存在个数
    maxBracket = op_count - 1

    # 获取参数列表
    parameter_list = []
    for i in range(op_count + 1):
        parameter_list.append(str(random_parameter(maxNum)))

    # 根据最大括号数再来决定实际的括号数
    if maxBracket == 0:
        return getFormula(parameter_list, op_list)
    elif maxBracket == 1:
        # 随机决定括号个数
        tag = random.randint(0, maxBracket)
        if tag == 0:
            return getFormula(parameter_list, op_list)
        elif tag == 1:
            return getFormulaWithBracket(parameter_list, op_list, tag)
    elif maxBracket == 2:
        # 随机决定括号个数
        tag = random.randint(0, maxBracket)
        if tag == 0:
            return getFormula(parameter_list, op_list)
        elif tag == 1 or tag == 2:
            return getFormulaWithBracket(parameter_list, op_list, tag)


# 判断生成算式是否重复，若重复重新生成
def checkrepeat(q_list, all_question, a_list, all_answer):
    if (len(all_question) and len(all_answer)):
        const_op = ("+", "-", "×", "÷")
        numbernum = []
        all_num = []
        symbol = []
        all_symbol = []
        for alnum in processeFormula(q_list[0]):
            if alnum in const_op:
                symbol.append(alnum)
        numbernum.append(len(processeFormula(q_list[0])) - len(symbol))

        for alqust in all_question:
            num = 0
            for alqustnum in processeFormula(alqust):

                singlequst = []
                if alqustnum in const_op:
                    singlequst.append(alqustnum)
                    num += 1
                if (len(singlequst)):
                    all_symbol.append(singlequst[0])
            all_num.append(len(processeFormula(alqust)) - num)

        samesymbol = [x for x in symbol if x in all_symbol]
        sameanswer = [x for x in a_list if x in all_answer]
        samenum = [x for x in numbernum if x in all_num]
        if (len(samesymbol) and len(sameanswer) and len(samenum)):
            return True
        else:
            return False
    else:
        return False


def checkrepeatup(q_list, all_question, a_list, all_answer):
    if (len(all_question) and len(all_answer)):
        sameanswer = [x for x in a_list if x in all_answer]
        if (len(sameanswer)):
            return True
        else:
            return False
    else:
        return False


# 随机生成算式主入口  maxNum 题目答案最大值， formula_count 题目数量
def mainRandomFormula(maxNum, formula_count):
    # 存储算式
    formula_list = []
    # 存储答案
    answer_list = []

    count = 1
    formula_count = int(formula_count)
    while (count <= formula_count):
        # 随机获取一个算式
        formula = randomFormula(maxNum)
        answer = checkFormula(formula, maxNum)
        # 判断是否重复
        if (formula_count<100):
            if (checkrepeat(formula, formula_list, answer, answer_list)):
                continue

        else:
            if (checkrepeatup(formula, formula_list, answer, answer_list)):
                continue
        # 判断值是否存在
        if 'Null' in answer:
            continue
        formula_list.append(formula)
        answer_list.append(answer)
        count += 1
    randomfor = []
    randomfor.append(formula_list)
    randomfor.append(answer_list)
    return randomfor






