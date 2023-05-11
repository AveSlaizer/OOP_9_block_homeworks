from fraction import MathematicalFraction, FractionPickleAdapter, FractionJSONAdapter

"""
Задание 3
К уже реализованному классу «Дробь» добавьте возможность упаковки и распаковки данных с использованием json и pickle
"""


def execute_application():
     fraction = MathematicalFraction(1, 2)
     print(fraction)
     data = FractionJSONAdapter.to_json(fraction)
     print(data)
     new_fraction = FractionJSONAdapter.from_json(data)
     print(new_fraction)


if __name__ == "__main__":
    execute_application()
