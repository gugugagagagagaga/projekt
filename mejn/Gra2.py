import time

def wprowadzenie():
    print("Witaj w grze przygodowej!")
    time.sleep(2)
    print("Jesteś podróżnikiem w magicznym świecie pełnym niebezpieczeństw i tajemnic.")
    time.sleep(2)
    print("Twoim celem jest zdobycie legendarnego skarbu ukrytego w zamku Czarodzieja Zła.")
    time.sleep(2)
    print("Zaczynamy przygodę!")

def wybierz_sciezke():
    print("\nWydajesz się przed dwie ścieżki:")
    print("1. Przejdź przez mroczny las")
    print("2. Podróżuj przez bezkresne pustkowie")

    wybor = input("Wybierz numer ścieżki: ")

    if wybor == "1":
        sciezka_mroczny_las()
    elif wybor == "2":
        sciezka_pustkowie()
    else:
        print("Nieprawidłowy wybór. Spróbuj ponownie.")
        wybierz_sciezke()

def sciezka_mroczny_las():
    print("\nWchodzisz do mrocznego lasu, gdzie drzewa zasłaniają światło słoneczne.")
    time.sleep(2)
    print("Słyszysz szepty wiatru i daleki pomruk nieznanych stworzeń.")
    time.sleep(2)
    print("Co robisz?")
    time.sleep(1)

    print("\n1. Poszukaj skarbu w jaskini")
    print("2. Zbierz magiczne zioła")
    print("3. Kontynuuj podróż przez las")

    wybor = input("Twój wybór: ")

    if wybor == "1":
        poszukiwania_w_jaskini()
    elif wybor == "2":
        zbieranie_ziol()
    elif wybor == "3":
        kontynuacja_przez_las()
    else:
        print("Nieprawidłowy wybór. Spróbuj ponownie.")
        sciezka_mroczny_las()

def sciezka_pustkowie():
    print("\nWkraczasz na bezkresne pustkowie, gdzie wiatr unosi piasek w powietrzu.")
    time.sleep(2)
    print("Nie ma tutaj schronienia, a jedynym znakiem życia są ślady dzikich zwierząt.")
    time.sleep(2)
    print("Co robisz?")
    time.sleep(1)

    print("\n1. Poszukaj ukrytej oazy")
    print("2. Zbuduj prowizoryczne schronienie")
    print("3. Kontynuuj podróż przez pustkowie")

    wybor = input("Twój wybór: ")

    if wybor == "1":
        poszukiwania_oazy()
    elif wybor == "2":
        budowanie_schronienia()
    elif wybor == "3":
        kontynuacja_przez_pustkowie()
    else:
        print("Nieprawidłowy wybór. Spróbuj ponownie.")
        sciezka_pustkowie()


def poszukiwania_w_jaskini():
    print("\nWchodzisz do jaskini w poszukiwaniu skarbu.")
    time.sleep(2)
    print("Jaskinia jest ciemna, ale słyszysz skrzypienie skrzydeł.")
    time.sleep(2)
    print("Co robisz?")
    time.sleep(1)

    print("\n1. Podążaj dalej w głąb jaskini")
    print("2. Otwórz magiczną latarnię")
    print("3. Wyjdź z jaskini")

    wybor = input("Twój wybór: ")

    if wybor == "1":
        podazaj_w_glab_jaskini()
    elif wybor == "2":
        otworz_magiczna_latarnie()
    elif wybor == "3":
        wyjdz_z_jaskini()
    else:
        print("Nieprawidłowy wybór. Spróbuj ponownie.")
        poszukiwania_w_jaskini()

def zbieranie_ziol():
    print("\nZbierasz magiczne zioła rosnące wokół ciebie.")
    time.sleep(2)
    print("Czujesz, jak energia magiczna rozchodzi się w twoim ciele.")
    time.sleep(2)
    print("przedawkowałeś energię i umierasz.")
   

def kontynuacja_przez_las():
    print("\nKontynuujesz podróż przez mroczny las...")
    time.sleep(2)
    print("Drzewa zaczynają się rozweselać, a śpiew ptaków jest coraz głośniejszy.")
    time.sleep(2)
    print(" bezpiecznie przeszedłeś przez las, wszystko się dobrze kończy.")
    

def poszukiwania_oazy():
    print("\nSzukasz ukrytej oazy na pustkowiu.")
    time.sleep(2)
    print("Po długim poszukiwaniu nic nie znajdujesz")
    time.sleep(2)
    print("po pewnym czasie mdlejszesz z przemęcznia i odwodnienia, i umierasz.")
   

def budowanie_schronienia():
    print("\nBudujesz prowizoryczne schronienie przed piaskiem i wiatrem.")
    time.sleep(2)
    print("udało ci się schronić a następnego dnia z oddali zobaczyłeś polanę, udało ci się do niej dotrzeć i wszystko się dobrze skończyło")
    
def kontynuacja_przez_pustkowie():
    print("\nKontynuujesz podróż przez bezkresne pustkowie...")
    time.sleep(2)
    print("idziesz i idziesz przez pustkowie aż padasz ze zmęczenia")
    time.sleep(2)
    print("umierasz.")
 
def podazaj_w_glab_jaskini():
    print("\nPodążasz głębiej w głąb jaskini...")
    time.sleep(2)
    print("Jaskinia staje się coraz ciemniejsza, a dźwięki stworzeń stają się głośniejsze.")
    time.sleep(2)
    print("w pewnym momencie gdy już nic nie widzisz nagle słyszysz coś za sobą, nie zdązysz zareagować, umierasz.")
    

def otworz_magiczna_latarnie():
    print("\nOtwierasz magiczną latarnię, wchodisz na górę")
    time.sleep(2)
    print(" na górzę oślepia cię blask latarni ")
    time.sleep(2)
    print("próbujesz się wycofać ale zapomniałeś o stromuch schodach, spadasz ze zchodów i umierasz.")
   
def wyjdz_z_jaskini():
    print("\nWychodzisz z jaskini i wracasz na ścieżkę.")
    time.sleep(2)
    print("idziesz szukać dalej skarbu.")
    wybierz_sciezke()
   

def Gra2():
    wprowadzenie()
    wybierz_sciezke()

if __name__ == "__main__":
    Gra2()

