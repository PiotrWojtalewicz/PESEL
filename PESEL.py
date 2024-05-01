import random

def generate_pesel(rok, miesiac, dzien, plec, miejsce):
 
    if not (1800 <= rok <= 2299):
        raise ValueError("Rok urodzenia powinien być w zakresie od 1800 do 2299.")
    if not (1 <= miesiac <= 12):
        raise ValueError("Miesiąc urodzenia powinien być w zakresie od 1 do 12.")
    if not (1 <= dzien <= 31):
        raise ValueError("Dzień urodzenia powinien być w zakresie od 1 do 31.")
    if not (plec.lower() in ['m', 'k']):
        raise ValueError("Płeć powinna być 'm' (mężczyzna) lub 'k' (kobieta).")
    if not (1 <= miejsce <= 999):
        raise ValueError("Miejsce urodzenia powinno być w zakresie od 1 do 999.")


    pesel = []


    pesel.extend([int(str(rok)[2:]), miesiac, dzien])


    pesel.extend([random.randint(0, 9) for _ in range(3)])


    if plec.lower() == 'm':
        pesel.append(random.randint(0, 4) * 2)
    else:
        pesel.append(random.randint(0, 4) * 2 + 1)


    wagi = [1, 3, 7, 9, 1, 3, 7, 9, 1, 3]
    suma_kontrolna = sum(w * p for w, p in zip(wagi, pesel)) % 10
    pesel.append((10 - suma_kontrolna) % 10)


    pesel.extend([int(d) for d in str(miejsce).zfill(3)])


    if len(pesel) != 11:
        raise ValueError("Wystąpił błąd podczas generowania PESELu.")


    pesel_str = ''.join(map(str, pesel))

    return pesel_str

# Przykładowe użycie
rok = int(input("Podaj rok urodzenia (1800-2299): "))
miesiac = int(input("Podaj miesiąc urodzenia (1-12): "))
dzien = int(input("Podaj dzień urodzenia (1-31): "))
plec = input("Podaj płeć ('m' lub 'k'): ")
miejsce = int(input("Podaj miejsce urodzenia (1-999): "))

try:
    pesel = generate_pesel(rok, miesiac, dzien, plec, miejsce)
    print("Wygenerowany PESEL:", pesel)
except ValueError as e:
    print("Błąd:", e)
