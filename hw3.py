# 1
class Bank:
    def __init__(self, name, balance):
        self._name = name
        self._balance = balance

    def moneyX(self):
        try:
            count_money = float(input("введите сумму:"))
            self._balance += count_money
            return f'баланс пополнен на {count_money}'
        except ValueError:
            print('Нужно вводить число')

    def _merge_balance(self, other):
        """Объединить баланс с другим клиентом"""
        if isinstance(other, Bank):
            self._balance += other._balance
            print(f"Баланс объединён! Текущий баланс: {self._balance}")
        else:
            print("Ошибка: нужно передать объект класса Bank.")

    def _kill(self):
        self._balance = 0

    def __jackpot(self):
        self._balance = self._balance*10

# 2
class Calculator:
    def __init__(self, value):
        self.value = value

    def __add__(self, other):
        return Calculator(self.value + other.value)

    def __sub__(self, other):
        return Calculator(self.value - other.value)

    def __mul__(self, other):
        return Calculator(self.value * other.value)

    def __truediv__(self, other):
        if other.value == 0:
            raise ZeroDivisionError("На ноль делить нельзя!")
        return Calculator(self.value / other.value)

    def __str__(self):
        return f"Результат: {self.value}"
