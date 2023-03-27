class UnitConverter:

    @staticmethod
    def kilometers_to_miles(kilometers: float) -> float:
        """
        Преобразует километры в мили

        :param kilometers (float): Километры
        :return:
                float: Мили
        """
        return kilometers * 0.6213

    @staticmethod
    def miles_to_kilometers(miles: float) -> float:
        """
        Преобразует мили в километры

        :param miles (float): Мили
        :return:
                float: Километры
        """
        return miles * 1.6093

    @staticmethod
    def kilograms_to_pounds(kg: float) -> float:
        """
        Преобразует килограммы в фунты

        :param kg (float): Килограммы
        :return:
                float: Фунты
        """
        return kg * 2.2

    @staticmethod
    def pounds_to_kilograms(pounds: float) -> float:
        """
        Преобразует фунты в килограммы

        :param pounds (float): Фунты
        :return:
                float: Килограммы
        """
        return pounds * 0.4535

