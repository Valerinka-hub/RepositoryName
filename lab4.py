class Vehicle:


    def __init__(self, brand: str, model: str, year: int) -> None:
        """
        Инициализация транспортного средства.

        :param brand: марка транспортного средства
        :param model: модель транспортного средства
        :param year: год выпуска
        """
        self._brand = brand
        self._model = model
        self._year = year
    def __str__(self) -> str:

        return f"{self._brand} {self._model} ({self._year})"

    def __repr__(self) -> str:

        return f"Vehicle(brand='{self._brand}', model='{self._model}', year={self._year})"

    def drive(self) -> str:

        return f"The {self._brand} {self._model} is driving."


class Car(Vehicle):


    def __init__(self, brand: str, model: str, year: int, doors: int) -> None:
        """
        Инициализация легкового автомобиля.

        :param brand: марка легкового автомобиля
        :param model: модель легкового автомобиля
        :param year: год выпуска
        :param doors: количество дверей
        """
        super().__init__(brand, model, year)
        self.doors = doors
    def __str__(self) -> str:
        """Возвращает строковое представление легкового автомобиля."""
        return f"{super().__str__()} with {self.doors} doors."

    def drive(self) -> str:
        """Перегруженный метод, который описывает движение легкового автомобиля.

        Здесь мы добавляем информацию о количестве дверей.
        """
        return f"The car {self._brand} {self._model} with {self.doors} doors is driving."


class Truck(Vehicle):
    """
    Класс грузового автомобиля, наследующий от Vehicle.
    """

    def __init__(self, brand: str, model: str, year: int, capacity: float) -> None:
        """
        Инициализация грузового автомобиля.

        :param brand: марка грузового автомобиля
        :param model: модель грузового автомобиля
        :param year: год выпуска
        :param capacity: грузоподъемность в тоннах
        """
        super().__init__(brand, model, year)
        self._capacity = capacity

    def __str__(self) -> str:
        """Возвращает строковое представление грузового автомобиля."""
        return f"{super().__str__()} with a capacity of {self._capacity} tons."

    def drive(self) -> str:
        """Перегруженный метод, который описывает движение грузового автомобиля.

        Здесь мы добавляем информацию о грузоподъемности.
        """
        return f"The truck {self._brand} {self._model} with a capacity of {self._capacity} tons is driving."


if __name__ == "__main__":
    car = Car("BMW", "3 Series", 2022, 4)
    truck = Truck("BMW", "X7", 2021, 3.5)

    print(car)
    print(car.drive())

    print(truck)
    print(truck.drive())