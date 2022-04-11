import datetime
import random
from datetime import datetime, timedelta

class Receip:
    """Номер квитанции"""

    count = 1


    def __init__(self, receipt, acceptance_date, status):
        self.receipt = receipt
        self.acceptance_date = acceptance_date
        self.status = status
        self.rec = Receip.count
        Receip.count += 1

    def receiptt(self):
        #with open('workshop.py', 'a+') as file:
            print("Квитанция №:", self.rec)

    """Дата приёмки"""

    def date(self):
        #with open('workshop.py', 'a') as file:
            self.acceptance_date = datetime.now()
            print("Дата приёмки: ", self.acceptance_date.__str__())

    """Дата выполнения заказа"""

    def date_of_completion(self):

       # with open('workshop.py', 'a') as file:
            self.acceptance_date = datetime.now()
            end = self.acceptance_date + timedelta(days=5)
            date_of_completion = self.acceptance_date + (end - self.acceptance_date) * random.random()
            print("Дата выполнения заказа: ", date_of_completion)

    """Статус заказа"""

    def st(self):
        #with open('workshop.py', 'a') as file:
            self.status = ["Ремонтируется", "Готово", "Выдано клиенту"]
            if self.acceptance_date != self.status[0]:
                print("Статус: Ремонтируется")
            elif self.acceptance_date == self.status[1]:
                print("Статус: Готово")
            elif self.status[2]:
                print("Статус: Выдано клиенту")

#     """
# номер квитанции
# тип изделия (телефон, ноутбук, телевизор)
# дата приемки
# дата выполнения ремонта
# ФИО человека, который сдал в ремонт техники
# статус (ремонтируется, готово, выдано клиенту)"""
