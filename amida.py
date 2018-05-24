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

        list = range(people-1)
        x_pos = random.choices(range(self.people-1), k=self.times-(self.people-1))
        x_pos.extend(list)
        random.shuffle(x_pos)

        #x_pos = random.choices(range(self.people-1), k=self.times)

        for i in range(self.times):
            self.draw_line(x_pos[i], i)

    def reset(self):
        for i in range(self.people-1):
            for j in range(self.times):
                self.lottery[j][i] = False


    def show(self):
        for i in self.lottery:
            print(i)


    def execute(self, pos):
        position = pos
        #self.show()

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

        return position



people = 5
times = 5 * 2

amida = Amida(people, times)
result = [0 for i in range(people)]


for j in range(people):
    for i in range(1000000):
        amida.draw_random_line()
        result[amida.execute(j)] += 1

        amida.reset()

    print(j)
    print(result)
    result = [0 for i in range(people)]

