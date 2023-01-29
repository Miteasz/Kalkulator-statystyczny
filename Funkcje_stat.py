class KalkStat:

    def __init__(self):
        self.numbers = []
        self.name = ""

    def print_hi(self):
        self.name = input("Podaj swoje imię: ")
        print(f' Cześć, {self.name}')

    def liczby_uzytkownika(self):
        numbers = input("Wprowadź liczby rozdzielone spacją: ")
        try:
            self.numbers = [int(number) for number in numbers.split()]
        except ValueError:
            print("Upewnij się, że podałeś liczby i rozdzieliłeś je spacjami")

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
        wybor = int(input("Wybierz funkcję (podaj numer): "))
        if wybor == 1:
            print(self.obl_odchylenie_std())
        elif wybor == 2:
            print(self.obl_mode())
        elif wybor == 3:
            print(self.obl_mediana())
        elif wybor == 4:
            print(self.srednia_geometry())
        elif wybor == 5:
            print(self.srednia_arytmetyczna())
        else:
            print("Nieprawidłowy wybór. Proszę wybrać numer od 1 do 5.")



