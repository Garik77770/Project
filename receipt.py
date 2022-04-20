import datetime
import random
from datetime import datetime, timedelta

from technic import Laptop, Phone, Tv
from technic import phone_features, tv_features, laptop_features


class Receipt:
    """Номер квитанции и дата приемки"""

    count = 1

    def __init__(self, receipt, acceptance_date, status, name, choice):
        self.receipt = Receipt.count
        self.acceptance_date = datetime.now()
        self.status = ['ремонтируется', 'готово', 'выдано клиенту']
        Receipt.count += 1
        self.name = input("Фамилия Имя Отчество: ")
        self.choice = input("Напишите ваш выбор:(Laptop, Telephon, Tv) ")

    def __str__(self):
        product_type = ['Laptop', 'Telephon', 'Tv']

        if self.choice == product_type[0]:

            print(Laptop(*laptop_features()))


        elif self.choice == product_type[1]:

            print(Phone(*phone_features()))

        elif self.choice == product_type[2]:
            print(Tv(*tv_features()))
        end = self.acceptance_date + timedelta(days=5)
        date_of_completion = self.acceptance_date + (end - self.acceptance_date) * random.random()
        return f"Квитанция №: {self.receipt}\n" \
               f"Тип изделия: {self.choice}\n" \
               f"Дата приёмки: {self.acceptance_date}\n" \
               f"Дата выполнения заказа: {date_of_completion}\n" \
               f"Фамилия Имя Отчество: {self.name}\n" \
               f"Статус: {random.choice(self.status)}\n"


receipt1 = ['Квитанция №: 1',
            'Тип изделия:Laptop',
            'Дата приёмки: 2022-04-19 16:42:58.521218',
            'Дата выполнения заказа: 2022-04-22 17:44:43.829884',
            'Фамилия Имя Отчество:', 'Иванов Петр Леонидович',
            'Статус: готово']
receipt2 = ['Квитанция №: 2',
            'Тип изделия:Laptop',
            'Дата приёмки: 2022-04-10 16:22:58.521218',
            'Дата выполнения заказа: 2022-04-12 17:44:43.829884',
            'Фамилия Имя Отчество:', 'Иванов Александр Леонидович',
            'Статус: ремонтируется']
receipt3 = ['Квитанция №: 3',
            'Тип изделия:Tv',
            'Дата приёмки: 2022-04-19 17:52:19.138160',
            'Дата выполнения заказа: 2022-04-22 03:24:22.172024',
            'Фамилия Имя Отчество:', 'Петров Дмитрий Васильевич',
            'Статус: выдано клиенту']
receipt4 = ['Квитанция №: 4',
            'Тип изделия:Tv',
            'Дата приёмки: 2022-04-15 17:55:17.138160',
            'Дата выполнения заказа: 2022-04-20 03:24:22.172024',
            'Фамилия Имя Отчество: ', 'Васильев Дмитрий Иванович',
            'Статус: готово']
receipt5 = ['Квитанция №: 5',
            'Тип изделия: Telephon',
            'Дата приёмки: 2022-04-16 18:12:04.450731',
            'Дата выполнения заказа: 2022-04-19 22:18:14.025158',
            'Фамилия Имя Отчество:', 'Балышеф Олег Георгиевич',
            'Статус: выдано клиенту']
#     """
# номер квитанции
# тип изделия (телефон, ноутбук, телевизор)
# дата приемки
# дата выполнения ремонта
# ФИО человека, который сдал в ремонт техники
# статус (ремонтируется, готово, выдано клиенту)"""
