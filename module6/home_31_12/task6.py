# Класс Vehicle представляет общее транспортное средство с атрибутами марки (brand) и скорости (speed) 
# и методом move, который выводит сообщение о движении. Класс Car является наследником Vehicle и добавляет 
# метод honk, а также переопределяет метод move для отображения поведения автомобиля. Класс Bicycle, 
# также унаследованный от Vehicle, переопределяет метод move для отображения поведения велосипеда и 
# добавляет метод ring_bell для звонка в велосипедный звонок. Эти классы демонстрируют простое наследование и переопределение методов.

class Vehicle:
    def __init__(self, brand, speed):
        self.brand = brand
        self.speed = speed

    def move(self):
        print(f"Транспортное средство движется со скоростью {self.speed} км/ч")


class Car(Vehicle):
    def move(self):
        print(f"Машина едет со скоростью {self.speed} км/ч")

    def honk(self):
        print("Машина сигналит!")


class Bicycle(Vehicle):
    def move(self):
        print(f"Велосипед едет со скоростью {self.speed} км/ч")

    def ring_bell(self):
        print("Велосипед звонит в звонок!")


# Создаем объекты и демонстрируем их поведение
vehicle = Vehicle("Generic", 60)
car = Car("Toyota", 120)
bicycle = Bicycle("Trek", 20)

vehicle.move()
car.move()
car.honk()
bicycle.move()
bicycle.ring_bell()


# Классы Engine и Seats представляют компоненты транспортных средств. Engine описывает тип двигателя (engine_type) и 
# метод его запуска (start_engine), а Seats включает атрибут количества мест (seat_count) и метод настройки сидений (adjust_seats).
# Класс ElectricCar объединяет возможности классов Car, Engine и Seats с помощью множественного наследования. 
# Он переопределяет метод move, добавляет метод charge и демонстрирует использование всех функциональностей базовых классов в одном объекте.

class Engine:
    def __init__(self, engine_type):
        self.engine_type = engine_type

    def start_engine(self):
        print(f"Двигатель запущен: {self.engine_type}")


class Seats:
    def __init__(self, seat_count):
        self.seat_count = seat_count

    def adjust_seats(self):
        print(f"Регулировка {self.seat_count} сидений")


class ElectricCar(Car, Engine, Seats):
    def __init__(self, brand, speed, engine_type, seat_count):
        Car.__init__(self, brand, speed)
        Engine.__init__(self, engine_type)
        Seats.__init__(self, seat_count)

    def move(self):
        print(f"Электромобиль едет бесшумно со скоростью {self.speed} км/ч")

    def charge(self):
        print("Электромобиль заряжается")


# Создаем объект и демонстрируем его поведение
electric_car = ElectricCar("Tesla", 150, "Электрический", 5)

electric_car.move()
electric_car.start_engine()
electric_car.adjust_seats()
electric_car.honk()
electric_car.charge()
