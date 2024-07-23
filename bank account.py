class BalanceException(Exception):
    pass


class BankAccount:
    def __init__(self,initialamnt,acctname):
        self.balance=initialamnt
        self.name=acctname
        #print("\nAccount created for",self.name,"\nBalance = ",self.balance)
        #here f print is used.it is a way to string format {eg}/:.2f is decimal points
        print(f"\nAccount created for {self.name}.\nBalance = \u20B9{self.balance:.2f}")

    def getbalance(self):
        print(f"\nAccount {self.name} balance=\u20B9{self.balance:.2f}")


    def deposit(self,amount):
        #self.balance=self.balance+amount
        self.balance+=amount
        print(self.balance)
        print("Deposit completed successfully")
        #self.getbalance()
        
    def Viabletranscation(self,amount):
        if self.balance>=amount:
            return
        else:
            raise BalanceException(f"\nSorry account {self.name} your account has a only balance of \u20B9{self.balance:.2f}")
            
    def withdraw(self,amount):
        try:
            self.Viabletranscation(amount)
            self.balance-=amount
            print(self.balance)
            print("Withdraw completed successfully")
            self.getbalance
        except BalanceException as error:
            print(f"\nWithdraw Interrupted:{error}")

            
    def transfer(self,amount,account):
        try:
            print("\n****Beginning Transfer****")
            self.Viabletranscation(amount)
            self.withdraw(amount)
            account.deposit(amount)
            print("\n****Transfer completed****")
        except BalanceException as error:
            print("\n ****Transfer Failed {error}****")
    

        

print("\t\t\t**************Account Details***************")
Gopinath = BankAccount(5000,"Gopinath")
Imam=BankAccount(2500,"Imam")
print("\n\n")


print("\t\t\t**************Balance Details***************")
Gopinath.getbalance()
Imam.getbalance()
print("\n\n")


print("\t\t\t**************Cash Deposit Details***************")
Gopinath.deposit(1000)
Imam.deposit(1000)
print("\n\n")

print("\t\t\t**************Cash Withdraw Details***************")
Gopinath.withdraw(100)
print("\n\n")

print("\t\t\t**************Online Transaction Details***************")
Gopinath.transfer(200,Imam)
