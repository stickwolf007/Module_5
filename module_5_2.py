class House:
    def __init__(self, name, number_of_floors):
        self.number_of_floors = number_of_floors
        self.name = name

    def go_to(self, new_floor):
        if new_floor <= self.number_of_floors:
            for i in range(new_floor):
                i += 1
                print(i)
        else:
            print(f'Такого этажа не существует')

    def __len__(self):
        return self.number_of_floors


    def __str__(self):
        return f'Название {self.name}, количество этажей {self.number_of_floors}.'


h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)

# __str__
print(h1)
print(h2)

# __len__
print(len(h1))
print(len(h2))