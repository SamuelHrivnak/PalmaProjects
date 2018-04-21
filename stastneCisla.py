'''
Verzia riesenia ktora pracuje zo stringom na vstupe ... ziaci to casto takto robia ze nedefinuju metodu
so stupnym parametrom, ale pytaju vstup z klavesnice, preto aj taketo spravne riesenie. // nenapadli mi lepse nazvy premennych, skuste
porozmyslat ako presne by to bolo treba nazvat
'''
def jeStastneCisloString():
    vstup = input()
    while True:
        cislo = 0
        for elementCisla in vstup:
            cislo += (int(elementCisla) ** 2)
        vstup = str(cislo)
        if len(vstup) == 1:
            if int(vstup) == 1:
                return True
            else:
                return False
            break
'''
riesenie pristupom oddelovanie cifier pomocou modula a nasledneho delenia
'''

def  jeStastneInt(cislo):
    while cislo > 9:
        cislo = sucetMocnin(cislo)
    if cislo == 1 or cislo == 7:
        return True
    else:
        return False

def sucetMocnin(cislo):
    sucetMocnin = 0;
    while cislo > 0:
        zvysok = cislo % 10
        cislo = cislo // 10
        sucetMocnin =  sucetMocnin +(zvysok * zvysok)
    return sucetMocnin


print(sucetMocnin(218))
