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


from pyswip import Prolog, Functor, Variable, Query


def main():
    prolog = Prolog()
    prolog.consult("kanankiri.pl")
    count = int(input("Berapa jumlahnya kiri? ") or 100)
    total = int(input("Berapa total semuanya? ") or 500)
    kanankiri = Functor("kanankiri", 3)
    S = Variable()
    q = Query(kanankiri(S, count, total))
    i = 0
    while q.nextSolution():
        ## [1,5,10,50,100]
        s = zip(S.value, [1, 5, 10, 50, 100])
        print(i),
        for c, v in s:
            print("%dx%d" % (c,v)),
        print()
        i += 1
    q.closeQuery()

    
if __name__ == "__main__":
    main()
