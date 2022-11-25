
def szoveg():
    # Kérj be a felhasználótól egy szöveget.  Alakítsd nagybetűssé!
    szoveg1 = input(f"Kérlek adj meg egy szöveget és kiírom neked végig nagybetűvel!")

    print(szoveg1.upper())
    karakter_hossz(szoveg1)

def karakter_hossz(szoveg1):
    #Az előző szövegről döntsd el, hogy 10 karakternél hosszabb-e? Ha igen, akkor írd ki a hosszát!
    if 10 < len(szoveg1):
        print(f"A szöveged hossza: {len(szoveg1)}")


def betus_szo():
#Kérj be egy legalább 3 betűs szót a felhasználótól. A szavakat addig kérd be, amíg a hossza legalább 3!
    szo = input(f"Kérlek adj meg legalább 3 betűs szót")
    i = 0
    while 3 > len(szo):
        if len(szo) >= 3:
            print(f"De szép szót adtál meg!")
        else:
            print(input(f"Kérlek adj meg legalább 3 betűs szót"))
        i += 1


def a_betu():
#Kérj be a felhasználótól egy szöveget. Keresd meg benne az első "a" betűt.
    a_szoveg = input(f"Kérlek adj meg egy szöveget megmondom hanyadik betűje az első 'a' ! ")
    i = 0
    while i < len(a_szoveg) :
        if len(a_szoveg) == "a":
            print(f"A szövegedben a {i+1}.betű az első 'a'!")
        i += 1

def db_a():
#Hány "a" betű van a bekért szövegben?
    db_szoveg = input(f"Kérlek adj meg egy szöveget és megmondom,hány db 'a' betű található benne!")
    i = 0
    db = 0
    while i < len(db_szoveg):
        if db_szoveg[i] == "a":
            db += 1
        i += 1
    print(f"{db}db 'a' betű található a szövegben!")

def mennyi_db():
    #Írd ki, hogy a szöveg egyes betűi hányszor szerepelnek a szövegben?
    from collections import Counter
    db_szoveg = input(f"Kérlek adj meg egy szöveget és megmondom,hány db és milyen karakter található benne!")
    text = Counter(db_szoveg)
    print(text)

def jel():
#Addig kérj be neveket a felhasználótól, amíg @ jelet nem üt le.
#A szöveget alakítsd át úgy, hogy a kezdőbetűje mindig nagybetű legyen, a többi kicsi.
#(szövegkezelő fvények a w3-on) Tárold a neveket egy listában.
    nev = ''
    i = 0
    nevek = []
    while nev != "@":
        nev = input(f"Kérlek adj meg egy nevet!")
        if nevek != "@":
            nevek.append(nev.capitalize())
        elif nevek == "@":
            print(f"Ezeket a neveket adtad meg : {nevek} ")

#Generálj annyi véletlen számot [1, 100] között, ahány nevet bekértél.
# A számok az adott nevű ember korát reprezentálják.
# Tárold el a számokat "kor" nevezetű listában.
    import random
    kor = []
    i = 0
    while i < len(nevek)-1:
        vel = int(random.random() * 100) + 1
        if vel not in kor:
            kor.append(vel)
            i += 1
    print(f"A random korok : {kor}")

#Írd ki a a legidősebb ember nevét!
    i = 0
    max = kor[0]
    idos = str(nevek[i])
    while i < len(kor):
        if kor[i] > max:
            max = kor[i]
            idos = nevek[i]
        i += 1
    print(f"A legidősebb ember:" ,idos )
