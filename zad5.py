def lista_zawiera(items: list, value: int) -> bool:
    return value in items


lista = [1, 5, 10, 15]
wynik = lista_zawiera(lista, 10)
print(wynik)
