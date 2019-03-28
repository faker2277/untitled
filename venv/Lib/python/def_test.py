class Student():
    # def __init__(self, name):
    #     self.name = name
    #
    # def __gt__(self, obj):
    #     print("哈哈，A 的值{0} 会比B 的值{1}大么！".format(self, obj))
    #     return self.name < obj.name
    # def __str__(self):
    #     return self.name

# p1 = Student("one")
# p2 = Student("two")
# print(p1 > p2)
#print(Student.__str__)
    '''
    这是一条注释
    '''
    name = 'ok'
    age = 16
    # def __getattr__(self, name):
    #     print("您所定义的属性未正确，请调整！谢谢！")
    def __init__(self):
        self.name = "sss"
        self.age = 11
    def fget(self):
        return self._name + '-卫浴'

    def fset(self,name):
        self._name = name.upper()

    def fdel(self):
        self._name = "No Name"
    def doc(self):
        pass

    name = property(fget, fset, fdel, "Is OK")
a = Student()
print(a.name)
# print(a.add)

# p1 = Student()
# p1.name = "toto-"
# print(p1.name)
# print(Student.__dict__)
# print(Student.__name__)
# print(Student.__doc__)
# print(Student.__bases__)