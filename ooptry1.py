class Student(object):
    
    # __init__是一个特殊方法用于在创建对象时进行初始化操作
    # 通过这个方法我们可以为学生对象绑定name和age两个属性
    def __init__(self, name1, age1):
        self.name = name1
        self.age = age1

    def study(self, course_name1):
        print('%s正在学习%s.' % (self.name, course_name1))

    # PEP 8要求标识符的名字用全小写多个单词用下划线连接
    # 但是部分程序员和公司更倾向于使用驼峰命名法(驼峰标识)
    def watch_movie(self):
        if self.age < 18:
            print('%s只能观看《熊出没》.' % self.name)
        else:
            print('%s正在观看岛国爱情大电影.' % self.name)

def main():
    stu1=Student("cute plmm",20)
    stu1.watch_movie()
    

if __name__ == '__main__':
    main()
    