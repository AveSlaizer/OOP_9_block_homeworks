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

