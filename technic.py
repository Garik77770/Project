class Device:
    """Всё об аппаратуре которой сдают в ремонт"""

    def __init__(self, stamp, operating_system, breakdown_description):
        self.stamp = stamp
        self.breakdown_description = breakdown_description
        self.operating_system = operating_system


class Tv(Device):
    """О телевизоре, который сдают в ремонт"""

    def __init__(self, stamp, screen_diagonal, breakdown_description):
        super().__init__(self, stamp, breakdown_description)
        self.screen_diagonal = screen_diagonal

    def tv(self):
        with open('characteristic.txt', 'a') as file:
            self.stamp = input("Марка телевизора: ")
            print('Марка телевизора: ', self.stamp, file=file)
            self.screen_diagonal = input("диагональ экрана: ")
            print('диагональ экрана: ', self.screen_diagonal, file=file)
            self.breakdown_description = input("Описание поломки: ")
            print('Описание поломки: ', self.breakdown_description, file=file)


class Laptop(Device):
    """О ноутбуке, который сдают в ремонт"""

    def __init__(self, stamp, operating_system, year_of_release, breakdown_description):
        super().__init__(stamp, operating_system, breakdown_description)
        self.year_of_release = year_of_release

    def laptop(self):
        with open('characteristic.txt', 'a') as file:
            self.stamp = input("Марка ноутбука: ")
            print('Марка ноутбука: ', self.stamp, file=file)
            self.operating_system = input("диагональ экрана: ")
            print('диагональ экрана: ', self.operating_system, file=file)
            self.year_of_release = input("Год производства: ")
            print('Год производства: ', self.year_of_release, file=file)
            self.breakdown_description = input("Описание поломки: ")
            print('Описание поломки: ', self.breakdown_description, file=file)


class Telephon(Device):
    """ О телефоне, который сдают в ремонт"""

    def __init__(self, stamp, operating_system, breakdown_description):
        super().__init__(stamp, operating_system, breakdown_description)

    def telephone(self):
        with open('characteristic.txt', 'a') as file:
            self.stamp = input("Марка телефона: ")
            print('Марка телефона: ', self.stamp, file=file)
            self.operating_system = input("операционная система: ")
            print('операционная система: ', self.operating_system, file=file)
            self.breakdown_description = input("Описание поломки: ")
            print('Описание поломки: ', self.breakdown_description, file=file)
