import math

def area(r):
'''
Принимает число r, возвращает площадь круга.
    Параметры:
        r (int): радиус окружности в формате десятичного числа
    Возращаемое значение:
        Площадь окружности
    Пример:
        area(4) -> ~(3 * 4 * 4) ~= 27 
''' 
    return math.pi * r * r

def perimeter(r):
'''
Принимает число r, возвращает длину окружности.
    Параметры:
        r (int): радиус окружности в формате десятичного числа
    Возращаемое значение:
        Длина окружности
    Пример:
        area(4) -> ~(2 * 3 * 4) ~= 24 
''' 
    return 2 * math.pi * r
