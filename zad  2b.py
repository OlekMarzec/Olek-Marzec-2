def multiply_by_two_for(liczby):
    result = []
    for num in liczby:
        result.append(num * 2)
    return result
lista = [1, 2, 3, 4, 5]
print(multiply_by_two_for(lista))

def pomnoz_przez_dwa(liczby):
    return [num * 2 for num in liczby]
lista = [1, 2, 3, 4, 5]
print(pomnoz_przez_dwa(lista))


