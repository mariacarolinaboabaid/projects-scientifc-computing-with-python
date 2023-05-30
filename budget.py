# CLASS ------------------------------------------------------------------------------------------------------------------------------------------------------------
class Category:
  
    # Creating the attributes
    def __init__(self, category):
        self.category = category
        self.ledger = list() 
        
    # Printing the category
    def __str__(self):
        first_line = self.category.center(30, "*") 
        middle_line = ''
        total = 0
        for item in self.ledger:
            # Adding the spaces to 'description'             
            if len(item['description']) < 23:
                item['description'] = item['description'].ljust(23)
            else: 
                item['description'] = item['description'][0:23]
            # Adding the spaces to 'amount'
            item['amount'] = "{:.2f}".format(float(item["amount"]))
            if len(item['amount']) < 7:
                item['amount'] = item['amount'].rjust(7)
            else: 
                item['amount'] = item['amount'][0:7]
            middle_line += item['description'] + item['amount'] + '\n'
            total += float(item['amount'])
        total = "{:.2f}".format(total)
        return first_line + "\n" + middle_line + "Total: " + str(total)
            
    # Method GET BALANCE
    def get_balance(self):
        balance = 0
        for item in self.ledger:
            balance += float(item['amount'])
        return balance
        
    # Method CHECK FUNDS
    def check_funds(self, value):
        bal = self.get_balance()
        if value > bal:
            return False
        else: 
            return True
    
    # Method DEPOSIT    
    def deposit (self, value, desc=""):
        self.ledger.append({"amount": value, "description": desc})
      
    # Method WITHDRAW
    def withdraw (self, value, desc='' ):
        if self.check_funds(value) == True:
            self.ledger.append({"amount": value * -1, "description": desc})      
            return True
        else:
            return False
    
    # Method TRANSFER
    def transfer (self, value, destiny):
        if self.check_funds(value) == True:
            self.withdraw(value, "Transfer to " + destiny.category)
            destiny.deposit(value, "Transfer from " + self.category)
            return True
        else:
            return False

    # Method GET WITHDRAWS
    def get_withdraws(self):
        total_spent = 0
        for item in self.ledger:
            item['amount'] = float(item['amount'])
            if item['amount'] < 0:
                total_spent += item['amount']
        return total_spent


# FUNCTION ------------------------------------------------------------------------------------------------------
def truncate(n):
    multiplier = 10
    return int(n * multiplier) / multiplier

def get_totals(categories):
    total = 0
    breakdown = []
    for category in categories:
        total += category.get_withdraws()
        breakdown.append(category.get_withdraws())
        print(total, breakdown)
    rounded = list(map(lambda x: truncate(x / total), breakdown))
    return rounded

def create_spend_chart (categories):
    # Getting the categories names
    result = '''Percentage spent by category\n'''
    # Calculating the percentage 
    percentage = get_totals(categories)
    # Making the table of percentage
    for count in range(100, -10, -10): 
        check = ''
        for perc in percentage:
            if (perc * 100) >= count:
                check += " o "
            else:
                check += '   '
        check += ' \n'  
        # Adding the spaces
        count = str(count).rjust(3)
        result += count + '|' + check
     # Adding the line of dashes
    dashes =  "-" * (len(percentage) * 3) + '-'
    # Printing the categories
    names = []
    for item in categories:
        names.append(item.category)
    x_axis = '' 
    maxi = max(names, key=len)
    for x in range(len(maxi)):
        nameString = '     '
        for name in names:
            if x >= len(name):
                nameString += '   '
            else:
                nameString += name[x] + '  '
        if (x != len(maxi) - 1):
            nameString += '\n'
        x_axis += nameString
    result += '    ' + dashes + '\n' + x_axis
    return result

food = Category("Food")
food.deposit(900, "deposit")
food.withdraw(105.55)

entertainment = Category("Entertainment")
entertainment.deposit(900, "deposit")
entertainment.withdraw(33.40)

business = Category("Business")
business.deposit(900, "deposit")
business.withdraw(10.99)


print(create_spend_chart([business, food, entertainment]))