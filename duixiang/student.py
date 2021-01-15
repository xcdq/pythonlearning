from people import People


class Student(People):
    # sum = 0

    # def __init__(self, name, age):
    #     self.name = name
    #     self.age = age
    #     self.__class__.sum += 1

    def do_homework(self):
        print("do homework")


stu1 = Student('aaa', 18)
print(stu1.name)
print(stu1.age)
print(stu1.sum)
print(Student.sum)
stu1.get_name()
