from datetime import datetime
import pytz
import time 

class CheckingAccount():

    @staticmethod
    def _data_and_time():
        time_zone_BR = pytz.timezone('Brazil/East')
        hour_BR = datetime.now(time_zone_BR)
        return hour_BR.strftime('%d/%m/%Y %H:%M:%S')

    def __init__(self, _name, cpf, branch_num, acc_num):
        self._name = _name
        self.cpf = cpf
        self.balance = 0
        self.limit = None
        self.branch_num = branch_num
        self.acc_num = acc_num
        self.transactions= []

    def check_account_balance(self): 
        print('Your account balance is R${:,.2f}'.format(self.balance))

    def deposit(self, amount):
        self.balance += amount
        self.transactions.append((amount, 'Balance: {}'.format(self.balance), CheckingAccount._data_and_time()))

    def _Account_limit(self):
        self.limit = -1000
        return self.limit

    def withdraw(self, amount):
        if self.balance - amount < self._Account_limit():
            print('Insufficient balance on the account to withdraw this amount')
            self.check_account_balance()
        else:
            self.balance -= amount
            self.transactions.append((-amount, 'Balance: {}'.format(self.balance), CheckingAccount._data_and_time()))
    
    def check_overdraft(self):
        print('Your checking account overdraft limit is R${:,.2f}'.format(self._Account_limit()))

    def check_statement(self):
        print('Balance Statement:')
        print('Amount, Balance, Date and Time')
        for transaction in self.transactions:
            print(transaction)

    def transfer(self, amount, receipient_acc):
        self.balance -= amount
        self.transactions.append((-amount, 'Balance: {}'.format(self.balance), CheckingAccount._data_and_time()))
        receipient_acc.balance += amount 
        receipient_acc.transactions.append((amount, 'Balance: {}'.format(receipient_acc.balance), CheckingAccount._data_and_time()))


account_test = CheckingAccount("test", "444.111.222-77", "002", "002.001.00102-91")
account_test.check_account_balance()

account_test.deposit(10000)
account_test.check_account_balance()

time.sleep(3)

account_test.withdraw(11000)

print("Current balance: ")
account_test.check_account_balance()
account_test.check_overdraft()

print('-' * 20)
account_test.check_statement()

print('-' * 20)
another_acc= CheckingAccount('Another_Acc', '434.234.543-45', 455, 2456533)
account_test.transfer(1000, another_acc)

account_test.check_account_balance()
another_acc.check_account_balance()

account_test.check_statement()
another_acc.check_statement()


