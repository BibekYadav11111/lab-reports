# 3. Define a class BankAccount with private attributes account_number and
# balance. Implement methods to deposit and withdraw money, ensuring that
# the balance cannot go below zero. Provide a method to get the account
# details. Test the class by performing deposit and withdrawal operations.
class BankAccont:
    def __init__(self,account_number,balance):
        self.account_number=account_number
        self.balance=balance
    def withdraw(self,withdarw):
        if self.balance>withdarw:
            self.balance-=withdarw
            print(f'currnet balance : {self.balance}')
        else:
            print('Insuffient balance')
    def deposite(self,despoits):
        self.balance+=despoits
        print(f'currnet balance : {self.balance}')
    def info(self):
        print(f'{self.account_number} {self.balance}')
user=BankAccont('1111',10000)
user.info()
user.withdraw(100000000)
user.info()

        