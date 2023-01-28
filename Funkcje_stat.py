
class KalkStat:

    def __init__(self):
        self.numbers = []

    def liczby_uzytkownika():
        try:
            numbers = input("Wprowadź liczby rozdzielone spacją: ").split()
            numbers = [int(number) for number in numbers]
            return numbers
        except:
            print("Upewnij się, że podałeś liczby i rozdzieliłeś je przecinkami")

    numbers = liczby_uzytkownika()
    print(numbers)

    def srednia_arytmetyczna(numbers):
        return sum(numbers) / len(numbers)

    average = srednia_arytmetyczna(numbers)
    print(round(float(average),2))

    def srednia_geometryczna(numbers):
        dalej = 1
        for number in numbers:
            dalej *= number
        sr_geo = dalej ** (1/len(numbers))
        return sr_geo

    sr_geo = srednia_geometryczna(numbers)
    print(round(float(sr_geo),2))

    def obl_mediana(numbers):
        numbers.sort()
        if len(numbers) % 2 == 0:
            mediana = (numbers[len(numbers) // 2 - 1] + numbers[len(numbers) // 2]) / 2
        else:
            mediana = numbers[len(numbers) // 2]
        return mediana

    mediana = obl_mediana(numbers)
    print(mediana)

    def obl_mode(numbers):
        licznik = {}
        for number in numbers:
            if number in licznik:
                licznik[number] += 1
            else:
                licznik[number] = 1
        moda = max(licznik, key=licznik.get)
        return moda

    moda = obl_mode(numbers)
    print(round(float(moda),2))


    def obl_odchylenie_std(numbers):
        n = len(numbers)
        srednia = sum(numbers) / n
        wariancja = sum((x - srednia) ** 2 for x in numbers) / n
        odchylenie_standardowe = wariancja ** 0.5
        return odchylenie_standardowe

    odchylenie_standardowe = obl_odchylenie_std(numbers)
    print(round(float(odchylenie_standardowe),2))

