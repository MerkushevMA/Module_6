class Vehicle:
    __COLOR_VARIANTS = ['Red', 'Green', 'Yellow', 'White', 'Black']
    __color_variants_lower = []
    for i in __COLOR_VARIANTS:
        __color_variants_lower.append(i.lower())

    def __init__(self, owner, __model, __engine_power, __color):
        self.owner = str(owner) #Владелец
        self.__model = str(__model) #Модель
        self.__engine_power = int(__engine_power) #Мощность двигателя
        self.__color = str(__color) #Цвет

    def get_model(self):
        print(f'Модель: {self.__model}')

    def get_horsepower(self):
        print('Мощность двигателя:', self.__engine_power)

    def get_color(self):
        print('Цвет:', self.__color)

    def set_color(self, new_color):
        str(new_color)
        if new_color.lower() in self.__color_variants_lower:
            self.__color = new_color
        else:
            print(f'Нельзя изменить цвет на {new_color}')

    def print_info(self):
        print(f'Модель: {self.__model}')
        print(f'Мощность двигателя: {self.__engine_power}')
        print(f'Цвет: {self.__color}')
        print(f'Владелец: {self.owner}')

class Sedan(Vehicle):
    __passanger_limit = 5

vehicle1 = Sedan('Dick', 'GT500', '600', 'green')
vehicle1.print_info()
vehicle1.set_color('Pink')
vehicle1.set_color('BLACK')
vehicle1.owner = 'Vanziliy'

vehicle1.print_info()