def show_every_second():
    numbers = list(range(1, 11))
    print('Wszystkie liczby:', numbers)
    print('Co drugi element:')
    for i in range(0, len(numbers), 2):
        print(numbers[i], numbers[i + 1])


show_every_second()
