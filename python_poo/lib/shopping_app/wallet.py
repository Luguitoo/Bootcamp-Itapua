from ownable import Ownable  # Asegúrate de que el módulo y la clase se llamen correctamente

class Wallet(Ownable):  # Hacer que Wallet herede de Ownable
    def __init__(self, owner):
        super().__init__()  # Llamar al constructor de la clase padre
        self.set_owner(owner)
        self.balance = 0

    def deposit(self, amount):
        self.balance += int(amount)

    def withdraw(self, amount):
        if not self.balance >= amount:
            return
        self.balance -= int(amount)
        return amount
