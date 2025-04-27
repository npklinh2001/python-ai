"""
    Hãy mở rộng Ex2 bằng cách định nghĩa 1 loại tài khoản ngân hàng đặc biệt.
    Với loại tài khoản này, người dùng luôn phải duy trì 1 mức tiền nhất định
    tối thiểu trong tài khoản
"""
from task_2 import BankAccount

class MinimumBankAccount(BankAccount):
    def __init__(self, minimum_balance):
        super().__init__()
        self.minimum_balance = minimum_balance

    def withdraw(self, amount):
        if (self.balance - amount) >= self.minimum_balance:
            self.balance -= amount
            return self.balance
        else:
            return 'Không đủ tiền'

    def deposit(self, amount):
        self.balance += amount
        return self.balance

if __name__ == '__main__':
    bank_acc = MinimumBankAccount(10)
    current_balance = bank_acc.deposit(50)
    print(current_balance)
    current_balance = bank_acc.withdraw(100)
    print(current_balance)