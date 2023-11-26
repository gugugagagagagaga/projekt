def main():
    print("Wybierz grę do uruchomienia:")
    print("1. Gra 1")
    print("2. Gra 2")
    print("3. Gra 3")

    wybor = input("Wybierz numer gry: ")

    if wybor == "1":
        from gra1 import Gra1
        Gra1()
    elif wybor == "2":
        from Gra2 import Gra2
        Gra2()
    elif wybor == "3":
        from Gra3 import Gra3
        Gra3()
    else:
        print("Nieprawidłowy wybór.")

if __name__ == "__main__":
    main()