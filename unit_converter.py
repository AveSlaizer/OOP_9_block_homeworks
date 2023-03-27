class UnitConverter:

    @staticmethod
    def kilometers_to_miles(kilometers: float) -> float:
        """
        Преобразует километры в мили

        :param kilometers (float): Километры
        :return:
                float: Мили
        """
        return kilometers * 0.62137

    @staticmethod
    def miles_to_kilometers(miles: float) -> float:
        """
        Преобразует мили в километры

        :param miles (float): Мили
        :return:
                float: Километры
        """
        return miles * 1.609344

    @staticmethod
    def kilogram_to_pounds(kg: float) -> float:
        """
        Преобразует килограммы в фунты

        :param kg (float): Килограммы
        :return:
                float: Фунты
        """
        return kg * 2.2

