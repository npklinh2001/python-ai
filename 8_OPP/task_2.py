"""
    Định nghĩa 1 class tên là BankAccount.
    Định nghĩa phương thức khởi tạo
    Định nghĩa 2 phương thức của class, lần lượt để rút tiền và gửi tiền
"""


class BankAccount:
    def __init__(self):
        self.balance = 0

    def withdraw(self, amount):
        if self.balance > amount:
            self.balance -= amount 
            return self.balance
        else:
            return 'Khum có đủ tiền'
        
    def deposit(self, amount):
        self.balance += amount 
        return self.balance
    
if __name__ == '__main__':
    bank_acc = BankAccount()
    current_balance = bank_acc.deposit(200)
    print(current_balance)
    current_balance = bank_acc.withdraw(80)
    print(current_balance)

