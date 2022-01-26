# 多重繼承
class Employee:
    def __init__(self, title):
        self.title = title
    def __str__(self):
        return "Employee's title: %s " % (self.title)

class Computer:
    def __init__(self, cpu_speed):
        self.cpu_speed = cpu_speed
    def __str__(self):
        return "Computer's speed: %.1f Ghz " % (self.cpu_speed)

class Robot(Employee, Computer):
    def __init__(self, title, cpu_speed, name):
        Employee.__init__(self, title)
        Computer.__init__(self, cpu_speed)
        self.name = name
    def __str__(self):
        return Employee.__str__(self) + Computer.__str__(self) + 'name: %s' % self.name

if __name__ == '__main__':
    robot = Robot('保全', 3.0, '春麗')
    print(robot)