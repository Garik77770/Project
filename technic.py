class Device:

    def __init__(self, stamp, breakdown_description):
        self.stamp = stamp
        self.breakdown_description = breakdown_description


class Tv(Device):

    def __init__(self, stamp, screen_diagonal, breakdown_description):
        super().__init__(stamp, breakdown_description)
        self.screen_diagonal = screen_diagonal

    def __str__(self):
        return f'Марка телевизора:{self.stamp}\n' \
               f'Описание поломки:{self.breakdown_description}\n' \
               f'Диагональ экрана:{self.screen_diagonal}\n'


def tv_features():
    """О телевизоре, который сдают в ремонт"""
    stamp = input("Марка телевизора: ")
    screen_diagonal = int(input("диагональ экрана: "))
    breakdown_description = input("Описание поломки: ")
    return stamp, breakdown_description, screen_diagonal


class Laptop(Device):

    def __init__(self, stamp, operating_system, year_of_release, breakdown_description):
        super().__init__(stamp, breakdown_description)
        self.year_of_release = year_of_release
        self.operating_system = operating_system

    def __str__(self):
        return f'Марка ноутбука:  {self.stamp}\nдиагональ экрана: {self.operating_system}\n' \
               f'Год производства: {self.year_of_release}\n' \
               f'Описание поломки: {self.breakdown_description}'


def laptop_features():
    """Данные  ноутбуков, который сдают в ремонт"""

    stamp = input("Марка ноутбука: ")
    operating_system = int(input("диагональ экрана: "))
    year_of_release = int(input("Год производства: "))
    breakdown_description = input("Описание поломки: ")
    return stamp, operating_system, year_of_release, breakdown_description


class Phone(Device):

    def __init__(self, stamp, operating_system, breakdown_description):
        super().__init__(stamp, breakdown_description)
        self.operating_system = operating_system

    def __str__(self):
        return f'Марка телефона: {self.stamp}\n' \
               f'Операционная система:  {self.operating_system}\n' \
               f'Описание поломки:  {self.breakdown_description}\n'


def phone_features():
    """ Данные телефонов, который сдают в ремонт"""

    stamp = input("Марка телефона: ")
    operating_system = input("Операционная система: ")
    breakdown_description = input("Описание поломки: ")
    return stamp, operating_system, breakdown_description
