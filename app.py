import webbrowser
from random import randint

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication, QWidget, QLabel, QPushButton, 
                             QVBoxLayout, QHBoxLayout, QMessageBox)
from PyQt5.QtGui import QFont

def get_1():
    return webbrowser.open('https://www.kinopoisk.ru/film/476/')

def get_2():
    return webbrowser.open('https://www.kinopoisk.ru/film/2360/')

def get_3():
    return webbrowser.open('https://www.kinopoisk.ru/film/2213/')

def get_4():
    return webbrowser.open('https://www.kinopoisk.ru/film/8124/')

def get_5():
    return webbrowser.open('https://www.kinopoisk.ru/series/464963/')

def get_6():
    return webbrowser.open('https://www.kinopoisk.ru/series/401152/')

def get_random_film():
    if len(lst_films) > 0:
        url = lst_films[randint(0, len(lst_films)-1)]
        lst_films.remove(url)
        return webbrowser.open(url)
    else:
        box = QMessageBox()
        box.setText('Фильмов больше\nне осталось!!!')
        box.resize(700,200)
        box.setWindowTitle('Конец')
        box.exec()
        

lst_films = [
    'https://www.kinopoisk.ru/film/476/',
    'https://www.kinopoisk.ru/film/2360/',
    'https://www.kinopoisk.ru/film/2213/',
    'https://www.kinopoisk.ru/film/8124/',
    'https://www.kinopoisk.ru/series/464963/',
    'https://www.kinopoisk.ru/series/401152/'

]


app = QApplication([])
window = QWidget()
window.resize(700,400)
window.setWindowTitle('Кинопоиск')

line = QVBoxLayout()
line_h1 = QHBoxLayout()
line_h2 = QHBoxLayout()
line_h3 = QHBoxLayout()
line_h4 = QHBoxLayout()

text = QLabel('Выберите фильм:')
btn1 = QPushButton('Назад в будущее')
btn2 = QPushButton('Король лев')
btn3 = QPushButton('Титаник')
btn4 = QPushButton('Один дома')
btn5 = QPushButton('Игра престолов')
btn6 = QPushButton('Аватар: Легенда об Аанге')
btn7 = QPushButton('Рандом')

btn1.clicked.connect(get_1)
btn2.clicked.connect(get_2)
btn3.clicked.connect(get_3)
btn4.clicked.connect(get_4)
btn5.clicked.connect(get_5)
btn6.clicked.connect(get_6)
btn7.clicked.connect(get_random_film)

line_h1.addWidget(btn1, alignment=Qt.AlignCenter)
line_h1.addWidget(btn2, alignment=Qt.AlignCenter)
line_h2.addWidget(btn3, alignment=Qt.AlignCenter)
line_h2.addWidget(btn4, alignment=Qt.AlignCenter)
line_h3.addWidget(btn5, alignment=Qt.AlignCenter)
line_h3.addWidget(btn6, alignment=Qt.AlignCenter)
line_h4.addWidget(btn7, alignment=Qt.AlignCenter)

line.addWidget(text, alignment=Qt.AlignCenter)
line.addLayout(line_h1)
line.addLayout(line_h2)
line.addLayout(line_h3)
line.addLayout(line_h4)

window.setStyleSheet('background-color: rgb(0, 10, 0); color: white; font-size: 25px; font-style:italic; font-weight: 600')
btn1.setStyleSheet('background-color: rgb(83, 6, 102); border: 10px inset green')
btn2.setStyleSheet('background-color: rgb(83, 6, 102); border: 10px inset green')
btn3.setStyleSheet('background-color: rgb(83, 6, 102); border: 10px inset green')
btn4.setStyleSheet('background-color: rgb(83, 6, 102); border: 10px inset green')
btn5.setStyleSheet('background-color: rgb(83, 6, 102); border: 10px inset green')
btn6.setStyleSheet('background-color: rgb(83, 6, 102); border: 10px inset green')
btn7.setStyleSheet('background-color: rgb(83, 6, 102); border: 10px inset green')
text.setStyleSheet('background-color: rgb(83, 6, 102); border: 10px inset green')
text.setFont(QFont('Times New Roman'))
btn1.setFont(QFont('Times New Roman'))
btn2.setFont(QFont('Times New Roman'))
btn3.setFont(QFont('Times New Roman'))
btn4.setFont(QFont('Times New Roman'))
btn5.setFont(QFont('Times New Roman'))
btn6.setFont(QFont('Times New Roman'))
btn7.setFont(QFont('Times New Roman'))


window.setLayout(line)
window.show()
app.exec()
