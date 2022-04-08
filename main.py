class Name:
    """ Ввод ФИО человека сдающего технику"""

    def __init__(self, Name):
        self.Name = Name

    def nam(self):
        with open('workshop.csv', 'a+') as file:
            self.Name = input("Введите ФИО: ")
            print('FIO: ', self.Name, file=file)


from kvitancia import Receip

r = Receip("")
r.receiptt()
t = Name('')
t.nam()


class Vibor:
    """Выбор техники """

    def __init__(self, Vibor, product_type):
        self.Vibor = Vibor
        self.product_type = product_type

    def vib(self):

        with open('workshop.csv', 'a+') as file:
            self.Vibor = input("Напишите ваш выбор:(Laptop, Telephon, Tv) ")
            print('Тип изделия: ', self.Vibor, file=file)
            self.product_type = ['Laptop', 'Telephon', 'Tv']

        if self.Vibor == self.product_type[0]:
            from texnica import Laptop

            l = Laptop("", "", "", "")
            l.laptop()


        elif self.Vibor == self.product_type[1]:
            from texnica import Telephon

            tel = Telephon("", "", "")
            tel.telephone()

        elif self.Vibor == self.product_type[2]:
            from texnica import Tv

            T = Tv("", "", "")
            T.tv()


V = Vibor('', '')
V.vib()

import sys

with open("file_name.txt", 'r') as file:
    for line in file:
        if not line.isspace():
            sys.stdout.write(line)

from kvitancia import Date

t = Date("")
t.date()

d = Date("")
d.date_of_completion()
from kvitancia import Status

s = Status("", "")
s.st()
