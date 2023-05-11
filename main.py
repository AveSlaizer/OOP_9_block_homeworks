from times import Time, TimePickleAdapter, TimeJSONAdapter

"""
Задание 4
К уже реализованному классу «Часы» добавьте возможность упаковки и распаковки данных с использованием json и pickle.
"""


def execute_application():
    time = Time(100)
    print(time)
    data = TimeJSONAdapter.to_json(time)
    print(data)
    obj = TimeJSONAdapter.from_json(data)
    print(obj)



if __name__ == "__main__":
    execute_application()
