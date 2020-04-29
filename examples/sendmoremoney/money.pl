
:- use_module(library('bounds')).

sendmore(Digits) :-
   Digits = [S,E,N,D,M,O,R,Y],     % Membuat variables
   Digits in 0..9,               % Mengasosiasi domains ke variables
   S #\= 0,                        % Constraint: S harus beda dari 0
   M #\= 0,
   all_different(Digits),           % semua elemen, nilainya harus berbeda
                1000*S + 100*E + 10*N + D     % constraints yang lain
              + 1000*M + 100*O + 10*R + E
   #= 10000*M + 1000*O + 100*N + 10*E + Y,
   label(Digits).               % mulai pencarian

