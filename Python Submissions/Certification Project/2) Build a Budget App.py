import math

class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []

    def deposit(self, amount, description=''):
        self.ledger.append({'amount' : amount, 'description' : description})

    def withdraw(self, amount, description=''):
        if self.check_funds(amount):
            self.ledger.append({'amount' : -amount, 'description' : description})
            return True
        return False
    
    def get_balance(self):
        balance = 0
        for transaction in self.ledger:
            balance += transaction.get('amount')
        return balance
    
    def transfer(self, amount, category):
        if self.check_funds(amount):
            self.withdraw(amount, f'Transfer to {category.name}')
            category.deposit(amount, f'Transfer from {self.name}')
            return True
        return False

    def check_funds(self, amount):
        return amount <= self.get_balance()

    def __str__(self):
        length = len(self.name)
        stars = '*' * ((30 - length) // 2)
        receipt = f'{stars}{self.name}{stars}'
        
        total = 0
        for transaction in self.ledger:
            amount = transaction.get('amount')
            desc = transaction.get('description')
            if len(desc) < 23:
                desc += ' ' * (23 - len(desc))
            elif len(desc) > 23:
                desc = desc[0:23]

            receipt += f'\n{desc}{amount:7.2f}'
            total += amount
        receipt += f'\nTotal: {total}'
        return receipt


def create_spend_chart(categories):
    spent = []
    for category in categories:
        withdrawn = 0
        for transaction in category.ledger:
            amount = transaction.get('amount')
            if amount < 0:
                withdrawn -= amount
        spent.append(withdrawn)

    total_spent = sum(spent)
    percentages = [int((amount / total_spent * 100) // 10 * 10) for amount in spent]

    bar_chart = 'Percentage spent by category\n'
    for value in range(100, -1, -10):
        bar_chart += str(value).rjust(3) + "| "
        for percent in percentages:
            bar_chart += 'o  ' if percent >= value else '   '
        bar_chart += "\n"

    bar_chart += "    " + "-" * (3 * len(categories) + 1)

    max_len = max(len(category.name) for category in categories)
    names = [category.name.ljust(max_len) for category in categories]
    for i in range(max_len):
        bar_chart += "\n     "
        for name in names:
            bar_chart += name[i] + "  "

    return bar_chart


