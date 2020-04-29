:- use_module(library('bounds')).

solusi(Papan) :-
	Papan = [NW,N,NE,W,E,SW,S,SE],
	Papan in 0..12,
	sum(Papan, #=, 15),
	NW + N + NE #= 6,
	NE + E + SE #= 6,
	NW + W + SW #= 6,
	SW + S + SE #= 6,

	label(Papan).
