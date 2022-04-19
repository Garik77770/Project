import receipt
from receipt import Receipt


def actions():
    """Делаем выбор между ремонтом и информацией"""
    star = input("Choose to put it into repair or view the information: ")

    actions = ['repair', 'information']
    if star == actions[0]:
        return Receipt("", "", "", "", "")
    elif star == actions[1]:
        number = int(input('enter the receipt number: '))

        if number == 1:
            return '\n'.join(receipt.receipt1)
        elif number == 2:
            return '\n'.join(receipt.receipt2)
        elif number == 3:
            return '\n'.join(receipt.receipt3)
        elif number == 4:
            return '\n'.join(receipt.receipt4)
        elif number == 5:
            return '\n'.join(receipt.receipt5)
