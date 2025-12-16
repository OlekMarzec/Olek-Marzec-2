def przetworz_listy(lista1: list, lista2: list) -> list:
    polaczona_lista = lista1 + lista2
    unikalne_elementy = list(set(polaczona_lista))
    elementy_do_szescianu = [x ** 3 for x in unikalne_elementy]
    return elementy_do_szescianu


moja_lista1 = [1, 2, 2]
moja_lista2 = [2, 3, 4]
wynik = przetworz_listy(moja_lista1, moja_lista2)
print(wynik)
