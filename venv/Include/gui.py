import tkinter
# 导入消息对话框子模块
import tkinter.messagebox
from tkinter.messagebox import *
from tkinter import *
from Include.check import *
from Include.calculate import *
from Myapp import *
import threading
import os
import re
import time


def creatGUI(n_paramet, r_paramet):
    global n_parameter
    global r_parameter
    n_parameter = n_paramet
    r_parameter = r_paramet
    allaqdict = {}

    def start(n_par, r_par):

        aqdict = {}
        lb.delete(0, END)
        aqnum = 1
        print(n_parameter)
        print(r_parameter)
        get_aq = start_making(n_parameter, r_parameter)
        aqdict = dict(zip(get_aq[0], get_aq[1]))
        allaqdict.update(aqdict)
        for i in allaqdict:
            lb.insert(END, str(aqnum) + ".  " + i)
            aqnum += 1

    #        Exercises_txt = open('Exercises' + '.txt', "r", encoding='utf-8')  ##创建两个txt文件
    #        Answers_txt= open('Answers' + '.txt', "r", encoding='utf-8')
    #        question_text = question_path.read()
    #        answer_text = answer_path.read()
    #        q_spilt=re.split('\n',question_text)
    #        a_spilt=re.split('\n',answer_text)
    #        aqdict=dict(zip(q_spilt,a_spilt))
    def get_current_time():
        current_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
        return current_time

    def check_answer(file1, file2):
        try:
            question_path = open(file1, 'r', encoding='utf-8')
            question_text = question_path.read()
        except IOError:
            text.insert(END, "Error: 没有从该路径：{}\n找到问题文件/读取问题文件失败\n请重新填写正确路径\n\n".format(file1))
        else:
            try:
                answer_path = open(file2, 'r', encoding='utf-8')
                answer_text = answer_path.read()
            except IOError:
                text.insert(END, "Error: 没有从该路径：{}\n找到答案文件/读取答案文件失败\n请重新填写正确路径\n\n".format(file2))
            else:

                q_spilt = re.split('\n', question_text)
                a_spilt = re.split('\n', answer_text)
                if (len(q_spilt) == len(a_spilt)):
                    text.insert(END, "正在检查问题答案对错.....\n时间：" + get_current_time() + "\n问题文件:" + file1 +
                                "\n答案文件:" + file2 + "\n一共有" + str(len(q_spilt)) + "道题目\n\n")

                    aq_dict = dict(zip(q_spilt, a_spilt))

                    checkanswers = checkAnswers(aq_dict)
                    wrong_list = wrongAnswers(aq_dict)

                    for i in range(0, len(q_spilt)):
                        if (str(i + 1) in checkanswers):
                            text.insert(END, "四则运算题目" + str(i + 1) + "\n题目： " + str(q_spilt[i]) + "\n输入答案： " + str(
                                a_spilt[i]) + "\n结果： 答案正确\n\n")
                        else:
                            text.insert(END, "四则运算题目" + str(i + 1) + "\n题目： " + str(q_spilt[i]) + "\n输入答案： " + str(
                                a_spilt[i]) + "\n正确答案： " + str(operate(q_spilt[i])) + "\n结果： 答案错误\n\n")
                    correct_str = "Correct: " + str(len(checkanswers)) + '(' + ",".join(
                        str(i) for i in checkanswers) + ')'
                    wrong_str = "   Wrong: " + str(len(wrong_list)) + '(' + ",".join(str(i) for i in wrong_list) + ')'
                    text.insert(END, correct_str + wrong_str + "\n正确率：" + str(
                        round((len(q_spilt) - len(wrong_list)) / len(q_spilt),
                              2)) + "\n**************************************************\n\n")
                else:
                    text.insert(END, "Error: 题目答案个数不同：\n题目个数" + str(len(q_spilt)) + "\n答案个数：" + str(
                        len(a_spilt)) + "\n请重新填写正确的题目答案个数\n\n")

    def openset():
        topset = Tk()
        topset.geometry("400x140+300+150")
        topset.title("设置题目数量/范围")
        frmset = Frame(topset)
        frmset.pack(fill=X, padx=10, pady=3)
        toptap = Label(frmset, text='请分别输入生成题目个数与范围', font=("微软雅黑", 10), fg='red')
        toptap.pack(fill=X, padx=10, pady=3)
        set_entry_question = Entry(frmset, width=10, cursor='mouse')
        set_entry_question.insert(END, "请输入生成题目个数（默认10）")
        #    check_entry_question.insert(END, "请输入题目文件绝对路径")
        set_entry_question.pack(fill=X, padx=10, pady=3)
        set_entry_answer = Entry(frmset, width=10, cursor='mouse')
        set_entry_answer.insert(END, "请输入生成数范围（默认10）")
        #    check_entry_answer.insert(END, "请输入答案文件绝对路径")
        set_entry_answer.pack(fill=X, padx=10, pady=3)
        setbutton = Button(frmset, text="完成设置", bg="lightblue", width=20,
                           command=lambda: is_number(set_entry_question.get(), set_entry_answer.get()))
        setbutton.pack(fill=X, padx=10, pady=3)

        def is_number(uchar1, uchar2):
            if uchar1.isdigit():
                global n_parameter
                n_parameter = uchar1
                print(n_parameter)
            else:
                tkinter.messagebox.showerror('题目个数数据错误', '请填写整数数据')
            if uchar2.isdigit():
                global r_parameter
                r_parameter = uchar2
                print(r_parameter)
            else:
                tkinter.messagebox.showerror('范围数据错误', '请填写整数数据')

    # C:\Users\hp\Desktop\大三上\Exercises.txt
    # C:\Users\hp\Desktop\大三上\Answers.txt
    def opencheck():
        topcheck = Tk()
        topcheck.geometry("400x140+300+150")
        topcheck.title("检查")
        frmcheck = Frame(topcheck)
        frmcheck.pack(fill=X, padx=10, pady=3)
        toptap = Label(frmcheck, text='请分别输入题目与答案文件的绝对路径', font=("微软雅黑", 10), fg='red')
        toptap.pack(fill=X, padx=10, pady=3)
        check_entry_question = Entry(frmcheck, width=10, cursor='mouse')
        # check_entry_question.insert(END, r"C:\Users\hp\Desktop\大三上\question.txt")
        check_entry_question.insert(END, "请输入题目文件绝对路径")
        check_entry_question.pack(fill=X, padx=10, pady=3)
        check_entry_answer = Entry(frmcheck, width=10, cursor='mouse')
        # check_entry_answer.insert(END, r"C:\Users\hp\Desktop\大三上\answer.txt")
        check_entry_answer.insert(END, "请输入答案文件绝对路径")
        check_entry_answer.pack(fill=X, padx=10, pady=3)
        checkbutton = Button(frmcheck, text="验证答案", bg="lightblue", width=20,
                             command=lambda: check_answer(check_entry_question.get(), check_entry_answer.get()))
        checkbutton.pack(fill=X, padx=10, pady=3)

    def openimf(event):
        temp = lb.get(lb.curselection())
        top = Tk()
        top.geometry("600x340+200+150")
        xu = re.split('.  ', temp)
        top.title("四则运算题目： " + xu[0])

        frmtop = Frame(top)
        frmtop.pack(fill=X, padx=10, pady=3)
        toptap = Label(frmtop, text='题目:    ' + xu[1], font=("微软雅黑", 20), fg='blue')
        toptap.pack(fill=X, padx=10, pady=3)
        topentry = Entry(frmtop, width=10, cursor='mouse')
        topentry.pack(fill=X, padx=10, pady=3)
        topbuttonq = Button(frmtop, text="验证答案", bg="lightblue", width=20,
                            command=lambda: toptext.insert(END, lazy_sum()))
        topbuttonq.pack(fill=X, padx=10, pady=3)
        topbuttona = Button(frmtop, text="查看答案", bg="lightblue", width=20,
                            command=lambda: toptext.insert(END, "时间： " + get_current_time() + "\n"
                                                           + "操作： 验证答案\n" + "问题： " + xu[1] + "\n" + "答案： " +
                                                           allaqdict[xu[1]][0] + "\n\n"))
        topbuttona.pack(fill=X, padx=10, pady=3)
        tlabel = Label(frmtop, text='↓↓↓记录↓↓↓', font=("微软雅黑", 10), fg='red')
        tlabel.pack(fill=X, padx=10, pady=3)
        toptext = Text(frmtop, width=50, height=10)
        toptext.pack(fill=X, padx=10, pady=3)

        def is_Chinese(word):
            for ch in word:
                if ('\u4e00' <= ch <= '\u9fff'):
                    return False
                if (ch >= u'\u0041' and ch <= u'\u005a') or (ch >= u'\u0061' and ch <= u'\u007a'):
                    return False
            return True

        def lazy_sum():
            if (is_Chinese(topentry.get())):
                if topentry.get() == allaqdict[xu[1]][0]:
                    return "时间： " + get_current_time() + "\n" + "操作： 验证答案\n" + "问题： " + xu[
                        1] + "\n" + "输入答案： " + topentry.get() + "\n" + "结果： 答案正确" + "\n\n"
                else:
                    return "时间： " + get_current_time() + "\n" + "操作： 验证答案\n" + "问题： " + xu[
                        1] + "\n" + "输入答案： " + topentry.get() + "\n" + "结果： 答案错误" + "\n\n"
            else:
                return "时间： " + get_current_time() + "\n" + "操作： 验证答案\n" + "问题： " + xu[
                    1] + "\n" + "输入答案： " + topentry.get() + "\n" + "结果： 输入答案类型错误请重新输入" + "\n\n"

    def thread_it(func, *args):
        '''将函数打包进线程'''
        t = threading.Thread(target=func, args=args)
        t.setDaemon(True)
        t.start()

    master = Tk()
    master.geometry("1000x520+100+100")
    master.title("结对项目：自动生成小学四则运算题目")

    frmb = Frame(master)
    frmb.grid(row=0, column=0)
    frmbutton = Frame(master)
    frmbutton.grid(row=1, column=0)
    frmn = Frame(master)
    frmn.grid(row=0, column=1)
    frmrz = Frame(master)
    frmrz.grid(row=1, column=1)
    frmr = Frame(master)
    frmr.grid(row=2, column=1)
    frmc = Frame(master)
    frmc.grid(row=2, column=0)

    strlabel = StringVar()
    warnlabel = StringVar()
    warnlabel1 = StringVar()
    sblabel = Label(frmc, text='双击题目可进行答题/查看答案', justify=LEFT, font=("微软雅黑", 12), fg='red')
    sblabel.grid(row=0, column=1)
    blabel = Label(frmb, text='小学四则运算题目系统', justify=LEFT, font=("微软雅黑", 20), fg='blue')
    blabel.grid(row=0, column=0)
    nlabel = Label(frmn, relief=RIDGE, text='班级：信息安全2班    姓名：张家维 严为炜   学号：3118005433 3118005431')
    nlabel.grid(row=0, column=1)
    wlabel = Label(frmrz, textvariable=strlabel)
    wlabel.grid(row=0, column=4)
    tlabel = Label(frmrz, textvariable=warnlabel)
    tlabel.grid(row=1, column=4)
    warnlabel.set('')
    strlabel.set('生成题目： 已生成0个题目')

    thebutton1 = Button(frmbutton, text="开始生成题目", bg="lightblue", width=20,
                        command=lambda: thread_it(start(n_parameter, r_parameter)))
    thebutton1.grid(row=0, column=1)
    thebutton2 = Button(frmbutton, text="设置数量/范围", bg="lightblue", width=20, command=lambda: thread_it(openset()))
    thebutton2.grid(row=0, column=2, pady=5)
    thebutton3 = Button(frmbutton, text="检查", bg="lightblue", width=20, command=lambda: thread_it(opencheck()))
    thebutton3.grid(row=0, column=3, pady=5)

    sb = Scrollbar(frmc)
    sb.grid(row=1, column=2, sticky='ns')
    lb = Listbox(frmc, width=70, height=20, selectmode=SINGLE, yscrollcommand=sb.set)
    lb.grid(row=1, column=1)
    sb.config(command=lb.yview)
    lb.bind('<Double-Button-1>', openimf)

    text = Text(frmr, width=50, height=30)
    text.grid(row=2, column=4)

    master.mainloop()



