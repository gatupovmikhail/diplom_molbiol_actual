import time


class Progressbar():
    def __init__(self, step, full, name='bar'):
        self.ind = 0    #   счетчик
        self.step = step    # в %
        self.full = full    # всего итераций
        self.perc = 0   # % на предыдущей итерации
        self.nstars = 0 # число звезд
        self.nall = 100//step #  - всего делений
        self.name = name
        self.end = 0

    def next(self):
        if self.ind <= self.full:
            self.ind += 1
        if self.ind/self.full >= self.perc and self.ind <= self.full:
            self.perc  = self.perc + self.step/100
            self.nstars += 1

        #print('Вот это прогресс бар')
        print('\r',end='')
        if self.ind <= self.full:
            print(self.name + ' ['+ '#'*self.nstars + ' '*(self.nall-self.nstars) + ']' + str(int(self.perc*100)) + '%',end=' ')
        else:
            if self.end == 0:
                print()
                self.end = 1

    print('Вот это прогресс бар')

#bar = Progressbar(5,135)
#for i in range(135):
    #bar.next()
    #time.sleep(0.1)
