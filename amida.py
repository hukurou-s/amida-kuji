class Amida:
    people = 0
    times = 0

    def __init__(self, p, t):
        self.people = p
        self.times = t
        self.lottery = [[False for i in range(p-1)] for j in range(t-1)]

    def draw_line(self, x, y):
        self.lottery[y][x] = True

    def execute(self):
        position = 0
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

    def show(self):
        for i in self.lottery:
            print(i)

amida = Amida(5, 5*2)

amida.draw_line(0,0)
amida.draw_line(1,1)
amida.draw_line(2,2)
amida.draw_line(3,3)
amida.draw_line(3,4)
amida.draw_line(2,5)

amida.execute()


