# cinema 5.0
import sys

import datetime

from PyQt5.QtCore import Qt

from PyQt5.QtWidgets import QCheckBox, QPlainTextEdit, QMainWindow, QGroupBox, QVBoxLayout
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QLineEdit
from PyQt5.QtWidgets import QCalendarWidget, QGridLayout, QListView, QRadioButton
from PyQt5.QtWidgets import QLineEdit, QTimeEdit, QToolButton, QPlainTextEdit, QComboBox


class cinema:
    def __init__(self):
        self.places = []
        self.halls = []
        self.times = []
        self.glances = []
        self.all = []
        
    def get_tickets(self, place, hall, seat, time, glance):
        self.all.append([place, hall, seat, time, glance])

    def create(self, place, hall, time, glance):
        if place not in self.places:
            self.places.append(place)
        if hall not in self.halls:
            self.halls.append(hall)
        if time not in self.times:
            self.times.append(time)
        if glance not in self.glances:
            self.glances.append(glance)

        self.all.append([place, hall, Seat([0, 0]), time, glance])
    

connect = cinema()


class Place:
    def __init__(self, place):
        self.place = place

    def __eq__(self, other):
        if self.place == other.place:
            return True
        else:
            return False


class Hall:
    def __init__(self, config):
        self.name = str(config[0])
        self.config = [int(config[1]), int(config[2])]

    def __eq__(self, other):
        if self.config == other.config:
            return True
        else:
            return False


class Time:
    def __init__(self, y, m, d, h, mi):
        self.year = int(y)
        self.month = int(m)
        self.data = int(d)
        self.hour = int(h)
        self.minute = int(mi)
        self.full = [self.year, self.month, self.data, self.hour, self.minute]
        self.hhh = ':'.join(['0' * (2 - len(str(h))) + str(h), '0' * (2 - len(str(mi))) + str(mi)])
        self.ddd = '.'.join(['0' * (2 - len(str(d))) + str(d), '0' * (2 - len(str(m))) + str(m), str(y)])
        self.beauty = ' '.join([self.hhh, self.ddd])
        
    def __eq__(self, other):
        if self.full == other.full:
            return True
        else:
            return False


def check(y, m, d, h, mi):
    y, m, d, h, mi = int(y), int(m), int(d), int(h), int(mi)
    dat = str(datetime.datetime.now())
    year = int(dat.split('-')[0])
    month = int(dat.split('-')[1])
    data = int((dat.split(' ')[0]).split('-')[-1])
    hour = int((dat.split(' ')[-1]).split(':')[0])
    minute = int((dat.split(' ')[-1]).split(':')[1])
    if y < year:
        return False
    elif y == year:
        if m < month:
            return False
        elif m == month:
            if d < data:
                return False
            elif d == data:
                if h < hour:
                    return False
                elif h == hour:
                    if mi <= minute:
                        return False
    return True


class Glance:
    def __init__(self, glance):
        self.glance = glance

    def __eq__(self, other):
        if self.glance == other.glance:
            return True
        else:
            return False


class Seat:
    def __init__(self, config):
        self.num = [int(config[0]), int(config[1])]

    def __eq__(self, other):
        if self.num == other.num:
            return True
        else:
            return False


class FirstWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
 
    def initUI(self):
        self.setGeometry(300, 625, 400, 300)
        self.setWindowTitle('Кинотеатры последние')
 
        btn = QPushButton('Создать\n сеанс', self)
        btn.setStyleSheet('QPushButton {background-color: #A3C1DA; color: black;}')
        btn.resize(75, 50)
        btn.move(66, 125)
        btn.pressed.connect(self.run)

        btn = QPushButton('Заказать\n билет', self)
        btn.setStyleSheet('QPushButton {background-color: #A3C1DA; color: black;}')
        btn.resize(75, 50)
        btn.move(166, 125)
        btn.pressed.connect(self.run)

        btn = QPushButton('Помощь', self)
        btn.setStyleSheet('QPushButton {background-color: #A3C1DA; color: black;}')
        btn.resize(75, 50)
        btn.move(266, 125)
        btn.pressed.connect(self.run)

    def run(self):
        if str(self.sender().text()) == 'Создать\n сеанс':
            self.pro1 = Create()
            self.pro1.show()
            
        elif str(self.sender().text()) == 'Заказать\n билет':
            self.pro1 = BookTickets()
            self.pro1.show()
        else:
            self.pro1 = Info()
            self.pro1.show()


class Create(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
 
    def initUI(self):
        self.setGeometry(300, 625, 400, 625)
        self.setWindowTitle('Создание сеанса')
        self.all = ["Здание: ", "Номер зала: ", "Кол-во рядов: ", "Кол-во мест в ряду: ", "Название фильма: ", "Время: "]

        self.name_input1 = QLineEdit(self)

        self.name_input2 = QLineEdit(self)

        self.name_input3 = QLineEdit(self)

        self.name_input4 = QLineEdit(self)

        self.name_input5 = QLineEdit(self)

        self.timeEdit = QTimeEdit()
        self.cWidget = QCalendarWidget()

        self.pButton = QPushButton("Создать сеанс", self)
        
        self.listEvent = QPlainTextEdit()
       
        self.grid = QGridLayout(self)
        self.grid.addWidget(self.name_input1, 0, 1)
        self.grid.addWidget(self.name_input2, 1, 1)
        self.grid.addWidget(self.name_input3, 2, 1)
        self.grid.addWidget(self.name_input4, 3, 1)
        self.grid.addWidget(self.name_input5, 4, 1)
        self.grid.addWidget(self.timeEdit, 5, 1)
        self.grid.addWidget(self.cWidget, 6, 1)
        self.pButton.clicked.connect(self.add)
        self.grid.addWidget(self.pButton, 7, 1)
        
        for i in range(len(self.all)):
            self.name_label = QLabel(self)
            self.name_label.setText(self.all[i])
            self.grid.addWidget(self.name_label, i, 0)

    def add(self):
        self.name_input1.setStyleSheet('QLineEdit {background-color: blue; color: white;}')
        self.name_input2.setStyleSheet('QLineEdit {background-color: blue; color: white;}')
        self.name_input3.setStyleSheet('QLineEdit {background-color: blue; color: white;}')
        self.name_input4.setStyleSheet('QLineEdit {background-color: blue; color: white;}')
        self.name_input5.setStyleSheet('QLineEdit {background-color: blue; color: white;}')
        self.timeEdit.setStyleSheet('QTimeEdit {background-color: blue; color: white;}')
        
        if not bool(self.name_input1.text()):
            self.name_input1.setStyleSheet('QLineEdit {background-color: red; color: black;}')
        elif not bool(self.name_input2.text()) or not self.name_input2.text().isdigit():
            self.name_input2.setStyleSheet('QLineEdit {background-color: red; color: black;}')
        elif not bool(self.name_input3.text()) or not self.name_input3.text().isdigit():
            self.name_input3.setStyleSheet('QLineEdit {background-color: red; color: black;}')
        elif not bool(self.name_input4.text()) or not self.name_input4.text().isdigit():
            self.name_input4.setStyleSheet('QLineEdit {background-color: red; color: black;}')
        elif not bool(self.name_input5.text()):
            self.name_input5.setStyleSheet('QLineEdit {background-color: red; color: black;}')
        elif not check(str(self.cWidget.selectedDate().year()),
                       str(self.cWidget.selectedDate().month()),
                       str(self.cWidget.selectedDate().day()),
                       str(self.timeEdit.time().hour()),
                       str(self.timeEdit.time().minute())):
            self.timeEdit.setStyleSheet('QTimeEdit {background-color: red; color: black;}')
        else:
            place = Place(str(self.name_input1.text()))
            hall = Hall([str(self.name_input2.text()), str(self.name_input3.text()), str(self.name_input4.text())])
            glance = Glance(self.name_input5.text())
            time = Time(str(self.cWidget.selectedDate().year()),
                     str(self.cWidget.selectedDate().month()),
                     str(self.cWidget.selectedDate().day()),
                     str(self.timeEdit.time().hour()),
                     str(self.timeEdit.time().minute()))
            ok = True
            for el in connect.all:
                if [place, hall] == el[:2]:
                    if time == el[3]:
                        ok = False
                    elif [time.year, time.month, time.data] == [el[3].year, el[3].month, el[3].data]:
                        if time.hour in range(el[3].hour, el[3].hour + 2):
                            ok = False
            if ok:                                         
                self.name_input1.setStyleSheet('QLineEdit {background-color: green; color: white;}')
                self.name_input2.setStyleSheet('QLineEdit {background-color: green; color: white;}')
                self.name_input3.setStyleSheet('QLineEdit {background-color: green; color: white;}')
                self.name_input4.setStyleSheet('QLineEdit {background-color: green; color: white;}')
                self.name_input5.setStyleSheet('QLineEdit {background-color: green; color: white;}')
                self.timeEdit.setStyleSheet('QTimeEdit {background-color: green; color: white;}')

                connect.create(place, hall, time, glance)
            else:
                self.name_input1.setStyleSheet('QLineEdit {background-color: red; color: white;}')
                self.name_input2.setStyleSheet('QLineEdit {background-color: red; color: white;}')
                self.name_input3.setStyleSheet('QLineEdit {background-color: red; color: white;}')
                self.name_input4.setStyleSheet('QLineEdit {background-color: red; color: white;}')
                self.name_input5.setStyleSheet('QLineEdit {background-color: red; color: white;}')
                self.timeEdit.setStyleSheet('QTimeEdit {background-color: red; color: white;}')

            
class BookTickets(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
 
    def initUI(self):
        self.setGeometry(300, 600, 400, 300)
        self.setWindowTitle('Бронирование билетов')
        self.all = ["Выберите кинотеатр: ", "Выберите дату: ", "Выберите сеанс: ", "Выберите места: "]
        self.ok = False
        for i in range(len(self.all)):
            self.name_label = QLabel(self)
            self.name_label.setText(self.all[i])
            self.name_label.move(25, i*70 + 10)

        self.combo1 = QComboBox(self)
        self.combo1.addItems(list(map(lambda x: x.place, connect.places)))
        self.combo1.activated[str].connect(self.onActivated)
        self.combo1.resize(150, 25)
        self.combo1.move(175, 10)
        
        self.combo2 = QComboBox(self)
        self.combo2.activated[str].connect(self.onActivated1)
        self.combo2.resize(150, 25)
        self.combo2.move(175, 80)

        self.combo3 = QComboBox(self)
        self.combo3.activated[str].connect(self.onActivated2)
        self.combo3.resize(150, 25)
        self.combo3.move(175, 150)

        self.combo4 = QComboBox(self)
        self.combo4.activated[str].connect(self.onActivated3)
        self.combo4.resize(150, 25)
        self.combo4.move(175, 220)

        self.btn = QPushButton('Бронь', self)
        self.btn.setStyleSheet('QPushButton {background-color: #A3C1DA; color: black;}')
        self.btn.resize(75, 40)
        self.btn.move(150, 250)
        self.btn.pressed.connect(self.run)

    def onActivated(self, text):
        self.place = Place(text)
        self.combo2.clear()
        nes = []
        for el in connect.all:
            if el[0].place == str(text):
                if el[-2].ddd not in nes:
                    nes.append(el[-2].ddd)
        self.combo2.addItems(nes)

    def onActivated1(self, text):
        self.ddd = str(text)
        self.combo3.clear()
        nes = []
        for el in connect.all:
            if el[0] == self.place:
                if el[-2].ddd == self.ddd:
                    movie = 'Фильм: {}'.format(el[-1].glance)
                    if ', '.join([movie, el[-2].hhh]) not in nes:
                        nes.append(', '.join([movie, el[-2].hhh]))
        self.combo3.addItems(nes)
                
    def onActivated2(self, text):
        self.combo4.clear()
        nesnt = []
        nes = []
        for el in connect.all:
            if el[0] == self.place:
                if el[-2].ddd == self.ddd:
                    if el[-2].hhh == str(text).split(', ')[-1]:
                        self.place = el[0]
                        self.hall = el[1]
                        self.time = el[-2]
                        self.glance = el[-1]
                        if el[2].num != [0, 0]:
                            nesnt.append(el[2].num)
        for i in range(1, self.hall.config[0] + 1):
            for j in range(1, self.hall.config[1] + 1):
                if [i, j] not in nesnt:
                    a = 'Ряд: {}, '.format(str(i))
                    b = 'Кресло: {} '.format(str(j))
                    c = a + b
                    nes.append(c)
        self.combo4.addItems(nes)
                        
    def onActivated3(self, text):
        a = int(str(text).split(', ')[0].split('Ряд: ')[-1])
        b = int(str(text).split(', ')[-1].split('Кресло: ')[-1])
        self.seat = Seat([a, b])
        self.ok = True
    
    def run(self):
        if self.ok:
            self.combo1.setStyleSheet('QComboBox {background-color: green; color: white;}')
            self.combo2.setStyleSheet('QComboBox {background-color: green; color: white;}')
            self.combo3.setStyleSheet('QComboBox {background-color: green; color: white;}')
            self.combo4.setStyleSheet('QComboBox {background-color: green; color: white;}')
            connect.get_tickets(self.place, self.hall, self.seat, self.time, self.glance)
        else:
            self.combo1.setStyleSheet('QComboBox {background-color: red; color: white;}')
            self.combo2.setStyleSheet('QComboBox {background-color: red; color: white;}')
            self.combo3.setStyleSheet('QComboBox {background-color: red; color: white;}')
            self.combo4.setStyleSheet('QComboBox {background-color: red; color: white;}')

    
class Info(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
 
    def initUI(self):
        self.setWindowTitle('Помощь')
        self.check = []
        
        self.combo1 = QComboBox(self)
        self.combo1.addItems(list(map(lambda x: x.place, connect.places)))
        self.combo1.activated[str].connect(self.onActivated1)

        self.combo2 = QComboBox(self)
        self.combo2.addItems(list(map(lambda x: x.ddd, connect.times)))
        self.combo2.activated[str].connect(self.onActivated2)

        self.combo3 = QComboBox(self)
        need = []
        for el in connect.all:
            if el[2] != Seat([0, 0]):
                cin = 'Фильм: {}, время: {}'.format(el[-1].glance, el[-2].hhh)
                need.append(cin)
        self.combo3.addItems(need)
        self.combo3.activated[str].connect(self.onActivated3)
        
        grid = QGridLayout()
        grid.addWidget(self.createExampleGroup(), 0, 0)

        self.text = QPlainTextEdit(self)

        vbox1 = QVBoxLayout()
        vbox1.addWidget(self.combo1)
        vbox1.addWidget(self.combo2)
        vbox1.addWidget(self.combo3)
        vbox1.addWidget(self.text)
        vbox1.addStretch(1)
        groupBox1 = QGroupBox(" ")
        groupBox1.setLayout(vbox1)
        grid.addWidget(groupBox1, 0, 1)
        
        self.setLayout(grid)

    def createExampleGroup(self):
        groupBox = QGroupBox("Выберите критерий поиска: ")

        self.radio1 = QRadioButton("Кинотеатр")
        self.radio2 = QRadioButton("Дата")
        self.radio3 = QRadioButton("Фильм/время")

        self.radio1.setChecked(True)

        vbox = QVBoxLayout()
        vbox.addWidget(self.radio1)
        vbox.addWidget(self.radio2)
        vbox.addWidget(self.radio3)
        vbox.addStretch(1)
        groupBox.setLayout(vbox)

        return groupBox
    
    def onActivated1(self, text):
        text1 = ["Результаты поиска: "]
        if self.radio1.isChecked():
            if bool(connect.all):
                for el in connect.all:
                    if el[0].place == str(text) and el[2] != Seat([0, 0]):
                        a = []
                        a.append('Здание: {}'.format(el[0].place))
                        a.append('Кинозал: {}'.format(el[1].name))
                        a.append('Дата: {}'.format(el[3].ddd))
                        movie = 'Фильм: {}'.format(el[-1].glance)
                        a.append(', '.join([movie, el[-2].hhh]))
                        b = 'Ряд: {}, '.format(str(el[2].num[0]))
                        c = 'Кресло: {} '.format(str(el[2].num[1]))
                        a.append(''.join([b, c]))
                        text1.append('\n'.join(a))
        self.text.setPlainText('\n---------------------\n'.join(text1))

    def onActivated2(self, text):
        text1 = ["Результаты поиска: "]
        if self.radio2.isChecked():
            if bool(connect.all):
                for el in connect.all:
                    if el[3].ddd == str(text) and el[2] != Seat([0, 0]):
                        a = []
                        a.append('Здание: {}'.format(el[0].place))
                        a.append('Кинозал: {}'.format(el[1].name))
                        a.append('Дата: {}'.format(el[3].ddd))
                        movie = 'Фильм: {}'.format(el[-1].glance)
                        a.append(', '.join([movie, el[-2].hhh]))
                        b = 'Ряд: {}, '.format(str(el[2].num[0]))
                        c = 'Кресло: {} '.format(str(el[2].num[1]))
                        a.append(''.join([b, c]))
                        text1.append('\n'.join(a))
        self.text.setPlainText('\n---------------------\n'.join(text1))

    def onActivated3(self, text):
        text1 = ["Результаты поиска: "]
        notime = text.split(', время: ')[-1]
        if self.radio3.isChecked():
            if bool(connect.all):
                for el in connect.all:
                    if el[3].hhh == notime and el[2] != Seat([0, 0]):
                        a = []
                        a.append('Здание: {}'.format(el[0].place))
                        a.append('Кинозал: {}'.format(el[1].name))
                        a.append('Дата: {}'.format(el[3].ddd))
                        movie = 'Фильм: {}'.format(el[-1].glance)
                        a.append(', '.join([movie, el[-2].hhh]))
                        b = 'Ряд: {}, '.format(str(el[2].num[0]))
                        c = 'Кресло: {} '.format(str(el[2].num[1]))
                        a.append(''.join([b, c]))
                        text1.append('\n'.join(a))
        self.text.setPlainText('\n---------------------\n'.join(text1))

    
if __name__ == '__main__':
    app = QApplication(sys.argv)
    pro = FirstWindow()
    pro.show()
    sys.exit(app.exec())
