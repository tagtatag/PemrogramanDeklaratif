
% SEND + MORE = MONEY

:- use_module(library('bounds')).

sendmore(Digits) :-
   Digits = [S,E,N,D,M,O,R,Y],     % Membuat variables
   Digits in 0..9,               % mengasosiasi nilai 0 sampai 9 ke variables
   S #\= 0,                        % S harus tidak sama dengan 0
   M #\= 0,
   all_different(Digits),           % semua elemen harus berbeda nilainya
                1000*S + 100*E + 10*N + D     
              + 1000*M + 100*O + 10*R + E
   #= 10000*M + 1000*O + 100*N + 10*E + Y,
   label(Digits).               % Memulai pencarian

