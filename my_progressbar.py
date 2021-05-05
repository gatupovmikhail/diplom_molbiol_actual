import time
class Progressbar():
    def __init__(self,step,full):
        self.ind = 0    #   счетчик
        self.step = step    # в %
        self.full = full    # всего итераций
        self.perc = 0   # % на предыдущей итерации
        self.nstars = 0 # число звезд
        self.nall = 100//step #  - всего делений

    def next(self):
        self.ind += 1
        if self.ind/self.full >= self.perc:
            self.perc  = self.perc + self.step/100
            self.nstars += 1

        #print('Вот это прогресс бар')
        print('\r',end='')
        print('['+ '#'*self.nstars + ' '*(self.nall-self.nstars) + ']' + str(int(self.perc*100)) + '%',end=' ')

    print('Вот это прогресс бар')

#bar = Progressbar(5,135)
#for i in range(135):
    #bar.next()
    #time.sleep(0.1)
