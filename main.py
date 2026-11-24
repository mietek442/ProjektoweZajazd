import random
kolory = ["czerwony", "żółty", "zielony", "pomarańczowy", "niebieski", "czarny", "fioletowy"]
def zajazd(x):
    wynik = random.sample(kolory, 4)
    print("Wpisz 4 kolory: (czerwony, żółty, zielony, pomarańczowy, niebieski, czarny, fioletowy)\n")
    if len(x) != 4:
        print("Podano złą ilość kolorów!")
    else:
        proby = 0
        wygrana = False
        



