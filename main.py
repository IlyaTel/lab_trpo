from PyQt5.QtWidgets import (
    QApplication, QMainWindow, 
    QDialog, QTableWidgetItem)
from PyQt5.QtGui import (QIntValidator, 
    QRegExpValidator)
from PyQt5.QtCore import QRegExp 

from graf import (main, error, M_0, result_matrix)

from objects import (Matrix, Vector, Scalar)


current_index = 0

columns = 0
lines = 0

result = 0


def modification_matrix(input_matrix: str) -> list:
    matrix = []

    for column in input_matrix.split('], ['):
        elements_column = []

        for element in column.split(','):
            if element:
                elements_column.append(float(element))

        if len(elements_column) > 0:
            matrix.append(elements_column)

    return matrix

class Result_matrix(result_matrix.Ui_Dialog, QDialog):
    # Окно вывода результата выполненной операции с матрицей
    def __init__(self):
        QDialog.__init__(self)
        self.setupUi(self)

        global columns, lines

        self.tableWidget.setColumnCount(columns)
        self.tableWidget.setRowCount(lines)

        row = 0     # строка
        for i in result:
            col = 0     # столбец
            print('i = ', i)

            for j in i:
                print('j = ', j)
                number = QTableWidgetItem(str(j))
                print('n = ', number)
                self.tableWidget.setItem(row, col, number)

                col += 1
            row += 1

class Error(error.Ui_Dialog, QDialog):
    # Окно ошибки

    def __init__(self):
        QDialog.__init__(self)
        self.setupUi(self)


class Mul_M_on_S(M_0.Ui_Dialog, QDialog):
    # Окно нулевой операции

    def __init__(self):
        QDialog.__init__(self)
        self.setupUi(self)

        regexp_query = QRegExp('[1-9]*')
        input_validator = QRegExpValidator(regexp_query)
        input_validator.setRegExp(regexp_query)

        self.columns.setValidator(input_validator)      # колво столбцов
        self.lines.setValidator(input_validator)        # колво строк
        self.scalar.setValidator(input_validator)       # скаляр

        self.pushButton.clicked.connect(self.size_matrix)     # Нажатие на кнопку
        self.pushButton_2.clicked.connect(self.mul_matrix_on_scalar)

    # Обработка нажатия на кнопку, размерность матрицы
    def size_matrix(self):
        global columns, lines

        columns = int(self.columns.text())
        lines = int(self.lines.text())

        self.tableWidget.setColumnCount(columns)
        self.tableWidget.setRowCount(lines)

    #  Обработка нажатия на кнопку, операция умножение матрицы на скаляр
    def mul_matrix_on_scalar(self):    
        global columns, lines, result

        # получение введенных чисел пользователем
        data = []
        for line in range(lines):
            tmp = []
            for column in range(columns):
                try:
                    tmp.append(self.tableWidget.item(line, column).text())
                except:
                    tmp.append('0')
            data.append(tmp)
        for i in data: 
            print(i)

        # преобразование списка в строку и удаление лишних символов
        matrix_A = str(data).strip('[]').replace("'", "")
        scalar_b = float(self.scalar.text())

        # .tolist() преобразует матричный тип в список
        result = (Matrix(modification_matrix(matrix_A)) * Scalar(scalar_b)).tolist()

        result_dialog = Result_matrix()
        result_dialog.show()
        result_dialog.exec_()


class MainApp(main.Ui_MainWindow, QMainWindow):
    def __init__(self):
        super(MainApp, self).__init__()
        self.setupUi(self)

        # Добавление значений для выбора операций
        # self.comboBox.addItem('Умножение матрицы на скаляр')
        # self.comboBox.addItem('Поэлементное сложение')
        # self.comboBox.addItem('Поэлементное произведение')

        self.comboBox.addItems(['Умножение матрицы на скаляр',
            'Поэлементное сложение', 'Поэлементное произведение'])

        self.comboBox.highlighted[int].connect(self.save_index)

        self.generate_and_calculate.clicked.connect(self.enter)     # Нажатие на кнопку
        # self.generate_and_calculate.clicked.connect(self.NAME.close)

    # Сохранение индекса выбранной операции
    def save_index(self, index):
        global current_index
        current_index = index
        print(current_index)

    # Обработка нажатия на кнопку "Выбрать данную операцию"
    def enter(self):
        # print(self.comboBox.currentData())
        # print(self.comboBox.setCurrentIndex(1)) 
        global current_index

        if current_index == 0:
            win = Mul_M_on_S()
            win.show()
            win.exec_()
            
        else:
            exit()


if __name__ == '__main__':
    app = QApplication([])
    main_app = MainApp()
    main_app.show()
    exit(app.exec_())
