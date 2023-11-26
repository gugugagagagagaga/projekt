import random

def intro():
    print("Witaj w grze kosmicznej podróży!")
    print("Jesteś dowódcą statku kosmicznego, który przemierza odległe zakątki galaktyki.")
    print("Twoim celem jest dotarcie do odległej planety, unikając niebezpieczeństw i optymalizując zasoby.")
    print("Rozpoczynamy misję!")

def podróż_kosmiczna():
    dystans = 0
    paliwo = [100]
    jedzenie = [100]
    naprawy = [100]
    losowe_zdarzenia = ["Meteoryt", "Obcy statek", "Czarna dziura", "Niezbadana planeta"]

    def mapa(dystans):
        mapa_str = ""
        for i in range(500):
            if i == dystans[0]:
                mapa_str += "X"
            elif i == 500 - 1:
                mapa_str += "P"
            else:
                mapa_str += "-"
        print(mapa_str)

    def obsluga_zdarzenia(zdarzenie, paliwo, jedzenie, naprawy):
        print("\nNapotkałeś na:", zdarzenie)

        if zdarzenie == "Meteoryt":
            print("Twój statek ucierpiał, ale udało się przetrwać.")
            paliwo[0] -= random.randint(5, 15)
            naprawy[0] -= random.randint(10, 20)

        elif zdarzenie == "Obcy statek":
            print("Spotkałeś przyjazny obcy statek, który dostarczył ci dodatkowe zasoby.")
            paliwo[0] += random.randint(10, 20)
            jedzenie[0] += random.randint(10, 20)
            naprawy[0] += random.randint(5, 15)

        elif zdarzenie == "Czarna dziura":
            print("Twój statek wpadł w obszar czarnej dziury. Straciłeś część zasobów.")
            paliwo[0] -= random.randint(15, 25)
            jedzenie[0] -= random.randint(10, 15)
            naprawy[0] -= random.randint(5, 10)

        elif zdarzenie == "Niezbadana planeta":
            print("Odkryłeś niezbadaną planetę. Wylądowałeś, aby zbadać.")
            odkrywanie_planety(paliwo, jedzenie, naprawy)

    def odkrywanie_planety(paliwo, jedzenie, naprawy):
        print("Znajdujesz niezwykłe zasoby na powierzchni planety.")

        znaleziska = ["Nowe technologie", "Egzotyczne minerały", "Cenne artefakty"]
        znalezisko = random.choice(znaleziska)

        if znalezisko == "Nowe technologie":
            print("Odkryłeś nowe technologie, które poprawią wydajność twojego statku.")
            naprawy[0] += random.randint(10, 20)

        elif znalezisko == "Egzotyczne minerały":
            print("Zebrałeś egzotyczne minerały, które zwiększą ilość paliwa.")
            paliwo[0] += random.randint(15, 25)

        elif znalezisko == "Cenne artefakty":
            print("Znalezione cenne artefakty przynoszą dodatkowe jedzenie.")
            jedzenie[0] += random.randint(15, 25)

    while dystans < 500:
        print("\nDystans do celu:", dystans, "jednostek astronomicznych")
        print("Stan zasobów - Paliwo:", paliwo[0], "Jedzenie:", jedzenie[0], "Naprawy:", naprawy[0])

        decyzja = input("\nWybierz akcję: (1) Przyspiesz, (2) Zwolnij, (3) Sprawdź mapę, (4) Losowe zdarzenie: ")

        if decyzja == "1":
            przyspieszenie = random.randint(10, 20)
            dystans += przyspieszenie
            paliwo[0] -= random.randint(5, 10)
            jedzenie[0] -= random.randint(3, 8)
            naprawy[0] -= random.randint(1, 5)
            print("Przyspieszyłeś o", przyspieszenie, "jednostek astronomicznych!")

        elif decyzja == "2":
            zwolnienie = random.randint(5, 15)
            dystans += zwolnienie
            paliwo[0] -= random.randint(3, 7)
            jedzenie[0] -= random.randint(2, 6)
            naprawy[0] -= random.randint(1, 4)
            print("Zwolniłeś o", zwolnienie, "jednostek astronomicznych.")

        elif decyzja == "3":
            print("\nMapa galaktyki:")
            print("X - Twoja pozycja")
            print("P - Planeta celu")
            mapa(dystans)

        elif decyzja == "4":
            zdarzenie = random.choice(losowe_zdarzenia)
            obsluga_zdarzenia(zdarzenie, paliwo, jedzenie, naprawy)

        else:
            print("Nieprawidłowa decyzja. Spróbuj ponownie.")

        if paliwo[0] <= 0 or jedzenie[0] <= 0 or naprawy[0] <= 0:
            print("Twoje zasoby wyczerpały się. Koniec misji!")
            break

    if dystans >= 500:
        print("Gratulacje! Dotarłeś do planety celu.")

if __name__ == "__main__":
    intro()
    podróż_kosmiczna()

def Gra3():
    intro()
    podróż_kosmiczna()

if __name__ == "__main__":
    Gra3()
