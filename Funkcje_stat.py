class KalkStat:


    '''Dokumentacja klasy KalkStat:

Klasa KalkStat jest kalkulatorem statystycznym, który umożliwia wykonywanie podstawowych obliczeń statystycznych na podanych przez użytkownika liczbach.

Metoda init inicjalizuje pustą listę "numbers" oraz pusty napis "name".

Metoda print_hi pyta użytkownika o imię i wyświetla powitanie.

Metoda liczby_uzytkownika pyta użytkownika o liczby i zapisuje je w atrybucie "numbers" jako listę liczb całkowitych. Sprawdza również, czy lista nie zawiera zera.

Metoda srednia_arytmetyczna oblicza i zwraca średnią arytmetyczną podanych liczb.

Metoda srednia_geometryczna oblicza i zwraca średnią geometryczną podanych liczb.

Metoda obl_mediana oblicza i zwraca medianę podanych liczb.

Metoda obl_mode oblicza i zwraca modę podanych liczb.

Metoda obl_odchylenie_std oblicza i zwraca odchylenie standardowe podanych liczb.

Metoda wybierz_funkcje pozwala użytkownikowi na wybór jednej z pięciu funkcji statystycznych do wykonania na podanych liczbach. Po wyborze i wykonaniu funkcji, wynik jest wyświetlany.'''
    def __init__(self):
        self.numbers = []
        self.name = ""

    def print_hi(self):
        self.name = input("Podaj swoje imię: ")
        print(f' Cześć, {self.name}')

    def liczby_uzytkownika(self):
        self.numbers = input("Wprowadź liczby rozdzielone spacją: ")
        print(f'''Wybrane liczby to: {self.numbers}''')
        try:
            self.numbers = [int(number) for number in self.numbers.split()]
            if 0 in self.numbers:
                print("Błąd: lista zawiera 0.")
                exit()
        except:
            print("Upewnij się, że podałeś liczby i rozdzieliłeś je spacjami")
            exit()


    def srednia_arytmetyczna(self):
        return sum(self.numbers) / len(self.numbers)



    def srednia_geometryczna(self):
        dalej = 1
        for number in self.numbers:
            dalej *= number
        sr_geo = dalej ** (1/len(self.numbers))
        return sr_geo

    def obl_mediana(self):
        self.numbers.sort()
        if len(self.numbers) % 2 == 0:
            mediana = (self.numbers[len(self.numbers) // 2 - 1] + self.numbers[len(self.numbers) // 2]) / 2
        else:
            mediana = self.numbers[len(self.numbers) // 2]
        return mediana

    def obl_mode(self):
        licznik = {}
        for number in self.numbers:
            licznik[number] = licznik.get(number, 0) + 1
        moda = max(licznik, key=licznik.get)
        return moda

    def obl_odchylenie_std(self):
        n = len(self.numbers)
        srednia = sum(self.numbers) / n
        wariancja = sum((x - srednia) ** 2 for x in self.numbers) / n
        odchylenie_standardowe = wariancja ** 0.5
        return odchylenie_standardowe

    def wybierz_funkcje(self):
        print('1. Odchylenie standardowe')
        print('2. Moda')
        print('3. Mediana')
        print('4. Średnia geometryczna')
        print('5. Średnia arytmetyczna')
        try:
            wybor = int(input("Wybierz funkcję (podaj numer): "))
            if wybor == 1:
                kalkulator = KalkStat()
                kalkulator.liczby_uzytkownika()
                wynik = kalkulator.obl_odchylenie_std()
                print(f'''Wynik to: {round(wynik, 2)}''')
            elif wybor == 2:
                kalkulator = KalkStat()
                kalkulator.liczby_uzytkownika()
                wynik = kalkulator.obl_mode()
                print(f'''Wynik to: {round(wynik, 2)}''')
            elif wybor == 3:
                kalkulator = KalkStat()
                kalkulator.liczby_uzytkownika()
                wynik = kalkulator.obl_mediana()
                print(f'''Wynik to: {round(wynik, 2)}''')
            elif wybor == 4:
                kalkulator = KalkStat()
                kalkulator.liczby_uzytkownika()
                wynik = kalkulator.srednia_geometryczna()
                print(f'''Wynik to: {round(wynik, 2)}''')
            elif wybor == 5:
                kalkulator = KalkStat()
                kalkulator.liczby_uzytkownika()
                wynik = kalkulator.srednia_arytmetyczna()
                print(f'''Wynik to: {round(wynik,2)}''')

            else:
                print("Nieprawidłowy wybór. Proszę wybrać numer od 1 do 5.")
        except:
            print("Nieprawidłowy wybór. Proszę wybrać numer od 1 do 5.")



