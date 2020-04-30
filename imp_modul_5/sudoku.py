#sebuah program untuk menyelesaikan game suodku
#setiap angka dalam satu baris harus berbeda
#setiap angka dalam satu kolom harus berbeda
#setiap angka dalam satu blok harus berbeda
#satu blok berukuran 3x3 nilai


from pyswip.prolog import Prolog #import libarary pyswip
from pyswip.easy import *


_ = 0 #deklarasi _=0
puzzle1 = [
            [_,6,_,1,_,4,_,5,_],
            [_,_,8,3,_,5,6,_,_],
            [2,_,_,_,_,_,_,_,1],
            [8,_,_,4,_,7,_,_,6],
            [_,_,6,_,_,_,3,_,_],
            [7,_,_,9,_,1,_,_,4],
            [5,_,_,_,_,_,_,_,2],
            [_,_,7,2,_,6,9,_,_],
            [_,4,_,5,_,8,_,7,_]
            ]


puzzle2 = [
            [_,_,1,_,8,_,6,_,4],
            [_,3,7,6,_,_,_,_,_],
            [5,_,_,_,_,_,_,_,_],
            [_,_,_,_,_,5,_,_,_],
            [_,_,6,_,1,_,8,_,_],
            [_,_,_,4,_,_,_,_,_],
            [_,_,_,_,_,_,_,_,3],
            [_,_,_,_,_,7,5,2,_],
            [8,_,2,_,9,_,7,_,_]
          ]


def pretty_print(table):
    print("".join(["/---", "----"*8, "\\"])) #membuat batas atas
    for row in table:
        print("".join(["|", "|".join(" %s " % (i or " ") for i in row), "|"])) #menampilkan setiap nilai pada soal dengan dibatasi |
    print("".join(["\\---", "----"*8, "/"])) #membuat batas bawah


def solve(problem): #definisi fungsi solve
    prolog.consult("prolog_file/sudoku.pl") #membuka file sudoku.pl
    p = str(problem).replace("0", "_") #mengganti angka 0 dan _ pada soal dengan jawaban
    result = list(prolog.query("L=%s,sudoku(L)" % p, maxresult=1)) 
    if result:  #membuat perulangan
        result = result[0] 
        return result["L"]
    else:
        return False


def main():
    puzzle = puzzle1 #memanggil puzzle pertama
    print("-- PUZZLE --") #menampilkan tulisan
    pretty_print(puzzle) #untuk menampilkan soal
    print
    print(" -- SOLUTION --") #menampilkan tulisan
    solution = solve(puzzle) #memanggil fungsi solve
    if solution:
        pretty_print(solution) #untuk menampilkan solusi atas soal
    else:
        print("This puzzle has no solutions [is it valid?]") #jika soal tidak dapat diselesaikan


if __name__ == "__main__":
    prolog = Prolog()
    main()
