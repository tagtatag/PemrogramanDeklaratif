#  import modul pyswip
from pyswip import *

# fungsi main
def main():
    p = Prolog()

    # deklarasi predikat
    # maksud dari Functor dengan parameter ("father",2) adalah predikat father memiliki/membutuhkan
    # 2 argumen. untuk implentasinya berada di code selanjutnya
    father = Functor("father", 2)
    mother = Functor("mother", 2)
    assertz = Functor("assertz", 1)

    '''Definisi Call : fungsi bawaan(meta-predikat) yang berfungsi untuk
     memanggil argumen tunggal sebagai goal/tujuan'''

    '''Definisi assertz : menambahkan fakta setelah aturan atau fakta lain
       dengan functor yang sama.Ketika lebih dari satu aturan / fakta dengan
       functor yang sama hadir dalam database
    '''

    # deklarasi Fakta
    call(assertz(father("john", "mich")))
    call(assertz(father("john", "gina")))
    call(assertz(father("hank", "cloe")))
    call(assertz(mother("jane", "mich")))
    call(assertz(mother("jane", "gina")))

    # p.assertz("father(john,mich)")
    # p.assertz("father(john,gina)")
    # p.assertz("mother(jane,mich)")

    # deklarasi Variabel
    X = Variable();
    Y = Variable();
    Z = Variable();

    # memanggil sejumlah fakta dengan 1 parameter yaitu ayah

    # listing = Functor("listing", 1)
    # call(listing(father))

    # deklarasi query/pertanyaan
    q = Query(father("john",Y))
    while q.nextSolution():
        # print (Y.value, Z.value)
        print(X.value, "is the father of", Y.value)
        print(Z.value, "is the mother of", Y.value)
        break
    q.closeQuery()    # Newer versions of SWI-Prolog do not allow nested queries

    print("\n")

    print("\nQuery dengan bentuk kalimat\n")
    for s in p.query("father(X,Y),mother(Z,Y), X = john"):
        print(s["X"], "adalah ayah dari", s["Y"])
        print(s["Z"], "adalah ibu dari", s["Y"])
        break
        # print(s["Y"], s["Z"])

    print("\n")

    print("Menjalankan dengan query")
    q = Query(father(X, Y))
    while q.nextSolution():
       print(X.value, "Ayah dari", Y.value)


if __name__ == "__main__":
    main()


