def parzysta(number: int):
    return number % 2 == 0


result = parzysta(9)

if result:
    print("Liczba parzysta")
else:
    print("Liczba nieparzysta")
