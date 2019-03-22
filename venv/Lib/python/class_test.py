class Peron():
    name = "网易"
    _age = 20
    __sitcte = 'x'
    gender = "male"

    def sleep(self):
        print("睡觉 ZZZ")
        return 'ok'

class Teacher(Peron):
    def MarkWork(self):
        #super().Peron()
        print("写作业")
        return 'ok'

class Cat():
    def __init__(self):
        print("阿斯蒂芬")


class A():
    def __init__(self):
        print("A")

class B(A):
    def __init__(self,name):
        print("B")
        print(name)
class C(B):
    pass

c = C('abc')
print(c)


t = Teacher()
print(t._age)
# print(t.__sitcte)
print(Teacher.name)
print(Teacher._age)
print(t.MarkWork())
print(t.sleep())
c = Cat()
print(c)
