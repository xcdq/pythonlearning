class Student():
    sum

    def do_homework(self):
        """
        docstring
        """
        print("homework")

    @classmethod
    def plus(cls):
        cls.sum += 1

    @staticmethod
    def do(a, b):
        print(a, b)


class Printer(stu):
    """
    docstring
    """

    def print_file(self):
        print("name:"+self.name)
        print("age:"+str(self.age))

# stu = Student()
# stu.print_file()
