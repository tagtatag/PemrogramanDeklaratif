
from pyswip import *


def main():
    p = Prolog()

    father = Functor("father", 2)
    mother = Functor("mother", 2)
    assertz = Functor("assertz", 1)


    p.assertz("father(john,mich)")
    p.assertz("father(john,gina)")
    p.assertz("mother(jane,mich)")

    X = Variable(); Y = Variable(); Z = Variable()

    listing = Functor("listing", 1)
    call(listing(father))


    q = Query(father("john",Y), mother(Z,Y))
    while q.nextSolution():
        print(Y.value, Z.value)

    q.closeQuery()

    print("\nQuery with strings\n")
    for s in p.query("father(john,Y),mother(Z,Y)"):

        print(s["Y"], s["Z"])


if __name__ == "__main__":
    main()


