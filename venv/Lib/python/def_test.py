#导入模块部分
import time


#定义类部分
class Python():
    name = "LiLi"
    age = 18

    #定义函数
    def say(self):
        self.name = "Anlge"
        self.age = 21
        print("The name is : {0}".format(Python.name))
        print("The name is : {0}".format(Python.age))

class Name_t():
    name = "原有"
    _age = 20

Hello = Name_t()

print(Hello.name)
print(Hello._age)

