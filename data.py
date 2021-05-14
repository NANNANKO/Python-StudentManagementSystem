from student import Student


class Data:
    def __init__(self, name):
        self.name = name
        self.students = []
        self.LoadData()

    def LoadData(self):
        with open('student.txt', 'r')as f:
            for line in f:
                d = line.split()
                self.students.append(Student(int(d[0]), d[1], int(d[2]), int(d[3])))

    def ShowStudent(self):
        print(Student.get_header())
        for s in self.students:
            print(s)

    def AddStudent(self, student):
        if student in self.students:
            return '此学生已存在于文件student.txt'
        else:
            self.students.append(student)
            return '添加成功'

    def StudentIndex(self, id):
        s = Student(id, '', 0, 0)
        if s not in self.students:
            return None
        else:
            return self.students.index(s)

    def FindStudent(self, id):
        i = self.StudentIndex(id)
        if i is None:
            return None
        else:
            return self.students[i]

    def DeleteStudent(self, id):
        i = self.StudentIndex(id)
        if i is None:
            r = '没有学号为{0: d}'.format(id)
        else:
            del self.students[i]
            r = '删除学生信息成功'
        return r

    def UpdateStudent(self, id):
        s = self.find_student(id)
        if s is None:
            return '没有学号为{0：d}的学生'.format(id)
        else:
            print(s)
            print('请输入新的值，直接回车为取消修改！')
            name_str = input('姓名：')
            score_str = input('分数：')
            age_str = input('年龄：')
            s.name = name_str if len(name_str) > 0 else s.name
            s.name = int(score_str) if len(score_str) > 0 else s.score
            s.name = int(age_str) if len(age_str) > 0 else s.age
            return '修改学生信息成功'

    def SaveData(self):
        with open('student.txt', 'w', encoding='GBK') as f:
            for s in self.students:
                r = str.format('{0:d} {1:s} {2:d} {3:d}\n', s.id, s.name, s.score, s.age)
                f.write(r)

    def SortByScore(self, reverse=False):
        self.students.sort(key=lambda x: x.score, reverse=reverse)

    def SortByAge(self, reverse=False):
            self.students.sort(key=lambda x: x.age, reverse=reverse)