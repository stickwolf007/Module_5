class House:
    houses_history = []

    def __new__(cls, *args, **kwargs):
        cls.houses_history.append(args[0])
        return object.__new__(cls)


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


    def __del__(self):
        print(f'{self.name} снесен, но останется в истории')



    def __len__(self):
        return self.number_of_floors


    def __str__(self):
        return f'Название {self.name}, количество этажей {self.number_of_floors}.'

    def __eq__(self, other):
        if isinstance(self.number_of_floors, int):
            return self.number_of_floors == other.number_of_floors

    def __lt__(self, other):
        if isinstance(self.number_of_floors, int):
            return self.number_of_floors < other.number_of_floors

    def __gt__(self, other):
        if isinstance(self.number_of_floors, int):
            return self.number_of_floors > other.number_of_floors

    def __le__(self, other):
        if isinstance(self.number_of_floors, int):
            return self.number_of_floors <= other.number_of_floors

    def __ge__(self, other):
        if isinstance(self.number_of_floors, int):
            return self.number_of_floors >= other.number_of_floors

    def __ne__(self, other):
        if isinstance(self.number_of_floors, int):
            return self.number_of_floors != other.number_of_floors

    def __add__(self, value):
        if isinstance(self.number_of_floors, int):
            self.number_of_floors += value
            return self

    def __radd__(self, value):
        if isinstance(self.number_of_floors, int):
            self.number_of_floors += value
            return self

    def __iadd__(self, value):
        if isinstance(self.number_of_floors, int):
            self.number_of_floors += value
            return self


h1 = House('ЖК Эльбрус', 10)
print(House.houses_history)
h2 = House('ЖК Акация', 20)
print(House.houses_history)
h3 = House('ЖК Матрёшки', 20)
print(House.houses_history)

# Удаление объектов
del h2
del h3

print(House.houses_history)

