#!/usr/bin/env python3
# coding=utf-8

import re
import sys

from PyQt5 import QtGui
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUi

list_of_numbers = []
mas = []


class Main(QDialog):
    def __init__(self):
        super(Main, self).__init__()
        loadUi('uis/main.ui', self)

        self.setWindowTitle('Работа с массивами и файлами в Python')
        self.setWindowIcon(QtGui.QIcon('images/logo.png'))

        self.btn_upload_data.clicked.connect(self.upload_data_from_file)
        self.btn_process_data.clicked.connect(self.process_data)
        self.btn_save_data.clicked.connect(self.save_data_in_file)
        self.btn_clear.clicked.connect(self.clear)

    def upload_data_from_file(self):
        """
        загружаем данные из файла
        :return: pass
        """
        global path_to_file
        path_to_file = QFileDialog.getOpenFileName(self, 'Открыть файл', '', "Text Files (*.txt)")[0]

        if path_to_file:
            file = open(path_to_file, 'r')

            data = file.read()

            self.plainTextEdit.appendPlainText("Полученные данные: \n" + data + "\n")

            with open(path_to_file, 'r') as f:
                for line in f:
                    mas.append([int(x) for x in line.split()])

            global list_of_numbers
            list_of_numbers = []

            # \b -- ищет границы слов
            # [0-9] -- описывает что ищем
            # + -- говорит, что искать нужно минимум от 1 символа
            for num in re.findall(r'\b[0-9]+\b', data):
                list_of_numbers.append(num)

    def process_data(self):
        if validation_of_data():
            find_max()
            find_sum_of_first_row()

            # -*- выполнение задания -*-
            if counter == 0:

                self.plainTextEdit.appendPlainText("Данные обработаны! " + '\n' + "Максимальный элементы 2 строки = " + str(maxim) +'\n'+"\n")

                # выводим список на экран
                for k, i in enumerate(fun(mas)):
                    self.plainTextEdit.insertPlainText(str(i) + " ")

                    if ((k + 1) % 5) == 0:
                        self.plainTextEdit.appendPlainText("")
            else:
                self.plainTextEdit.appendPlainText(
                    "Максимальный элемент 2 строки "
                    "не больше чем 1 элемент 3 строки! \n")
        else:
            self.plainTextEdit.appendPlainText("Неправильно введены данные! "
                                               "Таблица должна быть размером "
                                               "5х6 и состоять из чисел! \n")

    def save_data_in_file(self):
        """
        сохраняем данные в выбранный нами файл
        :return:
        """

        if path_to_file:
            file = open(path_to_file.split(".")[0] + '-Output.txt', 'w')

            for k, i in enumerate(fun(mas)):
                file.write(str(i) + " ")
                if ((k + 1) % 5) == 0:
                    file.write("\n")

            file.close()

            self.plainTextEdit.appendPlainText("Файл был успешно сохранен! \n")
        else:
            self.plainTextEdit.appendPlainText("Для начала загрузите файл!")

    def clear(self):
        self.plainTextEdit.clear()




def find_max():
    global counter
    global maxim
    maxim = max(mas[1])
    counter = 0
    print(mas)
    max_value = max(mas[1])
    max_index = mas[1].index(max_value)

    if max_value > mas[2][0]:
        count = mas[2][0]
        mas[2][0] = mas[1][max_index]
        mas[1][max_index] = count
    else:
         counter = 1



def validation_of_data():
    """
    проверяем данные на валидность: всего должно быть ровно 30 ЧИСЕЛ
    :return: True - данные корректны, False - нет
    """
    if len(list_of_numbers) == 30:
        for i in list_of_numbers:
            try:
                float(i)
            except Exception:
                return False
        return True
    else:
        return False


def fun(mas, result = []):
    for i in mas:
        if isinstance(i,list):
            fun(i, result)
        else:
            result.append(i)
    return result


def find_sum_of_first_row():
    """
    находим сумму чисел из первой строки таблицы
    :return: сумму чисел из первой строки
    """


def main():
    app = QApplication(sys.argv)
    window = Main()
    window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
