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
        return None

jack = PythonStudent()

print(jack.address)
print(jack.age)
print(jack.dohomework())

