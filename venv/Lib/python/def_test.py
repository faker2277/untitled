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
        print("The name is : {0}".format(__class__.name))
        print("The name is : {0}".format(__class__.age))

Hello = Python()
print(Hello.say())

