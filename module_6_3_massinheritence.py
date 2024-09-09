class Horse:

    def __init__(self):
        # self.name = name
        # self.sound = sound
        # self.x_distance = x_distance
        pass

    sound = 'Frrr'
    x_distance = 0

    def run(self, dx):
        self.x_distance += dx
        return self.x_distance

class Eagle:

    def __init__(self):
        # self.name = name
        # self.sound = sound
        # self.y_distance = y_distance
        pass

    sound = 'I train, eat, sleep, and repeat'
    y_distance = 0

    def fly(self, dy):
        self.y_distance += dy


class Pegasus(Horse, Eagle):

    def __init__(self):
        Eagle.__init__(self)
        Horse.__init__(self)

    def move(self, dx, dy):
        self.run(dx)
        self.fly(dy)

    def get_pos(self):
        return (self.x_distance, self.y_distance)

    def voice(self):
        print(self.sound)


p1 = Pegasus()


print(p1.get_pos())
p1.move(10, 15)
print(p1.get_pos())
p1.move(-5, 20)
print(p1.get_pos())

p1.voice()

print(Pegasus.mro())
print(Horse.mro())
print(Eagle.mro())
