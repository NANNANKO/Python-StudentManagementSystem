class Student:
    def __init__(self, id, name, score, age):
        self.id = id
        self.name = name
        self.__score = score
        self.__age = age

    @property
    def score(self):
        return self.__score

    @score.setter
    def score(self, score):
        self.__score = score if 0 <= score <= 100 else 0

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):
        self.__age = age if 0 <= age <= 100 else 0

    def __str__(self):
        s = str.format('{0:>4d}{1:　>4s}{2:>8d}{3:>8d}', self.id, self.name, self.score, self.age)
        return s

    @staticmethod
    def get_header():
        return '{0:>2s}{1:　>4s}{2: >4s}{3:　>4s}'.format('学号', '姓名', '分数', '年龄')

    def __eq__(self, other):
        return self.id == other.id

    def __gt__(self, other):
        return self.id > other.id