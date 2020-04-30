#import library pyswip
from pyswip.prolog import Prolog

#pyswip telah menyediakan dan telah menghubungkan python dengan bahasa prolog,
#sehingga tidak diperlukan file prolog eksternal

#fungsi utama
def main():
    prolog = Prolog()
    
    #membuka file coins.pl
    prolog.consult("prolog_file/coins.pl")
    
    #mendeklarasi nilai count dan total
    #menginputkan nilai count dan nilai total berupa angka
    count = int(input("Berapa jumlah koin(default: 100)? ") or 100)
    total = int(input("Jumlah target total (default: 500)? ") or 500)
    
    #melakukan perulangan dengan menampilkan nilai yang ada di dalam list
    #enumerate berfungsi untuk mengembalikan sebuah objek iterable yang setiap itemnya memiliki indeks
    #memanggil fungsi coins pada prolog
    for i, soln in enumerate(prolog.query("coins(S, %d, %d)." % (count,total))):
        # [1,5,10,50,100]
        S = zip(soln["S"], [1, 5, 10, 50, 100])
        print(i), #cetak nilai
        
        #melakukan perulangan untuk menampilkan angka perkalian
        for c, v in S:
            print("%dx%d" % (c,v)),  #cetak perkalian
        print  #cetak hasil perulangan
        
    #fungsi list yaitu mengembalikan list berisi anggota-anggota dari objek yang menjadi argumennya
    #jika argumennya kosong, maka fungsi ini akan mengembalikan list kosong
    #jika argumennya berisikan data, maka yang digunakan adalah data-data yang digunakan dari list tersebut
    #hasil akhirnya akan menampilkan perhitungan perkalian dari jumlah nilai yang diinputkan
    list(prolog.query("coins(S, %d, %d)." % (count,total)))


if __name__ == "__main__":
    main()
