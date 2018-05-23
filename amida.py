import random

class Amida:
    people = 0
    times = 0

    def __init__(self, p, t):
        self.people = p
        self.times = t
        self.lottery = [[False for i in range(p-1)] for j in range(t)]


    def draw_line(self, x, y):
        self.lottery[y][x] = True


    def draw_random_line(self):
        x_pos = random.choices(range(self.people-1), k=self.times)
        for i in range(self.times):
            self.draw_line(x_pos[i], i)


    def show(self):
        for i in self.lottery:
            print(i)


    def execute(self, pos):
        position = pos
        self.show()

        for i in self.lottery:

            if position == 0:
                if i[position]:
                    position += 1

            elif 0 < position and position < self.people-1:
                if i[position]:
                    position += 1
                elif i[position-1]:
                    position -= 1

            elif position == self.people-1:
                if i[position-1]:
                    position -= 1

        print(position)



amida = Amida(5, 5*2)

amida.draw_random_line()

amida.execute(0)


