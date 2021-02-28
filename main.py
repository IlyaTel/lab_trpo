from argparse import ArgumentParser
from sys import stderr

from objects import Matrix, Vector, Scalar

from numpy.linalg import LinAlgError


class ModifiedArgParser(ArgumentParser):
    def exit_with_error(self, error_text):
        print(error_text, file=stderr)
        exit(1)

    def print_help_and_exit(self):
        self.print_help()
        exit(0)


def modification_matrix(input_matrix: str) -> list:
    matrix = []

    for column in input_matrix.split(';'):      # столбец до разделителся ";"
        elemens_column = []

        for element in column.split(','):       # элемент до разделителя ";" 
            if element:
                elemens_column.append(float(element))

        if len(elemens_column) > 0:
            matrix.append(elemens_column)

    return matrix


if __name__ == '__main__':
    parser = ModifiedArgParser(prog='Lab1_TRPO_Telegin_576')
    subparsers = parser.add_subparsers(help='BLABLABLA')

    operations_with_matrix = subparsers.add_parser('matrix', 
        help='Операции с матрицами')
    operations_with_matrix.add_argument('-ms', '--mul_matrix_on_scalar', 
        action='store_true', help='Умножение матрицы на скаляр')
    operations_with_matrix.add_argument('-s', '--sum_martix',
        action='store_true', help='Поэлементное сложение')
    operations_with_matrix.add_argument('-m', '--mul_element_matrix',
        action='store_true', help='Поэлементное произведение')
    operations_with_matrix.add_argument('-mv', '--mul_matrix_on_vector',
        action='store_true', help='Умножение вектора на матрицу')
    operations_with_matrix.add_argument('-mm', '--mul_matrix',
        action='store_true', help='Матричное произведение')
    operations_with_matrix.add_argument('-mt', '--trace_matrix',
        action='store_true', help='Вычисление следа матрицы')
    operations_with_matrix.add_argument('-md', '--det_matrix',
        action='store_true', help='Вычисление определителя матрицы')
    operations_with_matrix.add_argument('-mr', '--reverse_matrix',
        action='store_true', help='Вычисление обратной матрицы')
    operations_with_matrix.add_argument('-mtr', '--transp_matrix',
        action='store_true', help='Транспонирование матрицы')

    operations_with_vector = subparsers.add_parser('vector',
        help='Операции с векторами')
    operations_with_vector.add_argument('-vs', '--mul_vector_on_scalar',
        action='store_true', help='Умножение вектора на скаляр')
    operations_with_vector.add_argument('-s', '--sum_vector',
        action='store_true', help='Поэлементное сложение')
    operations_with_vector.add_argument('-m', '--mul_element_vector',
        action='store_true', help='Поэлементное умножение')
    operations_with_vector.add_argument('-mv', '--mul_matrix_on_vector',
        action='store_true', help='Умножение вектора на матрицу')
    operations_with_vector.add_argument('-sm', '--mul_scalar',
        action='store_true', help='Скалярное произведение')
    operations_with_vector.add_argument('-vm', '--mul_vector',
        action='store_true', help='Векторное произведение')
    operations_with_vector.add_argument('-lv', '--len_vector',
        action='store_true', help='Вычисление длины вектора')
    operations_with_vector.add_argument('-l', '--line_vector',
        action='store_true', help='Проверка сонаправленности векторов')
    operations_with_vector.add_argument('-o', '--ortog_vector',
        action='store_true', help='Проверка векторов на ортогональность')

    operations_with_scalar = subparsers.add_parser('scalar',
        help='Операции со скалярами')
    operations_with_scalar.add_argument('-s', '--sum_scalar',
        nargs=2, type=float, help='Сумма скаляров')
    operations_with_scalar.add_argument('-r', '--reverse_scalar',
        nargs=1, type=float, help='Инверсия скаляра')
    operations_with_scalar.add_argument('-m', '--mul_scalar',
        nargs=2, type=float, help='Произведение скаляров')
    operations_with_scalar.add_argument('-p', '--pow_scalar',
        nargs=2, type=float, help='Возведение в степень скаляра')
    operations_with_scalar.add_argument('-sqrt', '--sqrt_scalar',
        nargs=2, type=float, help='Вычисление корня скаляра')
    operations_with_scalar.add_argument('-sin', '--sin_scalar',
        type=float, help='Синус скаляра')
    operations_with_scalar.add_argument('-cos', '--cos_scalar',
        type=float, help='Косинус скаляра')
    operations_with_scalar.add_argument('-tg', '--tg_scalar',
        type=float, help='Тангенс скаляра')
    operations_with_scalar.add_argument('-ctg', '--ctg_scalar',
        type=float, help='Котангенс скаляра')

    args = parser.parse_args()

    #---------------------------------#
    #                                 #
    #       Операции с матрицами      #
    #                                 #
    #---------------------------------#

    # Умножение матрицы на скаляр
    if args.mul_matrix_on_scalar:
    # if getattr(args, 'mul_matrix_on_scalar', False):
        scalar_b = float(input('Введите скаляр b: '))

        print('''Введите матрицу A в следующем виде:
        1, 2, 3; - 1-ая строка
        4, 5, 6; - 2-ая строка
        7, 8, 9; - 3-ья строка и так далее

        1  2  3
        4  5  6
        7  8  9
        ''')

        matrix_A = input('Введите матрицу A: ')

        print(Matrix(modification_matrix(matrix_A)) * Scalar(scalar_b))

    # Поэлементное сложение
    elif args.sum_martix:
        print('''Введите матрицы в следующем виде:
        1, 2, 3; - 1-ая строка
        4, 5, 6; - 2-ая строка
        7, 8, 9; - 3-ья строка и так далее

        1  2  3
        4  5  6
        7  8  9
        ''')

        matrix_A = input('Введите матрицу A: ')
        matrix_B = input('Введите матрицу B: ')

        print(Matrix(modification_matrix(matrix_A)) 
            + Matrix(modification_matrix(matrix_B)))
    
    # Поэлементное произведение
    elif args.mul_element_matrix:
        print('''Введите матрицы в следующем виде:
        1, 2, 3; - 1-ая строка
        4, 5, 6; - 2-ая строка
        7, 8, 9; - 3-ья строка и так далее

        1  2  3
        4  5  6
        7  8  9
        ''')

        matrix_A = input('Введите матрицу A: ')
        matrix_B = input('Введите матрицу B: ')

        print(Matrix(modification_matrix(matrix_A))
            .mul_by_element(Matrix(modification_matrix(matrix_B))))

    # Умножение вектора на матрицу
    elif args.mul_matrix_on_vector:
        print('''Введите матрицу A в следующем виде:
        1, 2, 3; - 1-ая строка
        4, 5, 6; - 2-ая строка
        7, 8, 9; - 3-ья строка и так далее

        1  2  3
        4  5  6
        7  8  9
        ''')

        matrix_A = input('Введите матрицу A: ')
        vector = input('Введите вектор (элементы через запятую): ')

        print(Matrix(modification_matrix(matrix_A))
            .mul_on_vector(Vector([float(i) for i in vector.split(',')])))

    # Матричное произведение
    elif args.mul_matrix:
        print('''Введите матрицы в следующем виде:
        1, 2, 3; - 1-ая строка
        4, 5, 6; - 2-ая строка
        7, 8, 9; - 3-ья строка и так далее

        1  2  3
        4  5  6
        7  8  9
        ''')

        matrix_A = input('Введите матрицу A: ')
        matrix_B = input('Введите матрицу B: ')

        try:
            print(Matrix(modification_matrix(matrix_A)) 
                * Matrix(modification_matrix(matrix_B)))
                
        except ValueError:
            parser.exit_with_error(
                '\nЧИСЛО СТОЛБЦОВ матрицы A не совпадает с числом строк матрицы B')

    # Вычисление следа матрицы
    elif args.trace_matrix:
        print('''Введите матрицу A в следующем виде:
        1, 2, 3; - 1-ая строка
        4, 5, 6; - 2-ая строка
        7, 8, 9; - 3-ья строка и так далее

        1  2  3
        4  5  6
        7  8  9
        ''')

        matrix_A = input('Введите матрицу A: ')

        print(Matrix(modification_matrix(matrix_A)).trace)

    # Вычисление определителя матрицы
    elif args.det_matrix:
        print('''Введите матрицу A в следующем виде:
        1, 2, 3; - 1-ая строка
        4, 5, 6; - 2-ая строка
        7, 8, 9; - 3-ья строка и так далее

        1  2  3
        4  5  6
        7  8  9
        ''')

        matrix_A = input('Введите матрицу A: ')

        try:
            print(Matrix(modification_matrix(matrix_A)).det)

        except LinAlgError:
            parser.exit_with_error('\nМатрица A должна быть квадратной')

    # Вычисление обратной матрицы
    elif args.reverse_matrix:
        print('''Введите матрицу A в следующем виде:
        1, 2, 3; - 1-ая строка
        4, 5, 6; - 2-ая строка
        7, 8, 9; - 3-ья строка и так далее

        1  2  3
        4  5  6
        7  8  9
        ''')

        matrix_A = input('Введите матрицу A: ')

        try:
            print(Matrix(modification_matrix(matrix_A)).reverse)

        except LinAlgError:
            parser.exit_with_error('\nМатрица должна быть квадратной')

    # Транспонирование матрицы
    elif args.transp_matrix:
        print('''Введите матрицу A в следующем виде:
        1, 2, 3; - 1-ая строка
        4, 5, 6; - 2-ая строка
        7, 8, 9; - 3-ья строка и так далее

        1  2  3
        4  5  6
        7  8  9
        ''')

        matrix_A = input('Введите матрицу A: ')

        print(Matrix(modification_matrix(matrix_A)).T)

