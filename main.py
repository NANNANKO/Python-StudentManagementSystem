import os
from student import Student
from data import Data


menu = """

=================================================

              学生成绩管理系统-功能目录
                1、浏览学生成绩
                2、按学号查找学生
                3、按成绩排序
                4、按年龄排序
                5、添加学生信息
                6、删除学生信息
                7、修改学生信息
                9、保存学生信息到文件
                0、退出不保存

=================================================
由王旭楠、肖淇颖、曾子洋制作

"""

print(menu)
tip = '输入功能数字进行下一步操作：'
choice = ''

b = Data('2017')

os.system('cls')


while True:
    choice = input(tip)
    os.system('cls')
    print(menu)
    if choice == '0':
        print('数据已保存在student.txt并退出')
        break
    elif choice == '1':
        b.ShowStudent()
    elif choice == '2':
        id = int(input('请输入想要查询学生的学号：'))
        s = b.FindStudent(id)
        if s is None:
            print('文件中没有这个学号的学生')
        else:
            print(s)
    elif choice == '3':
        b.SortByScore()
        b.ShowStudent()
    elif choice == '4':
        b.SortByAge()
        b.ShowStudent()
    elif choice == '5':
        print('请输入学生的个人信息：')
        id = int(input('学号：'))
        name = input('姓名：')
        score = int(input('成绩：'))
        age = int(input('年龄：'))
        student = Student(id, name, score, age)
        r = b.AddStudent(student)
        print(r)
    elif choice == '6':
        id = int(input('请输入需要删除学生的学号：'))
        r = b.DeleteStudent(id)
        print(r)

    elif choice == '7':
        id = int(input('请输入需要修改学生的学号：'))
        r = b.UpdateStudent(id)
        print(r)

    elif choice == '9':
        b.SaveData()
        print('保存信息到student.txt成功！')
    else:
        print('输入的数字指令有误！')
