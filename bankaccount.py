class BankAccount:
    def __init__(self):
        self.balance = 0

    def deposit(self, amount):
        self.balance = self.balance + amount

    def _withdraw(self, amount):
        self.balance = self.balance - amount

    def __showbalance(self):
        print("available balance is " , self.balance)

    def IsAuth_true(self,IsAuth):
        if IsAuth:
            print("welcome")
            self.__showbalance()
        else:
            print("bye bye")

    def Is_withdraw_auth_True(self,IsAuth_withdraw,amount):
        if IsAuth_withdraw:
            print("welcome")
            self._withdraw(amount)
        else:
            print("bye NO BALANCE")



account = BankAccount()
account.deposit(1000)
#account._withdraw(501)
account.Is_withdraw_auth_True(True,900)
account.IsAuth_true(False)
