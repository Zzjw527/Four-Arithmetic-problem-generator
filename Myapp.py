# -*- coding:utf-8 -*-
import sys, getopt

from Include.gui import *
from Include.randomFormula import *
from Include.check import *


def main(argv):
    n_parameter = 10
    r_parameter = 10
    back = 1
    try:
        input_np = ''
        input_rp = ''
        opts, args = getopt.getopt(argv, "hgn:r:e:a:", ["ifile=", "ofile="])
    except getopt.GetoptError:
        print('Error: 命令错误 \n 正确格式为-n num -r num / -g / -h \n（可输入参数-h输出帮助信息）')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print(
                " ***帮助信息***\n-h  输出帮助信息\n-n  指定生成表达式数量，如果不修改默认10(必须是不小于0的整数，且参数顺序先n后r)\n-r  指定生成表达式各个数字的取值范围，如果不修改默认10(必须是不小于0的整数)\n-a  需和-e参数共同使用进行批改，指定答案文件，需要与-e同时使用\n-e  需和-a参数共同使用进行批改，指定练习文件，需要与-a同时使用\n-g  开启GUI,拥有上诉所有功能")
            sys.exit(2)
        elif opt in ("-n", "--num"):
            n_parameter = arg


        elif opt in ("-r", "--range"):
            r_parameter = arg

        elif opt in ("-e", "--question"):
            input_np = arg
        elif opt in ("-a", "--answer"):
            input_rp = arg
        elif opt in ("-g", "--gui"):
            creatGUI(n_parameter, r_parameter)
            back = 0
    if (back):
        if (input_np == '' and input_rp == ''):
            start_making(n_parameter, r_parameter)
        else:
            checkanswer(input_np, input_rp)


def checkanswer(input_np, input_rp):
    try:
        question_path = open(input_np, 'r', encoding='utf-8')
        question_text = question_path.read()
    except IOError:
        print("Error: 没有从该路径：{}\n找到问题文件/读取问题文件失败\n请重新填写正确路径\n\n".format(input_np))
    else:
        try:
            answer_path = open(input_rp, 'r', encoding='utf-8')
            answer_text = answer_path.read()
        except IOError:
            print("Error: 没有从该路径：{}\n找到答案文件/读取答案文件失败\n请重新填写正确路径\n\n".format(input_rp))
        else:

            q_spilt = re.split('\n', question_text)
            a_spilt = re.split('\n', answer_text)
            if (len(q_spilt) == len(a_spilt)):
                aq_dict = dict(zip(q_spilt, a_spilt))
                getdown = getcheckAnswers(aq_dict)
                Grade_txt = open('Grade' + '.txt', "w", encoding='utf-8')
                Grade_txt.write(getdown)
                Grade_txt.close()
            else:
                print("Error: 题目答案个数不同：\n题目个数" + str(len(q_spilt)) + "\n答案个数：" + str(
                    len(a_spilt)) + "\n请重新填写正确的题目答案个数\n\n")


def start_making(n_num, r_num):
    Exercises_txt = open('Exercises' + '.txt', "w", encoding='utf-8')
    Answers_txt = open('Answers' + '.txt', "w", encoding='utf-8')

    getmain = mainRandomFormula(r_num, n_num)
    for i in range(len(getmain[0])):
        Exercises_txt.write(str(i + 1) + "." + getmain[0][i] + '\n')
        Answers_txt.write(str(i + 1) + "." + getmain[1][i] + '\n')
    Exercises_txt.close()
    Answers_txt.close()
    print("已成功生成" + str(n_num) + "道题目，其中范围在0~" + str(r_num) + "中")
    return getmain


if __name__ == '__main__':
    main(sys.argv[1:])