class Horse:
    def __init__(self, name):
        self.name = name

    x_distance = 0
    sound = 'Frrr'

    def run(self, dx):
        self.x_distance += dx
        return self.x_distance

class Eagle:
    def __init__(self, name):
        self.name = name

    y_distance = 0
    sound = 'I train, eat, sleep, and repeat'

    def fly(self, dy):
        self.y_distance += dy


class Peagasus(Horse, Eagle):

    def move(self, dx, dy):
        super().run(dx)
        super().fly(dy)

    def get_pos(self):
        return (self.x_distance, self.y_distance)

    def voice(self):
        print(Eagle.sound)


p1 = Peagasus('Peg1')
p2 = Peagasus('Peg2')

print(p1.get_pos())
p1.move(10, 15)
print(p1.get_pos())
p1.move(-5, 20)
print(p1.get_pos())

p1.voice()

print(p2.get_pos())
p2.move(14, 18)
print(p2.get_pos())
p2.move(-12, 30)
print(p2.get_pos())

p2.voice()
