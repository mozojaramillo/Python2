class usuario:
    def __init__(self, name, email, account_balance):
        self.name = name
        self.email = email
        self.account_balance = account_balance
        
    
    def make_deposit(self, amount):
        self.account_balance += amount

        return self    

        
    def make_withdrawal(self, amount):
        self.account_balance -= amount
        return self    

    def display_user_balance(self):
        print(self.account_balance)
        return self    
        
    def transfer_money(self, destinatario, amount):
        destinatario.make_deposit(amount)
        self.make_withdrawal((amount))
        self.display_user_balance()
        destinatario.display_user_balance()

        return self    

Guido = usuario("Guido", "guido@you.com", 0)
Aldo = usuario("Aldo", "guido@you.com", 0)
Belen = usuario("Belen", "guido@you.com", 0)

print(Guido.name)

Guido.make_deposit(1000).make_deposit(2000).make_withdrawal(400)

print(Guido.account_balance)

print(Aldo.name)

Aldo.make_deposit(5000).make_deposit(2000).make_withdrawal(400).make_withdrawal(700)

print(Aldo.account_balance)

print(Belen.name)

Belen.make_deposit(5000).make_withdrawal(7000).make_withdrawal(400).make_withdrawal(700)

print(Belen.account_balance)

Guido.transfer_money(Belen, 3200)



