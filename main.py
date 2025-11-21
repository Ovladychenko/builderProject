from __future__ import annotations
from enum import Enum

cpu_list = {
    'Intel': 1200,
    'AMD': 500
}

keyboard_list = {
    'Logitech': 1200,
    'Hator': 700,
    'Keychron': 450
}

system_block_list = {
    'Asus': 1200,
    'Artline': 700,
    'Dell': 3000,
    'HP': 2500
}

mause_list = {
    'Logitech': 350,
    'Razer': 400,
    'Asus': 500,
    'HyperX': 600
}


class CheckType(Enum):
    Sold: 1
    Returned: 2


class Shop:
    check_list = []
    account_summ = 0

    @staticmethod
    def calculate_computer(computer: Computer):
        prise = (cpu_list.get(computer.cpu)
                 + keyboard_list.get(computer.keyboard)
                 + system_block_list.get(computer.system_block)
                 + mause_list.get(computer.mause))

        # print('Computer components:')
        # print(f'cpu:{computer.cpu} prise:{cpu_list.get(computer.cpu)}')
        # print(f'keyboard:{computer.keyboard} prise:{keyboard_list.get(computer.keyboard)}')
        # print(f'system block:{computer.system_block} prise:{system_block_list.get(computer.system_block)}')
        # print(f'mause:{computer.mause} prise:{mause_list.get(computer.mause)}\n')
        # print(f'Total prise:{prise}')

        return prise

    @staticmethod
    def get_new_id():
        return len(Shop.check_list) + 1

    @staticmethod
    def get_pay(summ):
        Shop.account_summ += summ

    @staticmethod
    def return_pay(summ):
        Shop.account_summ -= summ

    @staticmethod
    def sale(client: Client, computer: Computer):
        check = Check(client, computer)
        Shop.check_list.append(check)

    @staticmethod
    def return_goods(number_order: int):
        for item in Shop.check_list:
            if item.id == number_order:
                item.status = 'возврат'
                item.client.get_money(item.summ)
                Shop.return_pay(item.summ)
                break

    @staticmethod
    def report():
        print(f'Сумма в кассе {Shop.account_summ}')
        for item in Shop.check_list:
            print(f'Заказ №{item.id} статус {item.status} клиент {item.client.name} сумма {item.summ} ')


class Computer:
    __cpu = str
    __keyboard = str
    __system_block = str
    __mause = str

    def add_cpu(self, cpu: str):
        self.__cpu = cpu
        return self

    def add_keyboard(self, keyboard: str):
        self.__keyboard = keyboard
        return self

    def add_system_block(self, system_block: str):
        self.__system_block = system_block
        return self

    def add_mause(self, mause: str):
        self.__mause = mause
        return self

    @property
    def cpu(self):
        return self.__cpu

    @property
    def keyboard(self):
        return self.__keyboard

    @property
    def system_block(self):
        return self.__system_block

    @property
    def mause(self):
        return self.__mause


class Client:
    def __init__(self, id, name, summ):
        self.id = id
        self.name = name
        self.summ = summ

    def send_money(self, summ):
        # отправка денег
        self.summ -= summ

    def get_money(self, summ):
        # получение денег
        self.summ -= summ


class Check:
    def __init__(self, client: Client, computer: Computer):
        self.id = Shop.get_new_id()
        self.client = client
        self.computer = computer
        self.summ = Shop.calculate_computer(computer)
        # self.status = CheckType.Sold #ошибка
        self.status = 'продано'

        client.send_money(self.summ)
        Shop.get_pay(self.summ)


client1 = Client(1, 'Иванов Иван Иванович', 57000)
client2 = Client(2, 'Петров Петр Петрович', 15000)
client3 = Client(3, 'Миронов Мадест Сидорович', 7500)

computer1 = Computer()
computer1.add_cpu('Intel')
computer1.add_keyboard('Logitech')
computer1.add_system_block('Dell')
computer1.add_mause('HyperX')

computer2 = Computer()
computer2.add_cpu('AMD')
computer2.add_keyboard('Keychron')
computer2.add_system_block('HP')
computer2.add_mause('Razer')

computer3 = Computer()
computer3.add_cpu('Intel')
computer3.add_keyboard('Logitech')
computer3.add_system_block('HP')
computer3.add_mause('Razer')

print(f'Сумма в кассе {Shop.account_summ}')
# продажа
Shop.sale(client1, computer1)
Shop.sale(client2, computer2)
Shop.sale(client3, computer3)

Shop.report()
# возврат
Shop.return_goods(3)

Shop.report()
