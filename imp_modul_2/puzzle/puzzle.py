
#sebuah program untuk menyelesaikan game puzzle yang terdiri dari 8 angka
#dalam 1 baris atau garis (3 angka), jumlah angka harus 6
#dalam satu kotak keseluruhan (8 angka), jumlah angka harus 15



from pyswip.prolog import Prolog                #import library pyswip



def main():
    prolog = Prolog()
    prolog.consult("prolog_file/puzzle1.pl")    #membuka file prolog puzzle.pl
    for soln in prolog.query("solve(B)."):      #menjalankan predikat solve seperti pada file prolog

        B = soln["B"]
        # [NW,N,NE,W,E,SW,S,SE]
        print("%d %d %d" % tuple(B[:3]))		#mencetak angka pada papan
        print("%d   %d"   % tuple(B[3:5]))
        print("%d %d %d" % tuple(B[5:]))

        cont = input("Press 'n' to finish: ")
        if cont.lower() == "n": break			#jika ditekan n, program selesai


if __name__ == "__main__":
    main()
()
