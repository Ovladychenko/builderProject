from __future__ import annotations

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


class Shop:
    def calculate_computer(self, computer: Computer):
        prise = (cpu_list.get(computer.cpu)
                 + keyboard_list.get(computer.keyboard)
                 + system_block_list.get(computer.system_block)
                 + mause_list.get(computer.mause))

        print('Computer components:')
        print(f'cpu:{computer.cpu} prise:{cpu_list.get(computer.cpu)}')
        print(f'keyboard:{computer.keyboard} prise:{keyboard_list.get(computer.keyboard)}')
        print(f'system block:{computer.system_block} prise:{system_block_list.get(computer.system_block)}')
        print(f'mause:{computer.mause} prise:{mause_list.get(computer.mause)}\n')
        print(f'Total prise:{prise}')


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


computer = Computer()
computer.add_cpu('Intel')
computer.add_keyboard('Logitech')
computer.add_system_block('Dell')
computer.add_mause('HyperX')

shop = Shop()
shop.calculate_computer(computer)
