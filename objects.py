from numpy import (array, int64,
                   dot, cross,
                   matrix, trace,
                   multiply)
from numpy.linalg import norm, inv, det
from math import sin, cos, tan

class Matrix(matrix):
    def __mul__(self, other):
        if isinstance(other, Scalar):                   # проверка принадлежности экземпляра к классу
            return Matrix(self.A.dot(other.val))        # dot скалярное произведение
        else:
            return self.A * other

    @property
    def reverse(self):
    # Обратная матрица
        return Matrix(inv(self.A))

    @property
    def trace(self) -> int64:
    # След матрицы
        return trace(self.A)

    @property
    def det(self):
    # Определитель матрицы
        return det(self.A)

    # Поэлементное произведение
    def mul_element_matrix(self, matrix):
        return Matrix(multiply(self.A, matrix.A))       # полементное произведение массивов x1*x2

    # Умножение вектора на матрицу
    def mul_on_vector(self, vector):
        if vector.len != len(self.A[0]):
            print('\nДЛИНА ВЕКТОРА не совпадает с размерностью введенной матрицы')
            exit()
        else:
            return Matrix(self.A.dot(vector.numpy_repr))


class Vector:
    def __init__(self, data: list) -> None:
        self.__data = array(data)

    def __str__(self) -> str:
        return str(self.__data)

    def __mul__(self, other):
        # Перегрузка оперетора умножения

        if isinstance(other, int) or isinstance(other, float):
            return Vector(self.__data * other)
        elif isinstance(other, Scalar):
            return Vector(self.__data * other.val)
        elif isinstance(other, Vector):
            if len(other.numpy_repr) != self.len:
                raise ValueError('Не совпадает длина векторов')
            else:
                return Vector(self.__data * other.numpy_repr)

    def __add__(self, other):
        # Перегрузка оператора сложения

        if not isinstance(other, Vector):
            raise TypeError('Второй аргумент не является вектором')
        else:
            if len(other.numpy_repr) != self.len:
                raise ValueError('Не совпадает длина векторов')
            else:
                return Vector(self.__data + other.numpy_repr)

    @property
    def numpy_repr(self) -> array:
        # Представление вектора в качестве <<NumPy.array>>

        return self.__data

    @property
    def len(self) -> int:
        # Длина в представлении Python

        return len(self.__data)

    @property
    def vec_len(self) -> float:
        # Длина вектора

        return norm(self.__data)

    def mul_on_matrix(self, matrix):
        # Умножение вектора на матрицу

        if not isinstance(matrix, Matrix):
            raise TypeError('Второй аргумент не является матрицей')
        else:
            if self.len != len(matrix.A[0]):
                raise ValueError('Не совпадает длина')
            else:
                return Vector(
                    matrix.dot(
                        self.__data
                    )
                )

    def scalar_mul(self, other) -> int64:
        # Скалярное умножение векторов
        
        return dot(self.__data, other.numpy_repr)

    def vec_mul(self, other):
        # Векторное произведение трехмерный векторов

        if not isinstance(other, Vector):
            raise TypeError('Второй аргумент не является вектором')
        else:
            if self.len < 3 or other.len < 3:
                raise ValueError('Вектор не является трехмерным')
            else:
                return Vector(cross(self.__data, other.numpy_repr))

    def is_collen(self, second_vector) -> bool:

        if not isinstance(second_vector, Vector):
            raise TypeError('Второй аргумент не является вектором')
        else:
            if second_vector.len != self.len:
                raise ValueError('Длины векторов не равны')
            else:
                second_vector = second_vector.numpy_repr

            results = []

            for i, j in zip(self.__data, second_vector):
                results.append(i / j)

            if len(set(results)) == 1:
                return True

            return False

    def is_ortog(self, second_vector) -> bool:

        if self.scalar_mul(second_vector) == 0:
            return True

        return False

class Scalar:
    def __init__(self, data) -> None:
        self.__data = data

    def __str__(self) -> str:
        return str(self.__data)

    def __add__(self, other):
        if isinstance(other, Scalar):
            return self.__data + other.val
        else:
            return self.__data + other

    def __mul__(self, other):
        if isinstance(other, Scalar):
            return self.__data * other.val
        else:
            return self.__data * other

    @property
    def val(self):
        return self.__data

    @property
    def reverse(self):
        # Инверсия

        return Scalar(-self.__data)

    def pow(self, other):
        # Возведение в степень

        return Scalar(
            self.__data ** other
        )

    def sqrt(self, other):
        # Извлечение корня

        return Scalar(
            self.__data ** (1 / other)
        )

    @property
    def sin(self):
        return Scalar(
            sin(self.__data)
        )

    @property
    def cos(self):
        return Scalar(
            cos(self.__data)
        )

    @property
    def tg(self):
        return Scalar(
            tan(self.__data)
        )

    @property
    def ctg(self):
        return Scalar(
            1 / tan(self.__data)
        )