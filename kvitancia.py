class Receip:
    """Номер квитанции"""
    count = 1

    def __init__(self, receipt):
        self.receipt = receipt
        self.rec = Receip.count
        Receip.count += 1

    def receiptt(self):
        with open('workshop.py', 'a+') as file:
            print("Квитанция №:", self.rec, file=file)


class Date:
    """Дата приёмки"""

    def __init__(self, acceptance_date):
        self.acceptance_date = acceptance_date

    def date(self):
        import datetime
        with open('workshop.py', 'a') as file:
            self.acceptance_date = datetime.datetime.now()
            print("Дата приёмки: ", self.acceptance_date.__str__(), file=file)

    """Дата выполнения заказа"""

    def date_of_completion(self):
        import random
        from datetime import datetime, timedelta
        with open('workshop.py', 'a') as file:
            self.acceptance_date = datetime.now()
            end = self.acceptance_date + timedelta(days=5)
            date_of_completion = self.acceptance_date + (end - self.acceptance_date) * random.random()
            print("Дата выполнения заказа: ", date_of_completion, file=file)


class Status(Date):
    """Статус заказа"""

    def __init__(self, status, acceptance_date):
        super().__init__(acceptance_date)
        self.status = status

    def st(self):
        with open('workshop.py', 'a') as file:
            self.status = ["Ремонтируется", "Готово", "Выдано клиенту"]
            if self.acceptance_date != self.status[0]:
                print("Статус: Ремонтируется", file=file)
            elif self.acceptance_date == self.status[1]:
                print("Статус: Готово", file=file)
            elif self.status[2]:
                print("Статус: Выдано клиенту", file=file)

#     """
# номер квитанции
# тип изделия (телефон, ноутбук, телевизор)
# дата приемки
# дата выполнения ремонта
# ФИО человека, который сдал в ремонт техники
# статус (ремонтируется, готово, выдано клиенту)"""
