def arrondir():
    a = int (input ("valeur"))
    a = a / 200
    a = int (a)
    print(a)
    arrondir()
arrondir()