# -*- coding: utf-8 -*-


# pyswip -- Python SWI-Prolog bridge
# Copyright (c) 2007-2012 Yüce Tekol
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.


# 100 coins must sum to $5.00


from pyswip.prolog import Prolog   #import library pyswip


def main():
    prolog = Prolog()
    prolog.consult("prolog_file/coins.pl")     #membuka file coins.pl
    count = int(input("Berapa jumlah koin(default: 100)? ") or 100)     #menginputkan nilai count
    total = int(input("Jumlah target total (default: 500)? ") or 500)   #menginputkan nilai total
    #melakukan perulangan dengan menampilkan nilai yang ada di dalam list
    for i, soln in enumerate(prolog.query("coins(S, %d, %d)." % (count,total))):
        # [1,5,10,50,100]
        S = zip(soln["S"], [1, 5, 10, 50, 100])
        print(i),
        for c, v in S:
            print("%dx%d" % (c,v)),    #menampilkan angka perkalian
        print
    list(prolog.query("coins(S, %d, %d)." % (count,total)))   #menampilkan seluruh list


if __name__ == "__main__":
    main()
