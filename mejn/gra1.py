from random import randint, choice

def Gra1():
    name = input('Podaj imię swojego bohatera: ')
    life = 100
    mana = 100
    przywrocenie_czesci_hp = 1

    def zwykly_atak():
        return randint(3, 10)

    def fire_ball():
        nonlocal mana
        if mana < 10:
            print("-" * 40)
            print("Nie masz wystarczającej ilości many!")
            return 0
        mana -= 10
        return randint(13, 20)

    def silny_atak():
        nonlocal mana
        if mana < 10:
            print("-" * 40)
            print("Nie masz wystarczająco many :(  !")
            return 0
        mana -= 15
        return randint(17, 25)

    def przywrocenie_hp():
        nonlocal przywrocenie_czesci_hp, life
        if przywrocenie_czesci_hp < 1:
            print("Już wykorzystałeś uleczenie")
            return 0
        przywrocenie_czesci_hp -= 1
        life += randint(20, 100)
        return 0

    def poddaj_się():
        nonlocal life
        life -= 200
        return 0

    def wybierz_atak():
        print('a/A - Wykonaj Normalny Atak')
        print('b/B - Fire ball!')
        print('c/C - Uderz silnym atakiem')
        print('d/D - Przywróć sobie część życia')
        print('e/E - Poddaj się')
        co = input().upper()
        if co == 'A':
            return zwykly_atak()
        elif co == 'B':
            return fire_ball()
        elif co == 'C':
            return silny_atak()
        elif co == 'D':
            return przywrocenie_hp()
        elif co == 'E':
            return poddaj_się()
        else:
            print("Nie wybrano akcji")
            return 0

    def random_oponent():
        opponents = [
            ["Mały Goblin", 15, 3, 0],
            ["Nimfa Wodna", 10, 3, 0],
            ["Nimfa", 1, 3, 0],
            ["Goblin", 15, 3, 0],
            ["W miarę ciężki przeciwnik", 15, 15, 0],
            ["Toaletan", 15, 3, 0],
            ["Miay", 16, 3, 0],
            ["Szszczvn", 15, 3, 0],
            ["Ncxzcxzaa", 17, 2, 0],
            ["Szkieletor", 17, 3, 0],
            ["Njgagaaa", 18, 3, 0],
            ["Acxgagzcxzin", 15, 3, 0],
            ["ZcxzNaa", 17, 2, 0],
            ["Gin", 17, 3, 0],
            ["Nvzagja", 18, 3, 0]
        ]
        return choice(opponents)

    liczba_pokonanych_przeciwników = 0

    while life > 0:
        opponent = random_oponent()
        print("-" * 40)

        while opponent[1] > 0 and life > 0:
            print(f"{name} walczy teraz z {opponent[0]}")
            print(f"Przeciwnik ma {opponent[1]} HP i zadaje Ci {opponent[2]} obrażeń")

            life -= opponent[2]
            if life <= 0:
                break

            print(f"Masz {life} HP i {mana} many oraz pozostałe przywrócenie zdrowia {przywrocenie_czesci_hp}")
            atak = wybierz_atak()
            opponent[1] -= atak
            print(f"Zadałeś {atak} obrażeń")

        if opponent[1] <= 0:
            print('Zabiłeś przeciwnika!!!')
            liczba_pokonanych_przeciwników += 1

    print("-" * 40)
    print("KONIEC GRY!")
    print("-" * 40)
    print(f"ZABIŁEŚ {liczba_pokonanych_przeciwników} PRZECIWNIKÓW")
    print("-" * 40)
    if 15 < liczba_pokonanych_przeciwników < 9:
        print("Średnio ci poszło, może następnym razem będzie lepiej")
        print("-" * 40)
    elif liczba_pokonanych_przeciwników >= 15:
        print("Dobrze ci poszło")
        print("-" * 40)
if __name__ == "__main__":
    Gra1()