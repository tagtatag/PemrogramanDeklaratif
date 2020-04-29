

#Kemungkinan dalam papan puzzle (8 kotak) dimana
#dalam satu baris/garis jumlah angkanya harus 6 dan
#total semua angka dari papan harus 15


from pyswip.prolog import Prolog     #import library pyswip


def main():
    prolog = Prolog()
    prolog.consult("puzzle.pl")            #membaca file prolog (puzzle.pl)
    for soln in prolog.query("solusi(B)."):
        #B = eval(soln["B"])
        B = soln["B"]
        # [NW,N,NE,W,E,SW,S,SE]
        print ("%d %d %d" % tuple(B[:3]))
        print ("%d   %d"   % tuple(B[3:5]))
        print ("%d %d %d" % tuple(B[5:]))
        
        cont = input("Tekan 'n' untuk selesai: ")
        if cont.lower() == "n": break

        
if __name__ == "__main__":
    main()
