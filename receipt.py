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
               f"Тип изделия:{self.choice}\n" \
               f"Дата приёмки: {self.acceptance_date}\n" \
               f"Дата выполнения заказа: {date_of_completion}\n" \
               f"Фамилия Имя Отчество: {self.name}\n" \
               f"Статус:{random.choice(self.status)}\n"





#     """
# номер квитанции
# тип изделия (телефон, ноутбук, телевизор)
# дата приемки
# дата выполнения ремонта
# ФИО человека, который сдал в ремонт техники
# статус (ремонтируется, готово, выдано клиенту)"""
