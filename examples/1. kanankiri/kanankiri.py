
from pyswip.prolog import Prolog  #import library pyswip


def main():
    prolog = Prolog()
    prolog.consult("kanankiri.pl")                          #membaca file prolog (kanankiri.pl)
    kiri = int(input("Berapa jumlahnya kiri? ") or 10)
    total = int(input("Berapa total semuanya? ") or 100)
    for i, soln in enumerate(prolog.query("kanankiri(S, %d, %d)." % (kiri,total))):

        S = zip(soln["S"], [1,5,10,50,100])
        print(i),
        for c, v in S:
            print("%dx%d" % (c, v))
        print()
    list(prolog.query("kanankiri(S, %d, %d)." % (kiri,total)))

    
if __name__ == "__main__":
    main()
