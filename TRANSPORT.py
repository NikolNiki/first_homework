from abc import ABC, abstractmethod

class Transport(ABC):
    def __init__(self, fuel: float, condition: int, fuel_consumption: float, wear_rate: float):
        self.fuel = fuel
        # Обмежуємо технічний стан в діапазоні від 0 до 100
        self._condition = max(0, min(condition, 100))
        self.fuel_consumption = fuel_consumption  # Витрата пального на 1 км
        self.wear_rate = wear_rate                # Знос стану на 1 км
    @property
    def condition(self) -> int:
        return self._condition

    @condition.setter
    def condition(self, value: int):
        self._condition = max(0, min(value, 100))

    @property
    def is_working(self) -> bool:
        # Транспорт придатний до роботи, якщо його технічний стан вище 20%
        return self._condition > 20

    def move(self, distance: float):
        # 1. Перевірка технічного стану
        if not self.is_working:
            print(f"Рух неможливий: транспортний засіб несправний (стан {self.condition}%).")
            return

        # 2. Перевірка запасу пального
        needed_fuel = distance * self.fuel_consumption
        if self.fuel < needed_fuel:
            print(f"Рух неможливий: недостатньо пального (необхідно {needed_fuel} л, є {self.fuel} л).")
            return
        # 3. Процес успішного руху
        self.fuel -= needed_fuel
        self.condition -= distance * self.wear_rate
        print(f"Успішно пройдено дистанцію: {distance} км.")

class Car(Transport):
    def __init__(self, model: str):
        super().__init__(fuel=50, condition=100, fuel_consumption=0.1, wear_rate=0.5)
        self.model = model

    def __str__(self) -> str:
        return f"Легковий автомобіль '{self.model}' | Пальне: {self.fuel} л | Стан: {self.condition}% | Працює: {self.is_working}"

class Truck(Transport):
    def __init__(self, name: str):
        super().__init__(fuel=120, condition=100, fuel_consumption=0.3, wear_rate=0.8)
        self.name = name

    def __str__(self) -> str:
        return f"Вантажівка '{self.name}' | Пальне: {self.fuel} л | Стан: {self.condition}% | Працює: {self.is_working}"

class Motorcycle(Transport):
    def __init__(self, brand: str):
        super().__init__(fuel=20, condition=100, fuel_consumption=0.05, wear_rate=0.3)
        self.brand = brand

    def __str__(self) -> str:
        return f"Мотоцикл '{self.brand}' | Пальне: {self.fuel} л | Стан: {self.condition}% | Працює: {self.is_working}"

class ServiceStation:
    def repair(self, transport_unit: Transport):
        print(f"--- Обслуговування на СТО для {transport_unit.__class__.__name__} ---")
        print(f"Стан до ремонту: {transport_unit.condition}%")
        transport_unit.condition += 40
        print(f"Стан після ремонту: {transport_unit.condition}%")

# --- Тести програми ---
if __name__ == "__main__":
    print("=== Створення об'єктів ===")
    car = Car("Toyota")
    truck = Truck("Volvo")
    motorcycle = Motorcycle("Yamaha")

    print(car)
    print(truck)
    print(motorcycle)

    print("\n=== 1. Перевірка руху транспорту ===")
    car.move(100)
    print(car)

    print("\n=== 2. Перевірка значення is_working ===")
    print(f"Машина придатна до роботи? {car.is_working}")

    print("\n=== 3. Перевірка вбудованого словника __dict__ ===")
    print(car.__dict__)

    print("\n=== 4. Перевірка поведінки при відсутності пального ===")
    car.move(500)

    print("\n=== 5. Перевірка поведінки при поганому тех. стані ===")
    motorcycle.condition = 15
    print(f"Поточний стан мотоцикла: {motorcycle.condition}%, Справний? {motorcycle.is_working}")
    motorcycle.move(10)

    print("\n=== 6. Перевірка ServiceStation ===")
    station = ServiceStation()

    station.repair(car)
    station.repair(motorcycle)

    print("\nСерія послідовних ремонтів мотоцикла:")
    station.repair(motorcycle)
    station.repair(motorcycle)

    print("\n=== Підсумковий стан після всіх тестів ===")
    print(car)
    print(motorcycle)