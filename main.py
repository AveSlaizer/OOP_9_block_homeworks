from temperature_formatter import TemperatureFormatter


"""
Задание 1.
Создайте класс для конвертирования температуры из Цельсия в
Фаренгейты и наоборот. У класса должно быть два статических метода: для
перевода из Цельсия в Фаренгейты и для перевода из Фаренгейта в Цельсии.
"""


def execute_application():
    celsius = float(input("Введите температуру в градусах Цельсия: "))
    fahrenheit = TemperatureFormatter.celsius_to_fahrenheit(celsius)
    print(f"{celsius} градусов Цельсия равно {fahrenheit:.01f} градусов Фаренгейта.")

    fahrenheit = float(input("Введите температура в градусах Фаренгейта: "))
    celsius = TemperatureFormatter.fahrenheit_to_celsius(fahrenheit)
    print(f"{fahrenheit} градусов Фаренгейта равно {celsius:.01f} градусов Цельсия")


if __name__ == "__main__":
    execute_application()
