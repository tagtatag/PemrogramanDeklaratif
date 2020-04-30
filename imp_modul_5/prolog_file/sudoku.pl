
% Public domain code.

:- use_module(library(bounds)).

%Pss adalah daftar yang mewakili papan permainan

sudoku(Pss) :- 
    flatten(Pss, Ps),
    Ps in 1..9, %inisialisasi angka 1 sampai 9
    maplist(all_different, Pss), %semua_elemen_harus_berbeda_nilainya
    Pss = [R1,R2,R3,R4,R5,R6,R7,R8,R9], %mewakili setiap nilai
    columns(R1, R2, R3, R4, R5, R6, R7, R8, R9), %kolom
    blocks(R1, R2, R3), blocks(R4, R5, R6), blocks(R7, R8, R9), %inisialisasi 9 blok 
    label(Ps).

columns([], [], [], [], [], [], [], [], []). %deklarasi kolom
columns([A|As],[B|Bs],[C|Cs],[D|Ds],[E|Es],[F|Fs],[G|Gs],[H|Hs],[I|Is]) :- %deklarasi nilai kolom
    all_different([A,B,C,D,E,F,G,H,I]), %membuat nilai setiap kolom berbeda dalam satu baris
    columns(As, Bs, Cs, Ds, Es, Fs, Gs, Hs, Is).

blocks([], [], []).
blocks([X1,X2,X3|R1], [X4,X5,X6|R2], [X7,X8,X9|R3]) :- %deklarasi blok
    all_different([X1,X2,X3,X4,X5,X6,X7,X8,X9]), %membuat nilai setiap blok berbeda 
    blocks(R1, R2, R3).
