# conda如何创建
- 提示符下：conda create -n oop python=3.6

- print(a.__mro__)  用来显示当前层级关系，如显示A类的父类及最顶父类

- property: 属性修饰符，可带参数（tget,tset,tdel,doc）
# 类的常用魔法方法

- 操作类
    - 返回一个类的属性
    print(Student.__dict__)
    - 返回一个类的名称
    print(Student.__name__)
    - 返回一个类的注释
    print(Student.__doc__)
    - 返回一个类的父类
    print(Student.__bases__)
    - 返回一个调用的方法，对象当做函数的时候触发
    print(Student.__call__)
    - 返回一个字符串，当对象被当做字符串使用的时候调用
    print(Student.__str__) || print(Student.__repr__) 类似
- 描述符
    - '__set__'
    - '__get__'
    - '__delete__'
- 属性操作相关
    - '__getattr__' :访问一个不存在的属性时触发
    



