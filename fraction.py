from math import gcd
from typing import Union
import pickle, json


class InitializationFractionError(Exception):

    def __init__(self, text: str, value):
        self.text = text
        self.value = value


class MathematicalFraction:

    def __init__(self, numerator: int, denominator: int):
        self.__numerator = self.__is_numerator(numerator)
        self.__denominator = self.__is_denominator(denominator)
        self.__convert_fraction()

    @staticmethod
    def __is_numerator(value: int):
        if not isinstance(value, int):
            raise TypeError(f"Не верный тип данных: \'{value.__class__.__name__}\' "
                            f"ожидался 'int'")
        return value

    @staticmethod
    def __is_denominator(value: int):
        if not isinstance(value, int):
            raise TypeError(f"Не верный тип данных: \'{value.__class__.__name__}\' "
                            f"ожидался 'int'")
        if value == 0:
            raise InitializationFractionError("Невозможно создать дробь со знаменателем равным", value)
        return value

    def __convert_fraction(self):
        """Конвертирует дробь к единообразному виду. Если дробь отрицательная - то числитель отрицательный,
        знаменатель положительный, если положительная - то числитель и знаменатель положительные."""
        if self.__numerator * self.__denominator < 0:
            self.__numerator = -1 * abs(self.__numerator)
            self.__denominator = abs(self.__denominator)
        if self.__numerator < 0 and self.__denominator < 0:
            self.__numerator *= -1
            self.__denominator *= -1

    def shorten_fraction(self):
        """
        Сокращает дробь
        """
        value = gcd(self.__numerator, self.__denominator)
        if value > 1:
            self.__numerator = int(self.__numerator / value)
            self.__denominator = int(self.__denominator / value)

    def __lead_to_common_denominator(self, other, denominator: bool = True) \
            -> Union[tuple[int, int], tuple[int, int, int]]:
        """
        Возвращает кортеж с числителем первой дроби, числителем второй дроби и общий знаменатель дробей.
        Если denominator == False, то общий знаменатель не будет возвращаться

        :param other MathematicalFraction: дробь
        :param denominator bool: триггер, определяет, вернется ли общий знаменатель
        :return:
                Union[tuple[int, int], tuple[int, int, int]]:
                 Числитель первой дроби, числитель второй дроби и общий знаменатель, если denominator == True
        """
        self.__is_math_fraction(other)
        if self.__denominator == other.__denominator:
            new_denominator = self.__denominator
        else:
            new_denominator = self.__denominator * other.__denominator

        if denominator:
            value_tuple = (self.__numerator * other.__denominator,
                           other.__numerator * self.__denominator,
                           new_denominator)
        else:
            value_tuple = (self.__numerator * other.__denominator,
                           other.__numerator * self.__denominator)
        return value_tuple

    def __is_math_fraction(self, other):
        if not isinstance(other, MathematicalFraction):
            raise TypeError(f"Ошибка! Требуемый тип данных:\'{self.__class__.__name__}\', "
                            f"получен: \'{other.__class__.__name__}\'")

    @property
    def numerator(self):
        return self.__numerator

    @property
    def denominator(self):
        return self.__denominator

    def __str__(self):
        return f"{'- ' if self.__numerator < 0 else ''}{abs(self.__numerator)} / {self.__denominator}"

    def __hash__(self):
        return hash((self.__numerator, self.__denominator))

    def __eq__(self, other):
        self.__is_math_fraction(other)
        numerator1, numerator2 = self.__lead_to_common_denominator(other, denominator=False)
        return numerator1 == numerator2

    def __ne__(self, other):
        self.__is_math_fraction(other)
        numerator1, numerator2 = self.__lead_to_common_denominator(other, denominator=False)
        return numerator1 != numerator2

    def __lt__(self, other):
        self.__is_math_fraction(other)
        numerator1, numerator2 = self.__lead_to_common_denominator(other, denominator=False)
        return numerator1 < numerator2

    def __le__(self, other):
        self.__is_math_fraction(other)
        numerator1, numerator2 = self.__lead_to_common_denominator(other, denominator=False)
        return numerator1 <= numerator2

    def __gt__(self, other):
        self.__is_math_fraction(other)
        numerator1, numerator2 = self.__lead_to_common_denominator(other, denominator=False)
        return numerator1 > numerator2

    def __ge__(self, other):
        self.__is_math_fraction(other)
        numerator1, numerator2 = self.__lead_to_common_denominator(other, denominator=False)
        return numerator1 >= numerator2

    def __add__(self, other):
        if isinstance(other, MathematicalFraction):
            numerator1, numerator2, denominator = self.__lead_to_common_denominator(other)
            new_fraction = MathematicalFraction(numerator1 + numerator2, denominator)
        elif isinstance(other, int):
            new_fraction = MathematicalFraction(self.__numerator + self.__denominator * other, self.__denominator)
        else:
            raise TypeError(f"Недопустимый тип данных \'{other.__class__.__name__}\'")
        new_fraction.shorten_fraction()
        return new_fraction

    def __sub__(self, other):
        if isinstance(other, MathematicalFraction):
            numerator1, numerator2, denominator = self.__lead_to_common_denominator(other)
            new_fraction = MathematicalFraction(numerator1 - numerator2, denominator)
        elif isinstance(other, int):
            new_fraction = MathematicalFraction(self.__numerator - self.__denominator * other, self.__denominator)
        else:
            raise TypeError(f"Недопустимый тип данных \'{other.__class__.__name__}\'")
        new_fraction.shorten_fraction()
        return new_fraction

    def __iadd__(self, other):
        if isinstance(other, MathematicalFraction):
            numerator1, numerator2, denominator = self.__lead_to_common_denominator(other)
            self.__numerator = numerator1 + numerator2
            self.__denominator = denominator
        elif isinstance(other, int):
            self.__numerator = self.__numerator + self.__denominator * other
        else:
            raise TypeError(f"Недопустимый тип данных \'{other.__class__.__name__}\'")
        self.shorten_fraction()
        return self

    def __isub__(self, other):
        if isinstance(other, MathematicalFraction):
            numerator1, numerator2, denominator = self.__lead_to_common_denominator(other)
            self.__numerator = numerator1 - numerator2
            self.__denominator = denominator
        elif isinstance(other, int):
            self.__numerator = self.__numerator - self.__denominator * other
        else:
            raise TypeError(f"Недопустимый тип данных \'{other.__class__.__name__}\'")
        self.shorten_fraction()
        return self

    def __mul__(self, other):
        if isinstance(other, MathematicalFraction):
            numerator = self.__numerator * other.__numerator
            denominator = self.__denominator * other.__denominator
            new_fraction = MathematicalFraction(numerator, denominator)
        elif isinstance(other, int):
            new_fraction = MathematicalFraction(self.__numerator * other, self.__denominator)
        else:
            raise TypeError(f"Недопустимый тип данных \'{other.__class__.__name__}\'")
        new_fraction.shorten_fraction()
        return new_fraction

    def __imul__(self, other):
        if isinstance(other, MathematicalFraction):
            self.__numerator *= other.__numerator
            self.__denominator *= other.__denominator
        elif isinstance(other, int):
            self.__numerator = self.__numerator * other
        else:
            raise TypeError(f"Недопустимый тип данных \'{other.__class__.__name__}\'")
        self.shorten_fraction()
        return self

    def __truediv__(self, other):
        if isinstance(other, MathematicalFraction):
            numerator = self.__numerator * other.__denominator
            denominator = self.__denominator * other.__numerator
            new_fraction = MathematicalFraction(numerator, denominator)
        elif isinstance(other, int):
            new_fraction = MathematicalFraction(self.__numerator, self.__denominator * other)
        else:
            raise TypeError(f"Недопустимый тип данных \'{other.__class__.__name__}\'")
        new_fraction.shorten_fraction()
        return new_fraction

    def __itruediv__(self, other):
        if isinstance(other, MathematicalFraction):
            self.__numerator *= other.__denominator
            self.__denominator *= other.__numerator
        elif isinstance(other, int):
            self.__denominator *= other
        else:
            raise TypeError(f"Недопустимый тип данных \'{other.__class__.__name__}\'")
        self.shorten_fraction()
        return self


class FractionPickleAdapter:

    @staticmethod
    def to_pickle(fraction: MathematicalFraction):
        if not isinstance(fraction, MathematicalFraction):
            raise TypeError(f"Недопустимый тип данных '{fraction.__class__.__name__}', "
                            f"ожидался 'MathematicalFraction'")
        return pickle.dumps({
            "className": fraction.__class__.__name__,
            "numerator": fraction.numerator,
            "denominator": fraction.denominator
        })

    @staticmethod
    def from_pickle(data):
        obj = pickle.loads(data)
        try:
            assert obj["className"] == "MathematicalFraction", "Ошибка обработки данных"
            return MathematicalFraction(obj["numerator"], obj["denominator"])
        except AttributeError:
            print("Ошибка обработки данных")
        except AssertionError as e:
            print(e)


class FractionJSONAdapter:

    @staticmethod
    def to_json(fraction: MathematicalFraction):
        if not isinstance(fraction, MathematicalFraction):
            raise TypeError(f"Недопустимый тип данных '{fraction.__class__.__name__}', "
                            f"ожидался 'MathematicalFraction'")
        return json.dumps({
            "className": fraction.__class__.__name__,
            "numerator": fraction.numerator,
            "denominator": fraction.denominator
        })

    @staticmethod
    def from_json(data):
        obj = json.loads(data)
        try:
            assert obj["className"] == "MathematicalFraction", "Ошибка обработки данных"
            return MathematicalFraction(obj["numerator"], obj["denominator"])
        except AttributeError:
            print("Ошибка обработки данных")
        except AssertionError as e:
            print(e)
