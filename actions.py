import receipt
from receipt import Receipt


def actions():
    # """Делаем выбор между ремонтом и информацией"""
    star = input("Choose to put it into repair or view the information: ")

    actions = ['repair', 'information']
    if star == actions[0]:
        return Receipt("", "", "", "", "")
    elif star == actions[1]:
        option = input('Enter number or name: ')
        n = ['number', 'name']
        if option == n[0]:
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
        elif option == n[1]:
            name = str(input('Enter Your Last Name First Name Patronymic: '))
            if name == receipt.receipt1[5]:
                return '\n'.join(receipt.receipt1)
            elif name == receipt.receipt2[5]:
                return '\n'.join(receipt.receipt2)
            elif name == receipt.receipt3[5]:
                return '\n'.join(receipt.receipt3)
            elif name == receipt.receipt4[5]:
                return '\n'.join(receipt.receipt4)
            elif name == receipt.receipt5[5]:
                return '\n'.join(receipt.receipt5)



