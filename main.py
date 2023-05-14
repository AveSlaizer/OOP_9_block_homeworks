from car import Car, CarPickleAdapter, CarJSONAdapter


def execute_application():
    car = Car("Лада", "Самара", "2000")
    print(car)
    data = CarJSONAdapter.to_json(car)
    print(data)
    obj = CarJSONAdapter.from_json(data)
    print(obj)


if __name__ == "__main__":
    execute_application()
