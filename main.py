# import sys

from receipt import Receip
from technic import Laptop
from technic import Telephon
from technic import Tv


class Name:
    """ Ввод ФИО человека сдающего технику"""

    def __init__(self, Name):
        self.Name = Name

    def nam(self):
        # with open('workshop.py', 'a+') as file:
        self.Name = input("Введите ФИО: ")

        return 'Фамилия Имя Отчество:', self.Name
    # print('Фамилия Имя Отчество: ', self.Name, file=file)


n = Name('')
n.nam()


class Vibor:
    """Выбор техники """

    def __init__(self, Vibor, product_type):
        self.Vibor = Vibor
        self.product_type = product_type

    def vib(self):

        # with open('workshop.py', 'a+') as file:
        self.Vibor = input("Напишите ваш выбор:(Laptop, Telephon, Tv) ")

        # print('Тип изделия: ', self.Vibor, file=file)

        self.product_type = ['Laptop', 'Telephon', 'Tv']

        if self.Vibor == self.product_type[0]:

            l = Laptop("", "", "", "")
            l.laptop()


        elif self.Vibor == self.product_type[1]:

            tel = Telephon("", "", "")
            tel.telephone()

        elif self.Vibor == self.product_type[2]:

            T = Tv("", "", "")
            T.tv()


V = Vibor('', '')
V.vib()
r = Receip("", "", "")
r.receiptt()
print('Тип изделия:', V.Vibor )
# with open("characteristic.txt", 'r') as file:
#     for line in file:
#         if not line.isspace():
#             sys.stdout.write(line)

t = Receip("", "", "")
t.date()

d = Receip("", "", "")
d.date_of_completion()
print('Фамилия Имя Отчество:', n.Name)

s = Receip("", "", "")
s.st()
