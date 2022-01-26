# 繼承
class Person:
    def __init__(self, name, age, sex) -> None:
        self.name = name
        self.age = age
        self.sex = sex

    def __str__(self) -> str:
        return "%s age: %d sex: %s" % (self.name, self.age, self.sex)

class Student(Person):
    def __init__(self, name, age, sex, number, grade):
        super().__init__(name, age, sex)
        self.number = number
        self.grade = grade

    def __str__(self):
        return super().__str__() + " number: %d grade: %s" % (self.number, self.grade)

if __name__ == '__main__':
    student = Student('John', 18, '男', 1, '大一')
    print(student.name, student.age, student.sex, student.number, student.grade)
    print(student)