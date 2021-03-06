#sebuah program yang digunakan untuk memindahkan urutan dari setiap step


from collections import deque                       #import library collections

from pyswip.prolog import Prolog                    #import library pyswip
from pyswip.easy import getList, registerForeign


class Notifier:                 #membuat class dengan nama notifier
    #pemanggilan fungsi
    def __init__(self, fun):    #mendeklarasikan variabel self, fun
        self.fun = fun          #mendeklrasikan fun. menngunakan kata self yang menunjukan bahwa fun merupaka milik class Tower

    def notify(self, t):        #membuat fungsi notify
        return not self.fun(t)           #return not self.fun(getList(t))
    notify.arity = 1


class Tower:            #membuat class dengan nama Tower

    #pemanggilan fungsi
    def __init__(self, N=3, interactive=False):    #mendeklarasikan variabel self, N=3, dan interactive=False
        """N adalah nomer dari disks
        """
        self.N = N                  #mendeklarasikan N menggunakan kata self yang menunjukkan bahwa N merupakan milik dari class Tower
        self.disks = dict(left=deque(range(N, 0, -1)), center=deque(), right=deque())
        self.started = False
        self.interactive = interactive
        self.step = 0                   #mendeklarasikan step

    def move(self, r):                  #membuat fungsi move
        if not self.started:
            self.step += 1              #mendeklarasikan step
            self.draw()
            self.started = True
        disks = self.disks
        disks[str(r[1])].append(disks[str(r[0])].pop())
        self.step += 1
        return self.draw()

    def draw(self):                     #membuat fungsi draw
        disks = self.disks
        print("\n Step", self.step)     #mencetak niali step dengan didahului kata self yang artinya memanggil dirinya sendiri kemudian memanggil step
        #menggunakan perulanagn for
        for i in range(self.N):
            n = self.N - i - 1
            print(" "),
            for pole in ["left", "center", "right"]:
                if len(disks[pole]) - n > 0:
                    print(disks[pole][n]),
                else:
                    print(" "),
            print
        print("-"*9)
        print(" ", "L", "C", "R")
        if self.interactive:
            cont = input("Press 'n' to finish: ")
            return cont.lower() == "n"      #digunakan untuk mengakhiri program


def main():             #digunakan untuk membuat fungsi main()
    N = 3               #pendeklarasian nilai N adalah 3
    INTERACTIVITY = True

    prolog = Prolog()
    tower = Tower(N, INTERACTIVITY)
    notifier = Notifier(tower.move)
    registerForeign(notifier.notify)
    prolog.consult("prolog_file/hanoi.pl")
    list(prolog.query("hanoi(%d)" % N))


if __name__ == "__main__":
    main()
