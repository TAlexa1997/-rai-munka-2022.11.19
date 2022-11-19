
"""def szoveg():
    # Kérj be a felhasználótól egy szöveget.  Alakítsd nagybetűssé!
    szoveg1 = input(f"Kérlek adj meg egy szöveget és kiírom neked végig nagybetűvel!")

    print(szoveg1.upper())
    karakter_hossz(szoveg1)

def karakter_hossz(szoveg1):
    #Az előző szövegről döntsd el, hogy 10 karakternél hosszabb-e? Ha igen, akkor írd ki a hosszát!
    i = 0
    while i < len(szoveg1):
        if i >= 10:
            print(f"A szöveged hossza: {len(szoveg1)}")
        i += 1


def betus_szo():
#Kérj be egy legalább 3 betűs szót a felhasználótól. A szavakat addig kérd be, amíg a hossza legalább 3!
    szo = input(f"Kérlek adj meg legalább 3 betűs szót")
    i = 0
    while i < len(szo):
        if len(szo) >= 3:
            print(f"De szép szavat adtál meg!")
        else:
            print(input(f"Kérlek adj meg legalább 3 betűs szót"))
        i += 1
"""
def a_betu():
#Kérj be a felhasználótól egy szöveget. Keresd meg benne az első "a" betűt.
    a_szoveg = input(f"Kérlek adj meg egy szöveget megmondom hanyadik betűje az első 'a' ! ")
    i = 0
    a = 1
    while i < len(a_szoveg):
        if a_szoveg[i] != "a":
            a += 1
        i += 1

    print(f"A szövegedben {a+1}.betű az 'a'!")


def db_a():
#Hány "a" betű van a bekért szövegben?
    db_szoveg = input(f"Kérlek adj meg egy szöveget és megmondom,hány db 'a' betű található benne!")
    i = 0
    db = 0
    while i < len(db_szoveg):
        if db_szoveg[i] == "a":
            db += 1
        i += 1
    print(f"{db}db 'a' betű található a szövegben")

def mennyi_db():

#++ feketeöveseknek: Írd ki, hogy a szöveg egyes betűi hányszor szerepelnek a szövegben?

#Addig kérj be neveket a felhasználótól, amíg @ jelet nem üt le. A szöveget alakítsd át úgy, hogy a kezdőbetűje mindig nagybetű legyen, a többi kicsi. (szövegkezelő fvények a w3-on) Tárold a neveket egy listában.
#Generálj annyi véletlen számot [1, 100] között, ahány nevet bekértél. A számok az adott nevű ember korát reprezentálják. Tárold el a számokat "kor" nevezetű listában.
#Írd ki a a legidősebb ember nevét!