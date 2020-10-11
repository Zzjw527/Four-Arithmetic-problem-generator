import json
import re
from fractions import Fraction
from Include.calculate import operate, processeNumber


#去除无用括号
def checkBracket( formula ):

    formula = re.sub(' ', '', formula)
    l = list(formula)
    left_bracket_index = [key for key, value in enumerate(l) if value == '(']
    right_bracket_index = [key for key, value in enumerate(l) if value == ')']




    if len(left_bracket_index) == 2:
        if left_bracket_index[1] - left_bracket_index[0] == 1 and right_bracket_index[1] - right_bracket_index[0] == 1:
            del l[right_bracket_index[0]]
            del l[left_bracket_index[1]]
            del left_bracket_index[1]
            del right_bracket_index[0]

    if l.index('(') == 0 and l.index(')') ==  len(l) -1 :
        del l[l.index('(')]
        del l[l.index(')')]

    print(left_bracket_index,right_bracket_index)
    print(l)
    return


#检测算式的答案是否符合要求, 符合则返回具体答案，否则返回空 ''
def checkFormula( formula, maxNum ):

    answer = operate(formula)

    #去除答案为负数 和 算式中除数为零时 的算式
    if '-' in answer[0] or ' ' in answer[0]:
        return 'Null'

#    answer = processeNumber(answer[0])
#    maxNum = processeNumber(str(maxNum))

    return str(answer)



#检查答案对错（用于文件输入）
def checkAnswers( question_text ):

    correct_list = []
    wrong_list = []

    count = 0

    for i in question_text:

        if i == '':
            break

        count += 1
        result = operate(i)
      #  strtt = question_text[i]
        if question_text[i] == result:
            correct_list.append(str(count))
        else:
            wrong_list.append(str(count))

    correct_count = len(correct_list)
    wrong_count = len(wrong_list)

    correct_str = "Correct: "+ str(correct_count) +'('+",".join(str(i) for i in correct_list) + ')'
    wrong_str = "Wrong: "+ str(wrong_count) +'('+",".join(str(i) for i in wrong_list) + ')'

    print(correct_str,wrong_str)
    return correct_list

def wrongAnswers( question_text ):

    correct_list = []
    wrong_list = []

    count = 0

    for i in question_text:

        if i == '':
            break

        count += 1
        result = operate(i)
      #  strtt = question_text[i]
        if question_text[i] == result:
            correct_list.append(str(count))
        else:
            wrong_list.append(str(count))

    return wrong_list

def getcheckAnswers( question_text ):


    correct_list = []
    wrong_list = []

    count = 0

    for i in question_text:

        if i == '':
            break

        count += 1
        result = operate(i)
      #  strtt = question_text[i]
        if question_text[i] == result:
            correct_list.append(str(count))
        else:
            wrong_list.append(str(count))

    correct_count = len(correct_list)
    wrong_count = len(wrong_list)

    correct_str = "Correct: "+ str(correct_count) +'('+",".join(str(i) for i in correct_list) + ')'
    wrong_str = "Wrong: "+ str(wrong_count) +'('+",".join(str(i) for i in wrong_list) + ')'
    last_str=correct_str+"\n"+wrong_str
    print(correct_str,wrong_str)
    return last_str