# 覆寫
class Bird:
    def move(self):
        print('我會飛')

class Penguin(Bird):
    def move(self):
        print('我不會飛但是我會游泳')

if __name__ == '__main__':
    bird = Bird()
    bird.move()
    penguin = Penguin()
    penguin.move()