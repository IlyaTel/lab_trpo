from PyQt5.QtWidgets import (
    QApplication, QMainWindow, 
    QDialog, QTableWidgetItem)
from PyQt5.QtGui import (QIntValidator, 
    QRegExpValidator)
from PyQt5.QtCore import QRegExp 

import numpy as np

from os import getcwd, mkdir, path

from graf import (select, main, 
    M_0, M_1, M_2, M_3, result_matrix, result_trace,
    mul_v_s, two_vector, v_len,
    two_scalar, one_scalar, s_pow)

from objects import (Matrix, Vector, Scalar)


current_index = 0   # глобальный переменная, содержащая индекс выбранной операции

columns_A = 0     # глобальная переменная, содержащая кол-во столбцов матрицы A
lines_A = 0       # глобальная переменная, содержащая кол-во строк матрицы A

columns_B = 0     # глобальная переменная, содержащая кол-во столбцов матрицы B
lines_B = 0       # глобальная переменная, содержащая кол-во строк матрицы B

result = 0      # глобальная переменная, содержащая результат выполненной операции


def modification_matrix(input_matrix: str) -> list:
    # Функция обработки и приведения к нужному виду введенной матрицы

    matrix = []

    for column in input_matrix.split('], ['):
        elements_column = []

        for element in column.split(','):
            if element:
                elements_column.append(float(element))

        if len(elements_column) > 0:
            matrix.append(elements_column)

    return matrix

def modification_vector(input_vector: str) -> list:
    # Функция обработки и приведения к нужному виду введенной матрицы

    vector = []

    for element in input_vector.split(']\n ['):
        if element:
            element = element.replace(".", "")
            vector.append(float(element))

    return vector

def output_result_matrix():
    # Функция вывода результата в виде матрицы

    result_dialog = Result_matrix()
    result_dialog.show()
    result_dialog.exec_()

def output_result_trace():
    # Функция вывода результата одним числом

    result_dialog = Result_trace()
    result_dialog.show()
    result_dialog.exec_()

def output_result_vector():
    # Функция вывода результата вектора

    result_dialog = Result_vector()
    result_dialog.show()
    result_dialog.exec_()

def save_input_A(self):
    # Получение введенных пользователем значений

    global columns_A, lines_A

    # получение введенных чисел пользователем
    data_A = []
    for line in range(lines_A):
        tmp = []
        for column in range(columns_A):
            try:
                tmp.append(self.tableWidget_A.item(line, column).text())
            except:
                tmp.append('0')
        data_A.append(tmp)

    return data_A

def save_input_B(self):
    # Получение введенных пользователем значений

    global columns_B, lines_B

    # получение введенных чисел пользователем
    data_B = []
    for line in range(lines_B):
        tmp = []
        for column in range(columns_B):
            try:
                tmp.append(self.tableWidget_B.item(line, column).text())
            except:
                tmp.append('0')
        data_B.append(tmp)

    return data_B

class Result_matrix(result_matrix.Ui_Dialog, QDialog):
    # Окно вывода результата выполненной операции с матрицей

    def __init__(self):
        QDialog.__init__(self)
        self.setupUi(self)

        global columns_A, lines_A

        self.tableWidget.setColumnCount(columns_A)
        self.tableWidget.setRowCount(lines_A)

        row = 0     # строка
        for i in result:
            col = 0     # столбец

            for j in i:
                j = round(j, 5)     # округление до 5ти знаков
                number = QTableWidgetItem(str(j))
                self.tableWidget.setItem(row, col, number)

                col += 1
            row += 1

        self.generate_csv_files()

    @staticmethod   # Создание csv файла
    def generate_csv_files():

        current_path = getcwd()
        folder_for_csv_files = path.join(current_path, 'result')
        if not path.exists(folder_for_csv_files):
            mkdir(folder_for_csv_files)

        np.savetxt(
            path.join(folder_for_csv_files, 'result_operations.csv'),
            result,
            delimiter=';',
            fmt='%d'
        )

class Result_T_matrix(result_matrix.Ui_Dialog, QDialog):
    # Окно вывода результата выполненной операции транспонирования с матрицей

    def __init__(self):
        QDialog.__init__(self)
        self.setupUi(self)

        global columns_A, lines_A

        self.tableWidget.setColumnCount(lines_A)
        self.tableWidget.setRowCount(columns_A)

        row = 0     # строка
        for i in result:
            col = 0     # столбец

            for j in i:
                j = round(j, 5)     # округление до 5ти знаков
                number = QTableWidgetItem(str(j))
                self.tableWidget.setItem(row, col, number)

                col += 1
            row += 1

        self.generate_csv_files()

    @staticmethod   # Создание csv файла
    def generate_csv_files():

        current_path = getcwd()
        folder_for_csv_files = path.join(current_path, 'result')
        if not path.exists(folder_for_csv_files):
            mkdir(folder_for_csv_files)

        np.savetxt(
            path.join(folder_for_csv_files, 'result_operations.csv'),
            result,
            delimiter=';',
            fmt='%d'
        )

class Result_trace(result_trace.Ui_Dialog, QDialog):
    # Окно вывода результата выполненной следа матрицы

    def __init__(self):
        QDialog.__init__(self)
        self.setupUi(self)

        self.tableWidget.setColumnCount(1)
        self.tableWidget.setRowCount(1)
    
        number = QTableWidgetItem(str(result))
        self.tableWidget.setItem(0, 0, number)

class Result_vector(result_matrix.Ui_Dialog, QDialog):
    # Окно вывода результата выполненной операции с матрицей

    def __init__(self):
        QDialog.__init__(self)
        self.setupUi(self)

        global columns_A, lines_A

        self.tableWidget.setColumnCount(columns_A)
        self.tableWidget.setRowCount(lines_A)

        row = 0     # строка
        for i in result:
            i = round(i, 5)     # округление до 5ти знаков
            number = QTableWidgetItem(str(i))
            self.tableWidget.setItem(row, 0, number)

            row += 1
        
        self.generate_csv_files()

    @staticmethod   # Создание csv файла
    def generate_csv_files():

        current_path = getcwd()
        folder_for_csv_files = path.join(current_path, 'result')
        if not path.exists(folder_for_csv_files):
            mkdir(folder_for_csv_files)

        np.savetxt(
            path.join(folder_for_csv_files, 'result_operations.csv'),
            result,
            delimiter=';',
            fmt='%d'
        )

#----------------------------------------------------------
# Операции с матрицами
#
class Mul_M_on_S(M_0.Ui_Dialog, QDialog):
    # Умножение матрицы на скаляр

    def __init__(self):
        QDialog.__init__(self)
        self.setupUi(self)

        regexp_query = QRegExp('[0-9]*')
        input_validator = QRegExpValidator(regexp_query)
        input_validator.setRegExp(regexp_query)

        self.columns_A.setValidator(input_validator)      # колво столбцов
        self.lines_A.setValidator(input_validator)        # колво строк
        self.scalar.setValidator(input_validator)       # скаляр

        # Нажатие на кнопку 'Заполнить матрицу'
        self.pushButton.clicked.connect(self.size_matrix)

        # Нажатие на кнопку 'Выполнить операцию'
        self.pushButton_2.clicked.connect(self.mul_matrix_on_scalar)

    # Обработка нажатия на кнопку 'Заполнить матрицу'
    def size_matrix(self):
        global columns_A, lines_A

        columns_A = int(self.columns_A.text())
        lines_A = int(self.lines_A.text())

        self.tableWidget_A.setColumnCount(columns_A)
        self.tableWidget_A.setRowCount(lines_A)

    # Обработка нажатия на кнопку 'Выполнить операцию'
    def mul_matrix_on_scalar(self):    
        global result

        # преобразование списка в строку и удаление лишних символов
        matrix_A = str(save_input_A(self)).strip('[]').replace("'", "")
        scalar_b = float(self.scalar.text())

        # .tolist() преобразует матричный тип в список
        result = (Matrix(modification_matrix(matrix_A)) * Scalar(scalar_b)).tolist()

        # Вывод результата в отдельное окно
        output_result_matrix()

class Sum_element_M(M_1.Ui_Dialog, QDialog):
    # Поэлементное сложение

    def __init__(self):
        QDialog.__init__(self)
        self.setupUi(self)

        regexp_query = QRegExp('[0-9]*')
        input_validator = QRegExpValidator(regexp_query)
        input_validator.setRegExp(regexp_query)

        self.columns_A.setValidator(input_validator)      # колво столбцов матрицы A
        self.lines_A.setValidator(input_validator)        # колво строк матрицы B

        self.columns_B.setValidator(input_validator)      # колво столбцов матрицы A
        self.lines_B.setValidator(input_validator)        # колво строк матрицы B

        # Нажатие на кнопку 'Заполнить матрицу'
        self.pushButton.clicked.connect(self.size_matrix)

        # Нажатие на кнопку 'Выполнить операцию'
        self.pushButton_2.clicked.connect(self.sum_matrix)

    # Обработка нажатия на кнопку 'Заполнить матрицу'
    def size_matrix(self):
        global columns_A, lines_A, columns_B, lines_B

        columns_A = int(self.columns_A.text())
        lines_A = int(self.lines_A.text())

        columns_B = int(self.columns_B.text())
        lines_B = int(self.lines_B.text())

        self.tableWidget_A.setColumnCount(columns_A)
        self.tableWidget_A.setRowCount(lines_A)

        self.tableWidget_B.setColumnCount(columns_B)
        self.tableWidget_B.setRowCount(lines_B)

    # Обработка нажатия на кнопку 'Выполнить операцию'
    def sum_matrix(self):
        global result

        # преобразование списка в строку и удаление лишних символов
        matrix_A = str(save_input_A(self)).strip('[]').replace("'", "")
        matrix_B = str(save_input_B(self)).strip('[]').replace("'", "")

        # .tolist() преобразует матричный тип в список
        result = (Matrix(modification_matrix(matrix_A)) 
            + Matrix(modification_matrix(matrix_B))).tolist()

        # Вывод результата в отдельное окно
        output_result_matrix()

class Mul_element_M(M_1.Ui_Dialog, QDialog):
    # Поэлементное произведение

    def __init__(self):
        QDialog.__init__(self)
        self.setupUi(self)

        regexp_query = QRegExp('[0-9]*')
        input_validator = QRegExpValidator(regexp_query)
        input_validator.setRegExp(regexp_query)

        self.columns_A.setValidator(input_validator)      # колво столбцов матрицы A
        self.lines_A.setValidator(input_validator)        # колво строк матрицы B

        self.columns_B.setValidator(input_validator)      # колво столбцов матрицы A
        self.lines_B.setValidator(input_validator)        # колво строк матрицы B

        # Нажатие на кнопку 'Заполнить матрицу'
        self.pushButton.clicked.connect(self.size_matrix)

        # Нажатие на кнопку 'Выполнить операцию'
        self.pushButton_2.clicked.connect(self.mul_element_matrix)

    # Обработка нажатия на кнопку 'Заполнить матрицу'
    def size_matrix(self):
        global columns_A, lines_A, columns_B, lines_B

        columns_A = int(self.columns_A.text())
        lines_A = int(self.lines_A.text())

        columns_B = int(self.columns_B.text())
        lines_B = int(self.lines_B.text())

        self.tableWidget_A.setColumnCount(columns_A)
        self.tableWidget_A.setRowCount(lines_A)

        self.tableWidget_B.setColumnCount(columns_B)
        self.tableWidget_B.setRowCount(lines_B)

    # Обработка нажатия на кнопку 'Выполнить операцию'
    def mul_element_matrix(self):
        global result

        # преобразование списка в строку и удаление лишних символов
        matrix_A = str(save_input_A(self)).strip('[]').replace("'", "")
        matrix_B = str(save_input_B(self)).strip('[]').replace("'", "")

        # .tolist() преобразует матричный тип в список
        result = (Matrix(modification_matrix(matrix_A))
            .mul_element_matrix(Matrix(modification_matrix(matrix_B)))).tolist()

        # Вывод результата в отдельное окно
        output_result_matrix()

class Mul_M_on_V(M_2.Ui_Dialog, QDialog):
    # Умножение вектора на матрицу

    def __init__(self):
        QDialog.__init__(self)
        self.setupUi(self)

        regexp_query = QRegExp('[0-9]*')
        input_validator = QRegExpValidator(regexp_query)
        input_validator.setRegExp(regexp_query)

        self.columns_A.setValidator(input_validator)      # колво столбцов матрицы A
        self.lines_A.setValidator(input_validator)        # колво строк матрицы A

        # Нажатие на кнопку 'Заполнить матрицу'
        self.pushButton.clicked.connect(self.size_matrix)

        # Нажатие на кнопку 'Выполнить операцию'
        self.pushButton_2.clicked.connect(
            self.mul_matrix_on_vector)

    # Обработка нажатия на кнопку 'Заполнить матрицу'
    def size_matrix(self):
        global columns_A, lines_A, columns_B, lines_B

        columns_A = int(self.columns_A.text())
        lines_A = int(self.lines_A.text())

        columns_B = 1
        lines_B = lines_A

        self.tableWidget_A.setColumnCount(columns_A)
        self.tableWidget_A.setRowCount(lines_A)

        self.tableWidget_B.setColumnCount(columns_B)
        self.tableWidget_B.setRowCount(lines_B)

    # Обработка нажатия на кнопку 'Выполнить операцию'
    def mul_matrix_on_vector(self):
        global result

        # преобразование списка в строку и удаление лишних символов
        matrix_A = str(save_input_A(self)).strip('[]').replace("'", "")
        vector = str(save_input_B(self)).strip('[]').replace("'", "")

        # .tolist() преобразует матричный тип в список
        result = (Matrix(modification_matrix(matrix_A))
            .mul_on_vector(Vector(modification_matrix(vector)))).tolist()

        # Вывод результата в отдельное окно
        output_result_matrix()

class Mul_M(M_1.Ui_Dialog, QDialog):
    # Матричное произведение

    def __init__(self):
        QDialog.__init__(self)
        self.setupUi(self)

        regexp_query = QRegExp('[0-9]*')
        input_validator = QRegExpValidator(regexp_query)
        input_validator.setRegExp(regexp_query)

        self.columns_A.setValidator(input_validator)      # колво столбцов матрицы A
        self.lines_A.setValidator(input_validator)        # колво строк матрицы B

        self.columns_B.setValidator(input_validator)      # колво столбцов матрицы A
        self.lines_B.setValidator(input_validator)        # колво строк матрицы B

        # Нажатие на кнопку 'Заполнить матрицу'
        self.pushButton.clicked.connect(self.size_matrix)

        # Нажатие на кнопку 'Выполнить операцию'
        self.pushButton_2.clicked.connect(self.mul_matrix)

    # Обработка нажатия на кнопку 'Заполнить матрицу'
    def size_matrix(self):
        global columns_A, lines_A, columns_B, lines_B

        columns_A = int(self.columns_A.text())
        lines_A = int(self.lines_A.text())

        columns_B = int(self.columns_B.text())
        lines_B = int(self.lines_B.text())

        self.tableWidget_A.setColumnCount(columns_A)
        self.tableWidget_A.setRowCount(lines_A)

        self.tableWidget_B.setColumnCount(columns_B)
        self.tableWidget_B.setRowCount(lines_B)

    # Обработка нажатия на кнопку 'Выполнить операцию'
    def mul_matrix(self):
        global result

        # преобразование списка в строку и удаление лишних символов
        matrix_A = str(save_input_A(self)).strip('[]').replace("'", "")
        matrix_B = str(save_input_B(self)).strip('[]').replace("'", "")

        # .tolist() преобразует матричный тип в список
        result = (Matrix(modification_matrix(matrix_A))
            * Matrix(modification_matrix(matrix_B))).tolist()

        # Вывод результата в отдельное окно
        output_result_matrix()

class Trace_M(M_3.Ui_Dialog, QDialog):
    # Вычисление следа матрицы

    def __init__(self):
        QDialog.__init__(self)
        self.setupUi(self)

        regexp_query = QRegExp('[0-9]*')
        input_validator = QRegExpValidator(regexp_query)
        input_validator.setRegExp(regexp_query)

        self.columns_A.setValidator(input_validator)      # колво столбцов
        self.lines_A.setValidator(input_validator)        # колво строк

        # Нажатие на кнопку 'Заполнить матрицу'
        self.pushButton.clicked.connect(self.size_matrix)

        # Нажатие на кнопку 'Выполнить операцию'
        self.pushButton_2.clicked.connect(self.trace_matrix)

    # Обработка нажатия на кнопку 'Заполнить матрицу'
    def size_matrix(self):
        global columns_A, lines_A

        columns_A = int(self.columns_A.text())
        lines_A = int(self.lines_A.text())

        self.tableWidget_A.setColumnCount(columns_A)
        self.tableWidget_A.setRowCount(lines_A)

    # Обработка нажатия на кнопку 'Выполнить операцию'
    def trace_matrix(self):    
        global result

        # преобразование списка в строку и удаление лишних символов
        matrix_A = str(save_input_A(self)).strip('[]').replace("'", "")

        # .tolist() преобразует матричный тип в список
        result = str((Matrix(modification_matrix(matrix_A)).trace).tolist())
        result = result.replace("[", "")

        # Вывод результата в отдельное окно
        output_result_trace()

class Det_M(M_3.Ui_Dialog, QDialog):
    # Вычисление определителя матрицы

    def __init__(self):
        QDialog.__init__(self)
        self.setupUi(self)

        regexp_query = QRegExp('[0-9]*')
        input_validator = QRegExpValidator(regexp_query)
        input_validator.setRegExp(regexp_query)

        self.columns_A.setValidator(input_validator)      # колво столбцов
        self.lines_A.setValidator(input_validator)        # колво строк

        # Нажатие на кнопку 'Заполнить матрицу'
        self.pushButton.clicked.connect(self.size_matrix)

        # Нажатие на кнопку 'Выполнить операцию'
        self.pushButton_2.clicked.connect(self.det_matrix)

    # Обработка нажатия на кнопку 'Заполнить матрицу'
    def size_matrix(self):
        global columns_A, lines_A

        columns_A = int(self.columns_A.text())
        lines_A = int(self.lines_A.text())

        self.tableWidget_A.setColumnCount(columns_A)
        self.tableWidget_A.setRowCount(lines_A)

    # Обработка нажатия на кнопку 'Выполнить операцию'
    def det_matrix(self):    
        global result

        # преобразование списка в строку и удаление лишних символов
        matrix_A = str(save_input_A(self)).strip('[]').replace("'", "")

        # .tolist() преобразует матричный тип в список
        try:
            result = str((Matrix(modification_matrix(matrix_A)).det).tolist())
            result = result.replace("[", "")

            # Вывод результата в отдельное окно
            output_result_trace()

        except np.linalg.LinAlgError:
            print('Ошибка! Матрица не является квадратной')

class Reverse_M(M_3.Ui_Dialog, QDialog):
    # Вычисление обратной матрицы

    def __init__(self):
        QDialog.__init__(self)
        self.setupUi(self)

        regexp_query = QRegExp('[0-9]*')
        input_validator = QRegExpValidator(regexp_query)
        input_validator.setRegExp(regexp_query)

        self.columns_A.setValidator(input_validator)      # колво столбцов
        self.lines_A.setValidator(input_validator)        # колво строк

        # Нажатие на кнопку 'Заполнить матрицу'
        self.pushButton.clicked.connect(self.size_matrix)

        # Нажатие на кнопку 'Выполнить операцию'
        self.pushButton_2.clicked.connect(self.reverse_matrix)

    # Обработка нажатия на кнопку 'Заполнить матрицу'
    def size_matrix(self):
        global columns_A, lines_A

        columns_A = int(self.columns_A.text())
        lines_A = int(self.lines_A.text())

        self.tableWidget_A.setColumnCount(columns_A)
        self.tableWidget_A.setRowCount(lines_A)

    # Обработка нажатия на кнопку 'Выполнить операцию'
    def reverse_matrix(self):    
        global result

        # преобразование списка в строку и удаление лишних символов
        matrix_A = str(save_input_A(self)).strip('[]').replace("'", "")

        try:
            # .tolist() преобразует матричный тип в список
            result = (Matrix(modification_matrix(matrix_A)).reverse).tolist()

            # Вывод результата в отдельное окно
            output_result_matrix()

        except np.linalg.LinAlgError:
            print('Ошибка! Матрица не является квадратной')

class Transp_M(M_3.Ui_Dialog, QDialog):
    #  Транспонирование матрицы

    def __init__(self):
        QDialog.__init__(self)
        self.setupUi(self)

        regexp_query = QRegExp('[0-9]*')
        input_validator = QRegExpValidator(regexp_query)
        input_validator.setRegExp(regexp_query)

        self.columns_A.setValidator(input_validator)      # колво столбцов
        self.lines_A.setValidator(input_validator)        # колво строк

        # Нажатие на кнопку 'Заполнить матрицу'
        self.pushButton.clicked.connect(self.size_matrix)

        # Нажатие на кнопку 'Выполнить операцию'
        self.pushButton_2.clicked.connect(self.transp_matrix)

    # Обработка нажатия на кнопку 'Заполнить матрицу'
    def size_matrix(self):
        global columns_A, lines_A

        columns_A = int(self.columns_A.text())
        lines_A = int(self.lines_A.text())

        self.tableWidget_A.setColumnCount(columns_A)
        self.tableWidget_A.setRowCount(lines_A)

    # Обработка нажатия на кнопку 'Выполнить операцию'
    def transp_matrix(self):    
        global result

        # преобразование списка в строку и удаление лишних символов
        matrix_A = str(save_input_A(self)).strip('[]').replace("'", "")

        # .tolist() преобразует матричный тип в список
        result = (Matrix(modification_matrix(matrix_A)).T).tolist()

        # Вывод результата в отдельное окно
        result_dialog = Result_T_matrix()
        result_dialog.show()
        result_dialog.exec_()
#
# Операции с матрицами
#----------------------------------------------------------


#----------------------------------------------------------
# Операции с векторами
#
class Mul_V_on_S(mul_v_s.Ui_Dialog, QDialog):
    # Умножение вектора на скаляр

    def __init__(self):
        QDialog.__init__(self)
        self.setupUi(self)

        regexp_query = QRegExp('[0-9]*')
        input_validator = QRegExpValidator(regexp_query)
        input_validator.setRegExp(regexp_query)

        self.lines_A.setValidator(input_validator)        # колво строк
        self.scalar.setValidator(input_validator)       # скаляр

        # Нажатие на кнопку 'Заполнить матрицу'
        self.pushButton.clicked.connect(self.size_matrix)

        # Нажатие на кнопку 'Выполнить операцию'
        self.pushButton_2.clicked.connect(self.mul_vector_on_scalar)

    # Обработка нажатия на кнопку 'Заполнить матрицу'
    def size_matrix(self):
        global columns_A, lines_A

        columns_A = 1
        lines_A = int(self.lines_A.text())

        self.tableWidget_A.setColumnCount(columns_A)
        self.tableWidget_A.setRowCount(lines_A)

    # Обработка нажатия на кнопку 'Выполнить операцию'
    def mul_vector_on_scalar(self):    
        global result

        # преобразование списка в строку и удаление лишних символов
        vector = str(save_input_A(self)).strip('[]').replace("'", "")
        scalar_b = float(self.scalar.text())

        # .tolist() преобразует матричный тип в список
        result = modification_vector(str(Vector(modification_matrix(vector))
            * Scalar(scalar_b)).strip('[]'))
    
        # Вывод результата в отдельное окно
        output_result_vector()

class Sum_element_V(two_vector.Ui_Dialog, QDialog):
    # Поэлементное сложение векторов

    def __init__(self):
        QDialog.__init__(self)
        self.setupUi(self)

        regexp_query = QRegExp('[0-9]*')
        input_validator = QRegExpValidator(regexp_query)
        input_validator.setRegExp(regexp_query)

        self.lines.setValidator(input_validator)        # колво строк векторов

        # Нажатие на кнопку 'Заполнить вектора'
        self.pushButton.clicked.connect(self.size_matrix)

        # Нажатие на кнопку 'Выполнить операцию'
        self.pushButton_2.clicked.connect(self.sum_element_vector)

    # Обработка нажатия на кнопку 'Заполнить матрицу'
    def size_matrix(self):
        global columns_A, lines_A, columns_B, lines_B

        columns_A = 1
        lines_A = int(self.lines.text())

        columns_B = 1
        lines_B = int(self.lines.text())

        self.tableWidget_A.setColumnCount(columns_A)
        self.tableWidget_A.setRowCount(lines_A)

        self.tableWidget_B.setColumnCount(columns_B)
        self.tableWidget_B.setRowCount(lines_B)

    # Обработка нажатия на кнопку 'Выполнить операцию'
    def sum_element_vector(self):
        global result

        # преобразование списка в строку и удаление лишних символов
        vector_A = str(save_input_A(self)).strip('[]').replace("'", "")
        vector_B = str(save_input_B(self)).strip('[]').replace("'", "")

        # .tolist() преобразует матричный тип в список
        result = modification_vector(str(Vector(modification_matrix(vector_A))
            + Vector(modification_matrix(vector_B))).strip('[]'))

        # Вывод результата в отдельное окно
        output_result_vector()

class Mul_element_V(two_vector.Ui_Dialog, QDialog):
    # Поэлементное произведение векторов

    def __init__(self):
        QDialog.__init__(self)
        self.setupUi(self)

        regexp_query = QRegExp('[0-9]*')
        input_validator = QRegExpValidator(regexp_query)
        input_validator.setRegExp(regexp_query)

        self.lines.setValidator(input_validator)        # колво строк векторов

        # Нажатие на кнопку 'Заполнить вектора'
        self.pushButton.clicked.connect(self.size_matrix)

        # Нажатие на кнопку 'Выполнить операцию'
        self.pushButton_2.clicked.connect(self.sum_element_vector)

    # Обработка нажатия на кнопку 'Заполнить матрицу'
    def size_matrix(self):
        global columns_A, lines_A, columns_B, lines_B

        columns_A = 1
        lines_A = int(self.lines.text())

        columns_B = 1
        lines_B = int(self.lines.text())

        self.tableWidget_A.setColumnCount(columns_A)
        self.tableWidget_A.setRowCount(lines_A)

        self.tableWidget_B.setColumnCount(columns_B)
        self.tableWidget_B.setRowCount(lines_B)

    # Обработка нажатия на кнопку 'Выполнить операцию'
    def sum_element_vector(self):
        global result

        # преобразование списка в строку и удаление лишних символов
        vector_A = str(save_input_A(self)).strip('[]').replace("'", "")
        vector_B = str(save_input_B(self)).strip('[]').replace("'", "")

        # .tolist() преобразует матричный тип в список
        result = modification_vector(str(Vector(modification_matrix(vector_A))
            * Vector(modification_matrix(vector_B))).strip('[]'))

        # Вывод результата в отдельное окно
        output_result_vector()

class V_len(v_len.Ui_Dialog, QDialog):
    # длина вектора

    def __init__(self):
        QDialog.__init__(self)
        self.setupUi(self)

        regexp_query = QRegExp('[0-9]*')
        input_validator = QRegExpValidator(regexp_query)
        input_validator.setRegExp(regexp_query)

        self.lines.setValidator(input_validator)        # колво строк

        # Нажатие на кнопку 'Заполнить матрицу'
        self.pushButton.clicked.connect(self.size_matrix)

        # Нажатие на кнопку 'Выполнить операцию'
        self.pushButton_2.clicked.connect(self.v_len)

    # Обработка нажатия на кнопку 'Заполнить матрицу'
    def size_matrix(self):
        global columns_A, lines_A

        columns_A = 1
        lines_A = int(self.lines.text())

        self.tableWidget_A.setColumnCount(columns_A)
        self.tableWidget_A.setRowCount(lines_A)

    # Обработка нажатия на кнопку 'Выполнить операцию'
    def v_len(self):    
        global result

        # преобразование списка в строку и удаление лишних символов
        vector = str(save_input_A(self)).strip('[]').replace("'", "")

        result = modification_vector(str(Vector(modification_matrix(vector))
           .vec_len).strip('[]'))
    
        # Вывод результата в отдельное окно
        output_result_vector()
#
# Операции с векторами
#----------------------------------------------------------


#----------------------------------------------------------
# Операции со скалярами
#
class Sum_S(two_scalar.Ui_Dialog, QDialog):
    # Инверсия

    def __init__(self):
        QDialog.__init__(self)
        self.setupUi(self)

        regexp_query = QRegExp('[0-9]*')
        input_validator = QRegExpValidator(regexp_query)
        input_validator.setRegExp(regexp_query)

        self.scalar.setValidator(input_validator)       # скаляр
        self.scalar_2.setValidator(input_validator)       # скаляр

        # Нажатие на кнопку 'Выполнить операцию'
        self.pushButton_2.clicked.connect(self.sum_s)

    # Обработка нажатия на кнопку 'Выполнить операцию'
    def sum_s(self):    
        global result

        scalar_a = float(self.scalar.text())
        scalar_b = float(self.scalar_2.text())

        result = Scalar(scalar_a) + Scalar(scalar_b)

        # Вывод результата в отдельное окно
        output_result_trace()

class Inv_S(one_scalar.Ui_Dialog, QDialog):
    # Инверсия

    def __init__(self):
        QDialog.__init__(self)
        self.setupUi(self)

        regexp_query = QRegExp('[0-9]*')
        input_validator = QRegExpValidator(regexp_query)
        input_validator.setRegExp(regexp_query)

        self.scalar.setValidator(input_validator)       # скаляр

        # Нажатие на кнопку 'Выполнить операцию'
        self.pushButton_2.clicked.connect(self.inv_s)

    # Обработка нажатия на кнопку 'Выполнить операцию'
    def inv_s(self):    
        global result

        scalar_a = float(self.scalar.text())

        result = Scalar(scalar_a).reverse
    
        # Вывод результата в отдельное окно
        output_result_trace()

class Mul_S(two_scalar.Ui_Dialog, QDialog):
    # Произведение

    def __init__(self):
        QDialog.__init__(self)
        self.setupUi(self)

        regexp_query = QRegExp('[0-9]*')
        input_validator = QRegExpValidator(regexp_query)
        input_validator.setRegExp(regexp_query)

        self.scalar.setValidator(input_validator)       # скаляр
        self.scalar_2.setValidator(input_validator)       # скаляр

        # Нажатие на кнопку 'Выполнить операцию'
        self.pushButton_2.clicked.connect(self.mul_s)

    # Обработка нажатия на кнопку 'Выполнить операцию'
    def mul_s(self):    
        global result

        scalar_a = float(self.scalar.text())
        scalar_b = float(self.scalar_2.text())

        result = Scalar(scalar_a) * Scalar(scalar_b)
    
        # Вывод результата в отдельное окно
        output_result_trace()

class Pow_S(s_pow.Ui_Dialog, QDialog):
    # Степень

    def __init__(self):
        QDialog.__init__(self)
        self.setupUi(self)

        regexp_query = QRegExp('[0-9]*')
        input_validator = QRegExpValidator(regexp_query)
        input_validator.setRegExp(regexp_query)

        self.scalar.setValidator(input_validator)       # скаляр
        self.scalar_2.setValidator(input_validator)       # степень

        # Нажатие на кнопку 'Выполнить операцию'
        self.pushButton_2.clicked.connect(self.pow_s)

    # Обработка нажатия на кнопку 'Выполнить операцию'
    def pow_s(self):    
        global result

        scalar_a = float(self.scalar.text())
        pow_value = float(self.scalar_2.text())

        result = Scalar(scalar_a).pow(pow_value)

        # Вывод результата в отдельное окно
        output_result_trace()

class Sqrt_S(s_pow.Ui_Dialog, QDialog):
    # Корень

    def __init__(self):
        QDialog.__init__(self)
        self.setupUi(self)

        regexp_query = QRegExp('[0-9]*')
        input_validator = QRegExpValidator(regexp_query)
        input_validator.setRegExp(regexp_query)

        self.scalar.setValidator(input_validator)       # скаляр
        self.scalar_2.setValidator(input_validator)       # степень

        # Нажатие на кнопку 'Выполнить операцию'
        self.pushButton_2.clicked.connect(self.pow_s)

    # Обработка нажатия на кнопку 'Выполнить операцию'
    def pow_s(self):    
        global result

        scalar_a = float(self.scalar.text())
        sqrt_value = float(self.scalar_2.text())

        result = Scalar(scalar_a).sqrt(sqrt_value)
    
        # Вывод результата в отдельное окно
        output_result_trace()

class Sin_S(one_scalar.Ui_Dialog, QDialog):
    # Синус

    def __init__(self):
        QDialog.__init__(self)
        self.setupUi(self)

        regexp_query = QRegExp('[0-9]*')
        input_validator = QRegExpValidator(regexp_query)
        input_validator.setRegExp(regexp_query)

        self.scalar.setValidator(input_validator)       # скаляр

        # Нажатие на кнопку 'Выполнить операцию'
        self.pushButton_2.clicked.connect(self.inv_s)

    # Обработка нажатия на кнопку 'Выполнить операцию'
    def inv_s(self):    
        global result

        scalar_a = float(self.scalar.text())

        result = Scalar(scalar_a).sin
    
        # Вывод результата в отдельное окно
        output_result_trace()

class Cos_S(one_scalar.Ui_Dialog, QDialog):
    # Косинус

    def __init__(self):
        QDialog.__init__(self)
        self.setupUi(self)

        regexp_query = QRegExp('[0-9]*')
        input_validator = QRegExpValidator(regexp_query)
        input_validator.setRegExp(regexp_query)

        self.scalar.setValidator(input_validator)       # скаляр

        # Нажатие на кнопку 'Выполнить операцию'
        self.pushButton_2.clicked.connect(self.inv_s)

    # Обработка нажатия на кнопку 'Выполнить операцию'
    def inv_s(self):    
        global result

        scalar_a = float(self.scalar.text())

        result = Scalar(scalar_a).cos
    
        # Вывод результата в отдельное окно
        output_result_trace()

class Tg_S(one_scalar.Ui_Dialog, QDialog):
    # Тангенс

    def __init__(self):
        QDialog.__init__(self)
        self.setupUi(self)

        regexp_query = QRegExp('[0-9]*')
        input_validator = QRegExpValidator(regexp_query)
        input_validator.setRegExp(regexp_query)

        self.scalar.setValidator(input_validator)       # скаляр

        # Нажатие на кнопку 'Выполнить операцию'
        self.pushButton_2.clicked.connect(self.inv_s)

    # Обработка нажатия на кнопку 'Выполнить операцию'
    def inv_s(self):    
        global result

        scalar_a = float(self.scalar.text())

        result = Scalar(scalar_a).tg
    
        # Вывод результата в отдельное окно
        output_result_trace()

class Ctg_S(one_scalar.Ui_Dialog, QDialog):
    # Котангенс

    def __init__(self):
        QDialog.__init__(self)
        self.setupUi(self)

        regexp_query = QRegExp('[0-9]*')
        input_validator = QRegExpValidator(regexp_query)
        input_validator.setRegExp(regexp_query)

        self.scalar.setValidator(input_validator)       # скаляр

        # Нажатие на кнопку 'Выполнить операцию'
        self.pushButton_2.clicked.connect(self.inv_s)

    # Обработка нажатия на кнопку 'Выполнить операцию'
    def inv_s(self):    
        global result

        scalar_a = float(self.scalar.text())

        result = Scalar(scalar_a).ctg
    
        # Вывод результата в отдельное окно
        output_result_trace()
#
# Операции со скалярами
#----------------------------------------------------------


#----------------------------------------------------------
# Основные окна
# 
class MainApp_M(main.Ui_Dialog, QDialog):
    def __init__(self):
        QDialog.__init__(self)
        self.setupUi(self)

        # Добавление значений для выбора операций
        self.comboBox.addItems(['Умножение матрицы на скаляр',
            'Поэлементное сложение', 'Поэлементное произведение',
            'Умножение вектора на матрицу', 'Матричное произведение',
            'Вычисление следа матрицы', 'Вычисление определителя матрицы',
            'Вычисление обратной матрицы', 'Транспонирование матрицы'])
        
        self.comboBox.highlighted[int].connect(self.save_index)

        self.generate_and_calculate.clicked.connect(self.enter)     # Нажатие на кнопку

    # Сохранение индекса выбранной операции
    def save_index(self, index):
        global current_index
        current_index = index

    # Обработка нажатия на кнопку "Выбрать данную операцию"
    def enter(self):
        global current_index

        if current_index == 0:
            win = Mul_M_on_S()
            win.show()
            win.exec_()

        elif current_index == 1:
            win = Sum_element_M()
            win.show()
            win.exec_()

        elif current_index == 2:
            win = Mul_element_M()
            win.show()
            win.exec_()

        elif current_index == 3:
            win = Mul_M_on_V()
            win.show()
            win.exec_()

        elif current_index == 4:
            win = Mul_M()
            win.show()
            win.exec_()

        elif current_index == 5:
            win = Trace_M()
            win.show()
            win.exec_()

        elif current_index == 6:
            win = Det_M()
            win.show()
            win.exec_()

        elif current_index == 7:
            win = Reverse_M()
            win.show()
            win.exec_()

        elif current_index == 8:
            win = Transp_M()
            win.show()
            win.exec_()
            
        else:
            exit()

class MainApp_V(main.Ui_Dialog, QDialog):
    def __init__(self):
        QDialog.__init__(self)
        self.setupUi(self)

        # Добавление значений для выбора операций
        self.comboBox.addItems(['Умножение вектора на скаляр',
            'Поэлементное сложение', 'Поэлементное произведение',
            'Умножение вектора на матрицу', 'Вычисление длины вектора',])

        self.comboBox.highlighted[int].connect(self.save_index)

        self.generate_and_calculate.clicked.connect(self.enter)     # Нажатие на кнопку

    # Сохранение индекса выбранной операции
    def save_index(self, index):
        global current_index
        current_index = index

    # Обработка нажатия на кнопку "Выбрать данную операцию"
    def enter(self):
        global current_index

        if current_index == 0:
            win = Mul_V_on_S()
            win.show()
            win.exec_()

        elif current_index == 1:
            win = Sum_element_V()
            win.show()
            win.exec_()

        elif current_index == 2:
            win = Mul_element_V()
            win.show()
            win.exec_()

        elif current_index == 3:        # тот же класс, что и в блоке с матрицами,
            win = Mul_M_on_V()          # так как действие одно и то же
            win.show()
            win.exec_()

        elif current_index == 4:
            win = V_len()
            win.show()
            win.exec_()

        else:
            exit()

class MainApp_S(main.Ui_Dialog, QDialog):
    def __init__(self):
        QDialog.__init__(self)
        self.setupUi(self)

        # Добавление значений для выбора операций
        self.comboBox.addItems(['Сумма',
            'Инверсия', 'Произведение',
            'Возведение в степень', 'Вычисление корня',
            'Вычисление синуса', 'Вычисление косинуса',
            'Вычисление тангенса', 'Вычисление котангенса'])

        self.comboBox.highlighted[int].connect(self.save_index)

        self.generate_and_calculate.clicked.connect(self.enter)     # Нажатие на кнопку

    # Сохранение индекса выбранной операции
    def save_index(self, index):
        global current_index
        current_index = index

    # Обработка нажатия на кнопку "Выбрать данную операцию"
    def enter(self):
        global current_index

        if current_index == 0:
            win = Sum_S()
            win.show()
            win.exec_()

        elif current_index == 1:
            win = Inv_S()
            win.show()
            win.exec_()

        elif current_index == 2:
            win = Mul_S()
            win.show()
            win.exec_()

        elif current_index == 3:
            win = Pow_S()
            win.show()
            win.exec_()

        elif current_index == 4:
            win = Sqrt_S()
            win.show()
            win.exec_()

        elif current_index == 5:
            win = Sin_S()
            win.show()
            win.exec_()

        elif current_index == 6:
            win = Cos_S()
            win.show()
            win.exec_()

        elif current_index == 7:
            win = Tg_S()
            win.show()
            win.exec_()

        elif current_index == 8:
            win = Ctg_S()
            win.show()
            win.exec_()
            
        else:
            exit()

class Select(select.Ui_MainWindow, QMainWindow):
    def __init__(self):
        super(Select, self).__init__()
        self.setupUi(self)

        self.comboBox.addItems(['Матрицы', 'Вектора', 'Скаляры'])
        self.comboBox.highlighted[int].connect(self.save_index)

        self.generate_and_calculate.clicked.connect(self.enter)     # Нажатие на кнопку

        # Сохранение индекса выбранной операции
    def save_index(self, index):
        global current_index
        current_index = index
        
    def enter(self):
        global current_index

        if current_index == 0:
            win = MainApp_M()
            win.show()
            win.exec_()

        elif current_index == 1:
            win = MainApp_V()
            win.show()
            win.exec_()

        elif current_index == 2:
            win = MainApp_S()
            win.show()
            win.exec_()
            
        else:
            exit()
# 
# Основные окна
#----------------------------------------------------------


if __name__ == '__main__':
    app = QApplication([])
    main_app = Select()
    main_app.show()
    exit(app.exec_())