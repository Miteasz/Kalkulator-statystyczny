class Start:
    def print_hi(name):
        name = input("Podaj swoje imię")
        print(f' Hi, {name}')

    def wybierz_funkcje():
        print('1. Odchylenie standardowe')
        print('2. Moda')
        print('3. Mediana')
        print('4. Średnia geometryczna')
        print('5. Średnia arytmetyczna')
        wybor = int(input("Wybierz funkcję (podaj numer): "))
        if wybor == 1:
            KalkStat.obl_odchylenie_std()
        elif wybor == 2:
            KalkStat.obl_mode()
        elif wybor == 3:
            KalkStat.obl_mediana()
        elif wybor == 4:
            KalkStat.srednia_geometryczna()
        elif wybor == 5:
            KalkStat.srednia_arytmetyczna()
        else:
            print("Nieprawidłowy wybór. Proszę wybrać numer od 1 do 5.")
