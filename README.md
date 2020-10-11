=================
|  这个作业属于哪个课程   | [软件工程](https://edu.cnblogs.com/campus/gdgy/informationsecurity1812/)  |
| :----:  | :----:  |
| 作业要求  | [作业要求](https://edu.cnblogs.com/campus/gdgy/informationsecurity1812/homework/11157) |
| Github  | [Github链接](https://github.com/Zzjw527/Four-Arithmetic-problem-generator) |
| 小队成员  | 3118005433 张家维、 3118005431 严为炜 |
| 这个作业的目标  | 熟悉结对编程，实现自动生成小学四则运算题目程序，对给定的题目文件和答案文件，判定答案中的对错并进行数量统计 |








# 核心功能实现
#### 1. 生成题目
##### 实现思路：
   * 随机生成参数列表和运算符列表

   * 判断算式是否存在括号

     ​		if 存在不括号：

     ​				 返回获取到的无括号算式 

     ​		else：

     ​				返回获取到的括号算式 

   * 算式存在括号

     * 括号数为1时

        利用 **random.randint(0, len(op_list) - 1)**来决定左括号的位置
        利用 **random.randint(left_bracket_index + 1, len(parameter_list) - 1)**来决定右括号的位置

     * 括号数为2时<br/>

       随机获取括号类型<br/>

       if 括号类型为并列：<br/>

       ​		      &emsp; 循环获取参数列表和运算符列表获取到算式时，在相应的的位置插入括号，即：( A +B ) + ( C + D )<br/>

       else 括号类型为嵌套：<br/>

       ​		      &emsp; 先确定外层括号的位置，再利用递归，传递外层括号里的子字符串，从而确定内从括号，最终得到嵌套括号的算式
     
       <br/>

   ##### 流程图
![](https://img2020.cnblogs.com/blog/2148345/202010/2148345-20201010183938182-569711629.png)

##### 代码截图
 ![](https://img2020.cnblogs.com/blog/2148345/202010/2148345-20201011162453983-919523616.png)

  
#### 2. 计算

  ##### 实现思路   
     先处理算式，得到参数和操作符组成的列表，例如：' 1 + 2' 处理成 ['1', '2', '3']
     
     创建数字栈和操作符栈
     
     进行循环获取算式列表
     
     	如果是数字则压入数字栈
     
     	如果是操作符
     		while True 的循环
     
     			如果操作符栈为空，或者运算符为 '(' 时
     				入栈，break
     
     			如果当前操作符的优先级比栈顶操作符的优先级高
     				入栈，break
     
     			如果当前操作符为 ')'，且栈顶操作符为 '('
     				'(' 出栈，丢掉 ')'，break
     
     			如果当前操作符的优先级比栈顶操作符的优先级低
                 
     				获得数字栈最后两个元素、操作符栈最后一个元素，进行计算
                     
     				如果除数为零、被除数大于除数、结果为负数
                     	return Error
     
                     得到结果入栈
                     
     if 循环之后如果数字栈和操作符栈还有内容
     	while 直到操作符栈不为空：
     		计算
     		如果除数为零、被除数大于除数、结果为负数，return Error
             得到的结果入栈
     
     数字栈的元素就是计算得出的结果
     
##### 流程图
![](https://img2020.cnblogs.com/blog/2148345/202010/2148345-20201010185226976-920884180.png)
##### 代码截图
![](https://img2020.cnblogs.com/blog/2148345/202010/2148345-20201011160816352-1133719117.png)

#### 3. 多线程查询是否存在生成重复问题
##### 部分代码截图
![](https://img2020.cnblogs.com/blog/2148345/202010/2148345-20201011201802619-1400367466.png)

![](https://img2020.cnblogs.com/blog/2148345/202010/2148345-20201011201832266-111959654.png)





# 功能运行
## 命令行参数
python Myapp.py [args|args]
[args]
├─ -h --help # 输出帮助信息
├─ -n # 指定生成表达式数量，默认10
├─ -r # 指定生成表达式各个数字的取值范围，默认10
├─ -e # 需和-a参数共同使用进行批改，指定练习文件
├─ -a # 需和-e参数共同使用进行批改，指定答案文件
└─ -g # 开启GUI
### 命令行界面

#### 1. -h
![](https://img2020.cnblogs.com/blog/2148345/202010/2148345-20201011153212275-214946211.png)
#### 2. -r -n  (也可以只输入一个参数)
![](https://img2020.cnblogs.com/blog/2148345/202010/2148345-20201011153339152-1658756929.png)
#### 3. -e -a  (需要同时输入两个参数)
![](https://img2020.cnblogs.com/blog/2148345/202010/2148345-20201011153718833-777516553.png)


### GUI 界面(-g)
####采用了多线程的界面，任何操作不会阻塞其他操作，例如：可以在生成答案的同时批改作业
#### 1. 生成题目以及在线做题(有验证答案和查看答案两个功能)
![](https://img2020.cnblogs.com/blog/2148345/202010/2148345-20201011183335167-774104474.png)
#### 2. 设置题目数量以及范围（默认两个值都为10）
![](https://img2020.cnblogs.com/blog/2148345/202010/2148345-20201011183212462-1967032192.png)
#### 3. 检查题目答案（输入两个文件路径即可开始检查）
![](https://img2020.cnblogs.com/blog/2148345/202010/2148345-20201011183102022-1422717935.png)

# 单元测试
样例及输出结果
![](https://img2020.cnblogs.com/blog/2148345/202010/2148345-20201011200744885-1688445306.png)




# 异常处理
### 命令行输入参数错误
![](https://img2020.cnblogs.com/blog/2148345/202010/2148345-20201011154243169-1587955644.png)
![](https://img2020.cnblogs.com/blog/2148345/202010/2148345-20201011154502875-937433095.png)

### GUI输入错误
![](https://img2020.cnblogs.com/blog/2148345/202010/2148345-20201011154849493-37891663.png)
![](https://img2020.cnblogs.com/blog/2148345/202010/2148345-20201011154716495-888932290.png)
![](https://img2020.cnblogs.com/blog/2148345/202010/2148345-20201011154757374-483380229.png)


# 性能分析
### GUI界面性能
![](https://img2020.cnblogs.com/blog/2148345/202010/2148345-20201011124802696-242870432.png)
![](https://img2020.cnblogs.com/blog/2148345/202010/2148345-20201011124859575-1049711039.png)
### 生成题目
* 采用多线程生成题目，当生成题目过大时更换更为简便的判断生成重复问题函数
![](https://img2020.cnblogs.com/blog/2148345/202010/2148345-20201011125035349-772528477.png)
![](https://img2020.cnblogs.com/blog/2148345/202010/2148345-20201011125008645-1692008193.png)
### 检查答案对错
![](https://img2020.cnblogs.com/blog/2148345/202010/2148345-20201011125732435-1475705011.png)
![](https://img2020.cnblogs.com/blog/2148345/202010/2148345-20201011125754878-274818343.png)


# PSP表格
|  PSP2.1   | Personal Software Process Stages  |  预估耗时（分钟）  |  实际耗时（分钟）  |  
|  ----  | :----:  | :----:  | :----:  |  
|  Planning   | 计划  |  100  |  80  | 
|  · Estimate   | · 估计这个任务需要多少时间  |  100  |  80  |  
|  Development   | 开发  |  1680  |  2110  |  
|  · Analysis   | · 需求分析 (包括学习新技术)  | 40  |  30  |   
|  · Design Spec   | · 生成设计文档  |  100  |  70  |  
|  · Design Review   | · 需求分析 (包括学习新技术)  |  80  |  100  |  
|  · Coding Standard  | · 代码规范 (为目前的开发制定合适的规范)  |  60  |  90  |  
|  · Design   | · 具体设计  |  100  |  120  |  
|  · Coding   | · 具体编码  |  800  |  1050  |  
|  · Code Review   | · 代码复审  |  250  |  300 |  
|  · Test   | · 测试（自我测试，修改代码，提交修改）  |  250  |  350  |  
|  Reporting   | 报告  |  100  |  90 |  
|  · Test Repor   | · 测试报告  |  20  |  20  |  
|  · Size Measurement   | · 计算工作量  |  20  |  20  |  
|  · Postmortem & Process Improvement Plan   | · 事后总结, 并提出过程改进计划  |  60  |  50  |  
|     | · 合计  |  1880  |  2280  |
     

# 项目小结
### 严为炜：
#### 结对感受：
   * 这是我第一次接触结对编程，通过结对编程，我们能及时地对功能需求进行讨论，同时将每个功能模块化，各自实现相应的功能，提高了编程效率。

#### 对彼此的闪光点或建议
   * 效率高，对 IDE 的熟练使用大大提高了我们编程的效率。
&nbsp; 
   * 对问题有独特的见解，善于发现问题  

### 张家维：
#### 结对感受：
   * 第一次接触，受益良多。在结对编程时，我们将需求列出，根据难度不同从而安排开发流程，每个人根据自己能力特出点
不同而去做不同的需求，再通过交流约定我们每个人的接口，做到最大化的取长补短。最大的收获是提高了沟通能力，简化开发流程，提高效率
#### 对彼此的闪光点或建议
   * 思路清晰，对解决问题有多种思路
&nbsp; 
   * 代码规范，注释清晰  