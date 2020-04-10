n = int(input("Enter the number of students: "))
data = {} # 用来存储数据的字典变量
Subjects = ('Physics', 'Maths', 'History') # 所有科目
try:
    for i in range(0, n):
        name = input('Enter the name of the student {}: '.format(i + 1)) # 获得学生名称
        marks = []
        for x in Subjects:
            marks.append(int(input('Enter marks of {}: '.format(x)))) # 获得每一科的分数
        data[name] = marks
    for x, y in data.items():
        total =  sum(y)
        print("{} 的总成绩是：{}".format(x, total))
        if total < 180:
            print(x, "的成绩不及格，很遗憾")
        else:
            print(x, "你的成绩很好，恭喜")
except ValueError:
    print('输入错误，分数只能为数字')
else:
    print('程序计算完成')
