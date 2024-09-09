class Horse:

    def __init__(self, name, sound, x_distance):
        self.name = name
        self.sound = sound
        self.x_distance = x_distance

    sound = 'Frrr'
    x_distance = 0

    def run(self, dx):
        self.x_distance += dx
        return self.x_distance

class Eagle:

    def __init__(self, name, sound, y_distance):
        self.name = name
        self.sound = sound
        self.y_distance = y_distance

    sound = 'I train, eat, sleep, and repeat'
    y_distance = 0

    def fly(self, dy):
        self.y_distance += dy


class Pegasus(Horse, Eagle):

    def __init__(self, name):
        self.name = name

    def move(self, dx, dy):
        super().run(dx)
        super().fly(dy)

    def get_pos(self):
        return (self.x_distance, self.y_distance)

    def voice(self):
        #Eagle.sound
        print(self.sound)


p1 = Pegasus('Peg1')
p2 = Pegasus('Peg2')

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
