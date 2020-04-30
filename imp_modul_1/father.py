#  import modul pyswip
from pyswip import *

# fungsi main
def main():
    p = Prolog()

    # deklarasi predikat
    # maksud dari Functor dengan parameter ("father",2) adalah predikat father memiliki/membutuhkan
    # 2 argumen. untuk implentasinya berada di code selanjutnya
    father = Functor("father", 2)
    mother = Functor("mther", 2)
    assertz = Functor("assertz", 1)

    call(assertz(father("john", "mich")))
    call(assertz(father("john", "gina")))
    call(assertz(father("hank", "cloe")))
    call(assertz(mother("jane", "mich")))
    call(assertz(mother("jane", "gina")))

    # p.assertz("father(john,mich)")
    # p.assertz("father(john,gina)")
    # p.assertz("mother(jane,mich)")

    X = Variable(); Y = Variable(); Z = Variable()

    listing = Functor("listing", 1)
    call(listing(father))

    #print list(p.query("listing(father))"))

    q = Query(father("john",Y))
    while q.nextSolution():
        print (Y.value, Z.value)
        #print X.value, "is the father of", Y.value
        #print Z.value, "is the mother of", Y.value
    q.closeQuery()    # Newer versions of SWI-Prolog do not allow nested queries

    print("\nQuery with strings\n")
    for s in p.query("father(john,Y),mother(Z,Y)"):
        #print s["X"], "is the father of", s["Y"]
        #print s["Z"], "is the mother of", s["Y"]
        print (s["Y"], s["Z"])

    #print "running the query again"
    #q = Query(father(X, Y))
    #while q.nextSolution():
    #    print X.value, "is the father of", Y.value


if __name__ == "__main__":
    main()


