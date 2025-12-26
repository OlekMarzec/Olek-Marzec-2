class Property:
    def __init__(self, area, rooms, price, address):
        self.area = area
        self.rooms = rooms
        self.price = price
        self.address = address

    def __str__(self):
        return (f"Nieruchomość przy {self.address}, {self.area}m2, "
                f"{self.rooms} pokoje, cena: {self.price}")


class House(Property):
    def __init__(self, area, rooms, price, address, plot):
        super().__init__(area, rooms, price, address)
        self.plot = plot

    def __str__(self):
        return f"Dom: {super().__str__()}, działka: {self.plot}m2"


class Flat(Property):
    def __init__(self, area, rooms, price, address, floor):
        super().__init__(area, rooms, price, address)
        self.floor = floor

    def __str__(self):
        return f"Mieszkanie: {super().__str__()}, piętro: {self.floor}"


house = House(120, 5, 600000, "Kwiatowa 5", 500)
flat = Flat(50, 2, 300000, "Leśna 10/4", 2)

print(house)
print(flat)
