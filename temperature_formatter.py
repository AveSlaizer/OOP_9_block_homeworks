class TemperatureFormatter:

    @staticmethod
    def celsius_to_fahrenheit(qty: float) -> float:
        """
        Рассчитывает градусы Фаренгейта, из полученных из градусов Цельсия

        :param qty (float): градусы Цельсия
        :return:
                float: Градусы Фаренгейта
        """
        return qty * 1.8 + 32

    @staticmethod
    def fahrenheit_to_celsius(qty: float) -> float:
        """
        Рассчитывает градусы Цельсия, из полученных из градусов Фаренгейта

        :param qty (float): Градусы Фаренгейта
        :return:
                float: градусы Цельсия
        """
        return (qty -32) / 1.8
