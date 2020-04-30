#  import modul pyswip

'''File ini tidak menggunakan file prolog external karena menggunakan package pyswip
yang telah menyediakan dan menjadi penghubung antara pyhton dengan bahasa prolog'''
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

    '''Definisi Call : meta-predikat yang memungkinkan argumen
       tunggal untuk dipanggil / dipanggil sebagai tujuan.'''

    '''Definisi assertz : menambahkan fakta setelah aturan atau fakta lain
       dengan functor yang sama.Ketika lebih dari satu aturan / fakta dengan
       functor yang sama hadir dalam database
    '''

    # deklarasi Fakta
    # call(assertz(father("Barok", "Atsumu")))
    # call(assertz(father("Barok", "Miya")))
    # call(assertz(father("Kagami", "Shishio")))
    # call(assertz(mother("Yachi", "Ishi")))
    # call(assertz(mother("Yachi", "Miya")))

    p.assertz("father(barok,atsumu)")
    p.assertz("father(kagami, miya)")
    p.assertz("father(kagami, shihio)")
    p.assertz("mother(yachi, atsumu)")
    p.assertz("mother(yachi, miya)")

    # deklarasi Variabel
    X = Variable();
    Y = Variable();
    Z = Variable();

    # memanggil sejumlah fakta dengan 1 parameter yaitu ayah

    # listing = Functor("listing", 1)
    # call(listing(father))
    print("Query dengan aturan yang didapat dari aturan fakta yang ditentukan")
    q = Query(father("barok",Y), mother(Z,Y))
    while q.nextSolution():
        print(" -","barok", "adalah ayah" ,Y.value)
        print(" -",Z.value, "adalah ibu" ,Y.value)
    q.closeQuery()

    print("\n")

    print("Query dengan aturan yang didapat dari aturan fakta secara keseluruhan")
    for s in p.query("father(X,Y),mother(Z,Y)"):
        print(" -",s["X"], "adalah ayah dari", s["Y"])
        print(" -",s["Z"], "adalah ibu dari", s["Y"])


    print("\n")

    print("Menjalankan dengan query berdasarkan predikat tanpa mememperhatikan siapa objeknya")
    q = Query(father(X, Y))
    while q.nextSolution():
       print(" -",X.value, "Ayah dari", Y.value)


if __name__ == "__main__":
    main()


