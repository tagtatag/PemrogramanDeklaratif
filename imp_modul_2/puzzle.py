
from pyswip.prolog import Prolog



def main():
    prolog = Prolog()
    prolog.consult("prolog_file/puzzle1.pl")
    for soln in prolog.query("solve(B)."):
        
        B = soln["B"]
        # [NW,N,NE,W,E,SW,S,SE]
        print("%d %d %d" % tuple(B[:3]))
        print("%d   %d"   % tuple(B[3:5]))
        print("%d %d %d" % tuple(B[5:]))

        cont = input("Press 'n' to finish: ")
        if cont.lower() == "n": break


if __name__ == "__main__":
    main()
()
