
#   S E N D
#   M O R E
# + -------
# M O N E Y
#
# Jadi, nilai dari S, E, N, D, M, O, R, Y
# jika semua angkanya berbeda.


from pyswip import Prolog               #import library pyswip


letters = "S E N D M O R Y".split()
prolog = Prolog()
prolog.consult("prolog_file/money.pl")              #membuka file money.pl
for result in prolog.query("sendmore(X)"):
    r = result["X"]
    for i, letter in enumerate(letters):
        print(letter, "=", r[i])

print("That's all...")
