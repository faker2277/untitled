class Peron():
    name = "网易"
    _age = 20
    gender = "male"

    def sleep(self):
        print("睡觉 ZZZ")
        return 'ok'

class Teacher(Peron):
    def MarkWork(self):
        print("写作业")
        return 'ok'

t = Teacher()
print(t._age)
print(Teacher.name)
print(Teacher._age)
print(t.MarkWork())
print(t.sleep())