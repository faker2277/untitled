class Student():
    pass
paerl = Student()

class PythonStudent():
    name = None
    age = 18
    address = "china"
    no = "001"

    def dohomework(self):
        print("做作业")
        # self.name = "abc"
        # self.age = 20
        return None

jack = PythonStudent()
print(jack.dohomework())
print(jack.no)
