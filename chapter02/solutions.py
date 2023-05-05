

# Solutions to the Exercies 


# Part One. Reinforcement

###################################################################################################


# R2.4 Write a Python class, Flower, that has three instance variables of type str,
# int, and float, that respectively represent the name of the flower, its num-ber 
# of petals, and its price. Your class must include a constructor method that 
# initializes each variable to an appropriate value, and your class should
# include methods for setting the value of each type, and retrieving the value
# of each type. 


# (1).Adopt set() and get() discriptive methods 


class Flower:
    def __init__(self, name=None, petals=None, price=None):
        self._name, self._petals, self._price = None, None, None   
        self.set_name(name)
        self.set_petals(petals)
        self.set_price(price)
    def set_name(self, name):
        try:
            self._name = str(name)
        except:
            print('Invalid input for a name, it must be a string') 
    def set_petals(self, petals):
        try:
            self._petals = petals
        except:
            print('Invalid input')  
    def set_price(self, price):
        if price is not None: 
            try:
                self._price = float(price)
            except:
                print('Invalid price, must be a number (no dollar sign)')  
    def get_name(self):
        if self._name is None: 
            return ('Attribute has not been set')
        else: 
            return self._name
    def get_petals(self):
        if self._petals is None: 
            return ('Attribute has not been set')
        else: 
            return self._petals            
    def get_price(self):
        if self._price is None: 
            return ('Attribute has not been set')
        else: 
            return self._price


if __name__ == '__main__':
    Dand = Flower('Dandelion', 5, '$10.32')
    print(Dand.get_name(), Dand.get_petals(), Dand.get_price())
    print ('\n')
    Rose = Flower()
    print(Rose.get_name(), Rose.get_petals(), Rose.get_price())
    Rose.set_name('Rose')
    Rose.set_price(20)
    Rose.set_petals(30)
    print(Rose.get_name(), Rose.get_petals(), Rose.get_price())


# Output:

"""
Invalid price, must be a number (no dollar sign)
Dandelion 5 Attribute has not been set

None Attribute has not been set Attribute has not been set
Rose 30 20.0
"""

#--------------------------------------------------------------------------------------------


# (2).Adopt general methods 


class Flower(object):
    """
    name: num price
    change_name: change_num   change_price
    """
    def __init__(self, num, name, price):
        self.name  = name
        self.num = num
        self.price = price
    def change_name(self,name):
        self.name = name
    def change_num(self,num):
        self.num = num
    def change_price(self,price):
        self.price = price
    def show(self):
        print("There are %d bunches %s with $%d per bunch"%(self.num, self.name, self.price))


if __name__ == '__main__':
    f = Flower(10, 'carnations', 1)
    f.show()
    f.change_num(100)
    f.show()


# Output:

"""
There are 10 bunches carnations with $1 per bunch
There are 100 bunches carnations with $1 per bunch
"""

##############################################################################################


# R2.5 使用１.7节的计数修订CreditCard类中的方法

# Use the techniques of Section 1.7 to revise the charge and make payment
# methods of the CreditCard class to ensure that the caller sends a number
# as a parameter.


# (1).Only use one class of CarditCard


class CreditCard:
    """A consumer credit card."""
    def __init__(self, customer, bank, acnt, limit):
        """
        Create a new credit card instance.
        The initial balance is zero.
        customer  the name of the customer (e.g., 'John Bowman')
        bank      the name of the bank (e.g., 'California Savings')
        acnt      the acount identifier (e.g., '5391 0375 9387 5309')
        limit     credit limit (measured in dollars)
        """
        self._customer = customer
        self._bank = bank
        self._account = acnt
        self._limit = limit
        self._balance = 0
    def get_customer(self):
        # Return name of the customer.
        return self._customer
    def get_bank(self):
        # Return the bank's name.
        return self._bank
    def get_account(self):
        # Return the card identifying number (typically stored as a string).
        return self._account
    def get_limit(self):
        # Return current credit limit.
        return self._limit
    def get_balance(self):
        # Return current balance.
        return self._balance
    def charge(self, price):
        # Charge given price to the card, assuming sufficient credit limit.
        try:
            price = float(price)
        except:
            print('Invalid input')
        # Return True if charge was processed; False if charge was denied.
        if price + self._balance > self._limit:  # if charge would exceed limit,
            print(f'Your deposit of {price} exceeds your remainder of {self.get_limit()-self.get_balance()}')
            return False                         # cannot accept charge
        else:
            self._balance += price
            return True
    def make_payment(self, amount):
        # Process customer payment that reduces balance."""
        try:
            amount = float(amount)
        except:
            print('Invalid input')
        self._balance -= amount
        return True


if __name__ == '__main__':
    cc1 = CreditCard('Andrew', 'ABC', '1234567890', 1000)
    cc1.make_payment(100)
    print(cc1.get_balance())
    cc1.charge(100)
    print(cc1.get_balance()) 
    cc1.charge(500) 
    print(cc1.get_balance()) 
    cc1.charge(200) 
    print(cc1.get_balance()) 
    cc1.charge(100)
    print(cc1.get_balance()) 
    cc1.charge(500)
    print(cc1.get_balance()) 
    cc1.charge("100")
    print(cc1.get_balance())
    cc1.charge("20")
    print(cc1.get_balance())
    cc1.charge("453.4")
    print(cc1.get_balance())


# Output:

"""
True
-100.0
True
0.0
True
500.0
True
700.0
True
800.0
Your deposit of 500.0 exceeds your remainder of 200.0
False
800.0
True
900.0
True
920.0
Your deposit of 453.4 exceeds your remainder of 80.0
False
920.0
"""

#---------------------------------------------------------------------------------------------


# (2).USe CreditCard class  and its subclass SubCreditCard


class CreditCard:
    """A consumer credit card."""
    def __init__(self, customer, bank, acnt, limit):
        """
        Create a new credit card instance.
        The initial balance is zero.
        customer  the name of the customer (e.g., 'John Bowman')
        bank      the name of the bank (e.g., 'California Savings')
        acnt      the acount identifier (e.g., '5391 0375 9387 5309')
        limit     credit limit (measured in dollars)
        """
        self._customer = customer
        self._bank = bank
        self._account = acnt
        self._limit = limit
        self._balance = 0   # Additional instance variable 
    def get_customer(self):
        # Return name of the customer.
        return self._customer
    def get_bank(self):
        # Return the bank's name.
        return self._bank
    def get_account(self):
        # Return the card identifying number (typically stored as a string).
        return self._account
    def get_limit(self):
        # Return current credit limit.
        return self._limit
    def get_balance(self):
        # Return current balance.
        return self._balance
    def charge(self, price):
        # Charge given price to the card, assuming sufficient credit limit.
        # Return True if charge was processed; False if charge was denied.
        if price + self._balance > self._limit:  # if charge would exceed limit,
            return False                         # cannot accept charge
        else:
            self._balance += price
            return True
    def make_payment(self, amount):
        # Process customer payment that reduces balance."""
        self._balance -= amount


class SubCreditCard(CreditCard):
    def __init__(self, customer, bank, acnt, limit, plus=None):
        if plus:
            self.plus = plus
        else :
            self.plus = None
        super().__init__(customer, bank, acnt, limit)
    def charge(self,price):
        try:
            if price+self._balance > self._limit:
                return False
            else:
                self._balance+=price
        except :
            print('pleace input a num')
    def make_payment(self,amount):
        try:
            self._balance-=amount
        except:
            print('pleace input a num')
            quit()
        if amount<0:
                raise ValueError
    def get_accountp(self):
        if self.plus:
            return self.plus
        else:
            print('No one in our accountr')
        

if __name__=="__main__":
    sub = SubCreditCard('John Bowman', 'California Savings',
                           '5391 0375 9387 5309', 2500,666)
    print(sub.get_balance())            
    sub.make_payment(1)    
    print(sub.get_balance())                
    print(sub.get_accountp())               


# Output:

"""
0
-1
666
"""

##############################################################################################


# R2.6 If the parameter to the make payment method of the CreditCard class
# were a negative number, that would have the effect of raising the balance
# on the account. Revise the implementation so that it raises a ValueError if
# a negative value is sent.


class CreditCard:
    """A consumer credit card."""
    def __init__(self, customer, bank, acnt, limit):
        """
        Create a new credit card instance.
        The initial balance is zero.
        customer  the name of the customer (e.g., 'John Bowman')
        bank      the name of the bank (e.g., 'California Savings')
        acnt      the acount identifier (e.g., '5391 0375 9387 5309')
        limit     credit limit (measured in dollars)
        """
        self._customer = customer
        self._bank = bank
        self._account = acnt
        self._limit = limit
        self._balance = 0
    def get_customer(self):
        # Return name of the customer.
        return self._customer
    def get_bank(self):
        # Return the bank's name.
        return self._bank
    def get_account(self):
        # Return the card identifying number (typically stored as a string).
        return self._account
    def get_limit(self):
        # Return current credit limit.
        return self._limit
    def get_balance(self):
        # Return current balance.
        return self._balance
    def charge(self, price):
        # Charge given price to the card, assuming sufficient credit limit.
        try:
            price = float(price)
        except:
            print('Invalid input')
        # Return True if charge was processed; False if charge was denied.
        if price + self._balance > self._limit:  # if charge would exceed limit,
            print(f'Your deposit of {price} exceeds your remainder of {self.get_limit()-self.get_balance()}')
            return False                         # cannot accept charge
        else:
            self._balance += price
            return True
    def make_payment(self, amount):
        # Process customer payment that reduces balance."""
        try:
            amount = float(amount)
        except:
            print('Invalid input')
        self._balance -= amount
        return True


class CreditCardWithoutNegatives(CreditCard):
    def make_payment(self, amount):
        try:
            amount = float(amount)
        except:
            print('Invalid Input')
            return False
        if amount < 0:
            raise ValueError('Cannot make negative payments and try the charge method')
        else:
            self._balance
            return True


if __name__ == '__main__':
    cc1 = CreditCardWithoutNegatives('Andrew', 'ABC', '1234567890', 1000)
    cc1.make_payment(100)
    print(cc1.get_balance())
    cc1.charge(100)
    print(cc1.get_balance()) 
    cc1.charge(500) 
    print(cc1.get_balance()) 
    cc1.charge(200) 
    print(cc1.get_balance()) 
    cc1.charge(100)
    print(cc1.get_balance()) 
    cc1.charge(500)
    print(cc1.get_balance()) 
    cc1.charge("100")
    print(cc1.get_balance())
    cc1.charge("20")
    print(cc1.get_balance())
    cc1.charge("453.4")
    print(cc1.get_balance())
    try:
        cc1.make_payment("-453.4")
        print(cc1.get_balance())
    except Exception as e:
        print(e)


# Output:

"""
True
0
True
100.0
True
600.0
True
800.0
True
900.0
Your deposit of 500.0 exceeds your remainder of 100.0
False
900.0
True
1000.0
Your deposit of 20.0 exceeds your remainder of 0.0
False
1000.0
Your deposit of 453.4 exceeds your remainder of 0.0
False
1000.0
Cannot make negative payments and try the charge method
"""

##############################################################################################


# R2.7 The CreditCard class of Section 2.3 initializes the balance of a new ac-
# count to zero. Modify that class so that a new account can be given a
# nonzero balance using an optional fifth parameter to the constructor. The
# four-parameter constructor syntax should continue to produce an account
# with zero balance.


class CreditCard():
    def __init__(self, customer, bank, acnt, limit):
        self._customer = customer
        self._bank = bank
        self._account = acnt
        self._limit = limit
        self._balance = 0  # Start with a balance of zero
    def get_customer(self):
        return self._customer
    def get_bank(self):
        return self._bank
    def get_account(self):
        return self._account
    def get_limit(self):
        return self._limit
    def get_balance(self):
        return self._balance
    def set_balance(self, value):
        self._balance = value
    def charge(self, price):
        try:
            price = float(price)  #This will accept an int, float or string that can be converted to a float
        except:
            print ('Invalid input')
            return False       
        if price+self._balance >self._limit:
            print(f'Your deposit of {price} exceeds your remainder of {self.get_limit()-self.get_balance()}')
            return False #You are going over your limit
        else:
            self._balance += price
            return True
    def make_payment(self, amount):
        try:
            amount = float(amount)  #This will accept an int, float or string that can be converted to a float
        except:
            print ('Invalid input')
            return False 
        self._balance -= amount
        return True


class CreditCardWithBalance(CreditCard):
    def __init__(self, customer, bank, acnt, limit, balance=0):
        self._balance = balance
        super().__init__(customer, bank, acnt, limit)


if __name__ == '__main__':
    cc1 = CreditCardWithBalance('Andrew', 'JPMorgan', '1234567890', 1000, 50)
    cc1.make_payment(100)
    print(cc1.get_balance())
    cc1.charge(100)
    print(cc1.get_balance()) 
    cc1.charge(500) 
    print(cc1.get_balance()) 
    cc1.charge(200) 
    print(cc1.get_balance()) 
    cc1.charge(100)
    print(cc1.get_balance()) 
    cc1.charge(500)
    print(cc1.get_balance()) 
    cc1.charge("100")
    print(cc1.get_balance())
    cc1.charge("20")
    print(cc1.get_balance())
    cc1.charge("453.4")
    print(cc1.get_balance())


# Output:

"""
True
-100.0
True
0.0
True
500.0
True
700.0
True
800.0
Your deposit of 500.0 exceeds your remainder of 200.0
False
800.0
True
900.0
True
920.0
Your deposit of 453.4 exceeds your remainder of 80.0
False
920.0
"""

##############################################################################################


# R 2.8 Modify the declaration of the first for loop in the CreditCard tests, from
# Code Fragment 2.3, so that it will eventually cause exactly one of the three
# credit cards to go over its credit limit. Which credit card is it? We make one of 
# the three credit card to exceed its credit quota. 


class CreditCard:
    """A consumer credit card."""
    def __init__(self, customer, bank, acnt, limit):
        """
        Create a new credit card instance.
        The initial balance is zero.
        customer  the name of the customer (e.g., 'John Bowman')
        bank      the name of the bank (e.g., 'California Savings')
        acnt      the acount identifier (e.g., '5391 0375 9387 5309')
        limit     credit limit (measured in dollars)
        """
        self._customer = customer
        self._bank = bank
        self._account = acnt
        self._limit = limit
        self._balance = 0
    def get_customer(self):
        # Return name of the customer.
        return self._customer
    def get_bank(self):
        # Return the bank's name.
        return self._bank
    def get_account(self):
        # Return the card identifying number (typically stored as a string).
        return self._account
    def get_limit(self):
        # Return current credit limit.
        return self._limit
    def get_balance(self):
        # Return current balance.
        return self._balance
    def charge(self, price):
        # Charge given price to the card, assuming sufficient credit limit.
        try:
            price = float(price)
        except:
            print('Invalid input')
        # Return True if charge was processed; False if charge was denied.
        if price + self._balance > self._limit:  # if charge would exceed limit,
            print(f'Your deposit of {price} exceeds your remainder of {self.get_limit()-self.get_balance()}')
            return False                         # cannot accept charge
        else:
            self._balance += price
            return True
    def make_payment(self, amount):
        # Process customer payment that reduces balance."""
        try:
            amount = float(amount)
        except:
            print('Invalid input')
        self._balance -= amount
        return True


class CreditCardSelfReport(CreditCard):
    def special_charge(self, amount):
        if super().charge(amount): 
            return True
        else:
            print("Credit card has failed:", self.get_bank())
    

if __name__ == '__main__':   
    wallet = []
    wallet.append(CreditCardSelfReport('John Bowman' , 'California Savings' ,'56 5391 0375 9387 5309' , 2500))
    wallet.append(CreditCardSelfReport('John Bowman' , 'California Federal' ,'3485 0399 3395 1954' , 3500))
    wallet.append(CreditCardSelfReport('John Bowman' , 'California Finance' ,'5391 0375 9387 5309' , 5000))
    for val in range (1,100):
        wallet[0].special_charge(val)
        wallet[1].special_charge(2*val)
        wallet[2].special_charge(3*val)
    for c in range(3):
        print ('Customer = ', wallet[c].get_customer())
        print ('Bank = ', wallet[c].get_bank())
        print('Account = ', wallet[c].get_account())
        print ('Limit = ', wallet[c].get_limit())
        print('Balance = ', wallet[c].get_balance())
        while wallet[c].get_balance()>100:
            wallet[c].make_payment(100)
            print('New Balance = ', wallet[c].get_balance())
        print()


# Ouput:

"""
...
True
...
Your deposit of 174.0 exceeds your remainder of 41.0
Credit card has failed: California Finance
True
Your deposit of 118.0 exceeds your remainder of 78.0
Credit card has failed: California Federal
Your deposit of 177.0 exceeds your remainder of 41.0
Credit card has failed: California Finance
True
Your deposit of 120.0 exceeds your remainder of 78.0
Credit card has failed: California Federal
Your deposit of 180.0 exceeds your remainder of 41.0
Credit card has failed: California Finance
True
Your deposit of 122.0 exceeds your remainder of 78.0
Credit card has failed: California Federal
Your deposit of 183.0 exceeds your remainder of 41.0
Credit card has failed: California Finance
True
Your deposit of 124.0 exceeds your remainder of 78.0
Credit card has failed: California Federal
Your deposit of 186.0 exceeds your remainder of 41.0
Credit card has failed: California Finance
True
Your deposit of 126.0 exceeds your remainder of 78.0
Credit card has failed: California Federal
Your deposit of 189.0 exceeds your remainder of 41.0
Credit card has failed: California Finance
True
...
Your deposit of 99.0 exceeds your remainder of 15.0
Credit card has failed: California Savings
Your deposit of 198.0 exceeds your remainder of 78.0
Credit card has failed: California Federal
Your deposit of 297.0 exceeds your remainder of 41.0
Credit card has failed: California Finance
Customer =  John Bowman
Bank =  California Savings
Account =  56 5391 0375 9387 5309
Limit =  2500
Balance =  2485.0
True
New Balance =  2385.0
True
...
Customer =  John Bowman
Bank =  California Finance
Account =  5391 0375 9387 5309
Limit =  5000
Balance =  4959.0
True
New Balance =  4859.0
True
"""

##############################################################################################


# 2.9 Implement the sub method for the Vector class of Section 2.3.3, so
# that the expression u−v returns a new vector instance representing the
# difference between two vectors.

# (1).Add the new method of __sub__()

# Realize the method of __sub__() and make thye u-v expression return a new vector


class Vector:
    def __init__(self, d):
        self._coords = [0]*d
    def __len__(self):
        return len(self._coords)
    def __getitem__(self, j):
        return self._coords[j]
    def __setitem__(self, j, val):
        try:
            self._coords[j] = val
            return True
        except:
            print('Invalid input or index')
            return False
    def __add__(self, other):
        if len(self) != len(other):
            raise ValueError('Dimensions must match')
        result = Vector(len(self))
        for j in range(len(self)):
            result[j] = self[j] + other[j]
        return result      
    def __eq__(self, other):
        return self._coords == other._coords
    def __ne__(self, other):
        return not self==other
    def __str__(self):
        return '<' + str(self._coords)[1:-1] + '>'
    def __sub__(self, other):
        if len(self) != len(other):
            raise ValueError('Dimensions must match')
        result = Vector(len(self))
        for j in range (len(self)):
            result[j] = self[j] - other[j]
        return result


if __name__ == '__main__':     
    v1 = Vector(5)
    v2 = Vector (5)
    for i in range(5):
        v1[i] = 5
        v2[i] = i   
    print (v1+v2)
    print (v1-v2)
    print (v2-v1)


# Output:

"""
<5, 6, 7, 8, 9>
<5, 4, 3, 2, 1>
<-5, -4, -3, -2, -1>
"""

#---------------------------------------------------------------------------------------------


# (2).Add NewVector subclass 


import collections


class Vector:
    """Represent a vector in a multidimensional space."""
    def __init__(self, d):
        if isinstance(d, int):
            self._coords = [0] * d
        else:                                  
            try: # we test if param is iterable
                self._coords = [val for val in d]
            except TypeError:
                raise TypeError('invalid parameter type')
    def __len__(self):
        # Return the dimension of the vector.
        return len(self._coords)
    def __getitem__(self, j):
        # Return jth coordinate of vector.
        return self._coords[j]
    def __setitem__(self, j, val):
        # Set jth coordinate of vector to given value.
        self._coords[j] = val
    def __add__(self, other):
        # Return sum of two vectors.
        if len(self) != len(other):          # relies on __len__ method
            raise ValueError('dimensions must agree')
        result = Vector(len(self))           # start with vector of zeros
        for j in range(len(self)):
            result[j] = self[j] + other[j]
        return result
    def __eq__(self, other):
        # Return True if vector has same coordinates as other.
        return self._coords == other._coords
    def __ne__(self, other):
        # Return True if vector differs from other.
        return not self == other             # rely on existing __eq__ definition
    def __str__(self):
        # Produce string representation of vector.
        return '<' + str(self._coords)[1:-1] + '>'  # adapt list representation
    def __neg__(self):
        # Return copy of vector with all coordinates negated.
        result = Vector(len(self))           # start with vector of zeros
        for j in range(len(self)):
            result[j] = -self[j]
        return result
    def __lt__(self, other):
        # Compare vectors based on lexicographical order.
        if len(self) != len(other):
            raise ValueError('dimensions must agree')
        return self._coords < other._coords
    def __le__(self, other):
        # Compare vectors based on lexicographical order.
        if len(self) != len(other):
            raise ValueError('dimensions must agree')
        return self._coords <= other._coords


class NewVector(Vector):
    """d is a len of list or a list"""
    def __init__(self,d):
        super().__init__(d)
    def __sub__(self, other):
        if len(self) != len(other):
            raise ValueError('Dimensions must match')
        result = Vector(len(self))
        for j in range (len(self)):
            result[j] = self[j] - other[j]
        return result


if __name__ == '__main__':     
    v1 = NewVector(5)
    v2 = NewVector(5)
    for i in range(5):
        v1[i] = 5
        v2[i] = i   
    print(v1+v2)
    print(v1-v2)
    print(v2-v1)


# Output:

"""
<5, 6, 7, 8, 9>
<5, 4, 3, 2, 1>
<-5, -4, -3, -2, -1>
"""

#---------------------------------------------------------------------------------------------


# (3).Add PredatoryVector subclass


import collections


class Vector:
    """Represent a vector in a multidimensional space."""
    def __init__(self, d):
        if isinstance(d, int):
            self._coords = [0] * d
        else:                                  
            try: # we test if param is iterable
                self._coords = [val for val in d]
            except TypeError:
                raise TypeError('invalid parameter type')
    def __len__(self):
        # Return the dimension of the vector.
        return len(self._coords)
    def __getitem__(self, j):
        # Return jth coordinate of vector.
        return self._coords[j]
    def __setitem__(self, j, val):
        # Set jth coordinate of vector to given value.
        self._coords[j] = val
    def __add__(self, other):
        # Return sum of two vectors.
        if len(self) != len(other):          # relies on __len__ method
            raise ValueError('dimensions must agree')
        result = Vector(len(self))           # start with vector of zeros
        for j in range(len(self)):
            result[j] = self[j] + other[j]
        return result
    def __eq__(self, other):
        # Return True if vector has same coordinates as other.
        return self._coords == other._coords
    def __ne__(self, other):
        # Return True if vector differs from other.
        return not self == other             # rely on existing __eq__ definition
    def __str__(self):
        # Produce string representation of vector.
        return '<' + str(self._coords)[1:-1] + '>'  # adapt list representation
    def __neg__(self):
        # Return copy of vector with all coordinates negated.
        result = Vector(len(self))           # start with vector of zeros
        for j in range(len(self)):
            result[j] = -self[j]
        return result
    def __lt__(self, other):
        # Compare vectors based on lexicographical order.
        if len(self) != len(other):
            raise ValueError('dimensions must agree')
        return self._coords < other._coords
    def __le__(self, other):
        # Compare vectors based on lexicographical order.
        if len(self) != len(other):
            raise ValueError('dimensions must agree')
        return self._coords <= other._coords


class PredatoryVector(Vector):
    """d is a len of list or a list"""
    def __init__(self,d):
        super().__init__(d)
    #2.9
    def __sub__(self,other):
        if len(self)!=len(other):
            raise ValueError('dimensions must agree')
        else:
            try:
                result=PredatoryVector([self[i]-other[i] for i in range(len(self))])
                return  result
            except:
                raise TypeError('the list must be num')
        

if __name__=="__main__":
    p1=PredatoryVector((1,2,3))
    p2=PredatoryVector([4,5,6])
    print('p1 is :',p1)
    print('p2 is :',p2)
    print('p2-p1:',p2-p1)


# Output:

"""    
p1 is : <1, 2, 3>
p2 is : <4, 5, 6>
p2-p1: <3, 3, 3>
"""

##############################################################################################


# 2.10 Implement the neg method for the Vector class of Section 2.3.3, so
# that the expression −v returns a new vector instance whose coordinates
# are all the negated values of the respective coordinates of v. 

# (1).Add the new method __neg__()

# Realize the method of __sub__() and make thye u-v expression return a new vector. 
# The corrdinate of the new vector v is negative value


class Vector:
    def __init__(self, d):
        self._coords = [0]*d
    def __len__(self):
        return len(self._coords)
    def __getitem__(self, j):
        return self._coords[j]
    def __setitem__(self, j, val):
        try:
            self._coords[j] = val
            return True
        except:
            print('Invalid input or index')
            return False
    def __add__(self, other):
        if len(self)!=len(other):
            raise ValueError('Dimensions must match')
        result = Vector(len(self))
        for j in range(len(self)):
            result[j] = self[j] + other[j]
        return result
    def __eq__(self, other):
        return self._coords == other._coords
    def __ne__(self, other):
        return not self==other
    def __str__(self):
        return '<' + str(self._coords)[1:-1] + '>'
    def __sub__(self, other):
        if len(self) != len(other):
            raise ValueError('Dimensions must match')
        result = Vector(len(self))
        for j in range (len(self)):
            result[j] = self[j] - other[j]
        return result


class VectorNeg(Vector):
    """
    def __init__(self,d):
        super().__init__(d)
    """
    def __neg__(self):
        result = Vector(len(self))
        for i in range(len(self)):
            result[i] = -self[i]
        return result
            

if __name__=="__main__":            
    v1 = VectorNeg(5)   
    v2 = VectorNeg(5)
    for i in range(5):
        v1[i] = 5
        v2[i] = i
    print(v1+v2)
    print(v1-v2)
    print(v2-v1)      
    print(-v1, v1)


# Output:

"""
<5, 6, 7, 8, 9>
<5, 4, 3, 2, 1>
<-5, -4, -3, -2, -1>
<-5, -5, -5, -5, -5> <5, 5, 5, 5, 5>
"""

#---------------------------------------------------------------------------------------------


# (2). VectorNeg subclass 


import collections


class Vector:
    """Represent a vector in a multidimensional space."""
    def __init__(self, d):
        if isinstance(d, int):
            self._coords = [0] * d
        else:                                  
            try: # we test if param is iterable
                self._coords = [val for val in d]
            except TypeError:
                raise TypeError('invalid parameter type')
    def __len__(self):
        # Return the dimension of the vector.
        return len(self._coords)
    def __getitem__(self, j):
        # Return jth coordinate of vector.
        return self._coords[j]
    def __setitem__(self, j, val):
        # Set jth coordinate of vector to given value.
        try:
            self._coords[j] = val
            return True
        except:
            print('Invalid input or index')
            return False
    def __add__(self, other):
        # Return sum of two vectors.
        if len(self) != len(other):          # relies on __len__ method
            raise ValueError('dimensions must agree')
        result = Vector(len(self))           # start with vector of zeros
        for j in range(len(self)):
            result[j] = self[j] + other[j]
        return result
    def __eq__(self, other):
        # Return True if vector has same coordinates as other.
        return self._coords == other._coords
    def __ne__(self, other):
        # Return True if vector differs from other.
        return not self == other             # rely on existing __eq__ definition
    def __str__(self):
        # Produce string representation of vector.
        return '<' + str(self._coords)[1:-1] + '>'  # adapt list representation
    def __sub__(self, other):
        if len(self) != len(other):
            raise ValueError('Dimensions must match')
        result = Vector(len(self))
        for j in range (len(self)):
            result[j] = self[j] - other[j]
        return result
    def __lt__(self, other):
        # Compare vectors based on lexicographical order.
        if len(self) != len(other):
            raise ValueError('dimensions must agree')
        return self._coords < other._coords
    def __le__(self, other):
        # Compare vectors based on lexicographical order.
        if len(self) != len(other):
            raise ValueError('dimensions must agree')
        return self._coords <= other._coords   


class VectorNeg(Vector):
    def __init__(self,d):
        super().__init__(d)
    def __neg__(self):
        result = Vector(len(self))
        for i in range(len(self)):
            result[i] = -self[i]
        return result
            

if __name__=="__main__":            
    v1 = VectorNeg(5)   
    v2 = VectorNeg(5)
    for i in range(5):
        v1[i] = 5
        v2[i] = i
    print(v1+v2)
    print(v1-v2)
    print(v2-v1)      
    print(-v1, v1)


# Output:

"""
<5, 6, 7, 8, 9>
<5, 4, 3, 2, 1>
<-5, -4, -3, -2, -1>
<-5, -5, -5, -5, -5> <5, 5, 5, 5, 5>
"""

#---------------------------------------------------------------------------------------------


# (3).VectorNeg subclass 


import collections


class Vector:
    """Represent a vector in a multidimensional space."""
    def __init__(self, d):
        if isinstance(d, int):
            self._coords = [0] * d
        else:                                  
            try: # we test if param is iterable
                self._coords = [val for val in d]
            except TypeError:
                raise TypeError('invalid parameter type')
    def __len__(self):
        # Return the dimension of the vector.
        return len(self._coords)
    def __getitem__(self, j):
        # Return jth coordinate of vector.
        return self._coords[j]
    def __setitem__(self, j, val):
        # Set jth coordinate of vector to given value.
        self._coords[j] = val
    def __add__(self, other):
        # Return sum of two vectors.
        if len(self) != len(other):          # relies on __len__ method
            raise ValueError('dimensions must agree')
        result = Vector(len(self))           # start with vector of zeros
        for j in range(len(self)):
            result[j] = self[j] + other[j]
        return result
    def __eq__(self, other):
        # Return True if vector has same coordinates as other.
        return self._coords == other._coords
    def __ne__(self, other):
        # Return True if vector differs from other.
        return not self == other             # rely on existing __eq__ definition
    def __str__(self):
        # Produce string representation of vector.
        return '<' + str(self._coords)[1:-1] + '>'  # adapt list representation
    def __lt__(self, other):
        # Compare vectors based on lexicographical order.
        if len(self) != len(other):
            raise ValueError('dimensions must agree')
        return self._coords < other._coords
    def __le__(self, other):
        # Compare vectors based on lexicographical order.
        if len(self) != len(other):
            raise ValueError('dimensions must agree')
        return self._coords <= other._coords


class PredatoryVector(Vector):
    """d is a len of list or a list"""
    def __init__(self,d):
        super().__init__(d)
    def __neg__(self):
        # Return copy of vector with all coordinates negated.
        result = Vector(len(self))           # start with vector of zeros
        for j in range(len(self)):
            result[j] = -self[j]
        return result


if __name__=="__main__":
    p1=PredatoryVector((1,2,3))
    print('-p1:',-p1)


# Output:

"""
-p1: <-1, -2, -3>
"""

##############################################################################################


# 2.11

"""
In Section 2.3.3, we note that our Vector class supports a syntax such as
v = u + [5, 3, 10, −2, 1], in which the sum of a vector and list returns
a new vector. However, the syntax v = [5, 3, 10, −2, 1] + u is illegal.
Explain how the Vector class definition can be revised so that this syntax
generates a new vector. 
"""

##############################################################################################


# 2.12 Implement the mul method for the Vector class of Section 2.3.3, so
# that the expression v 3 returns a new vector with coordinates that are 3
# times the respective coordinates of v. 

# (1).Based on the method __sub__(), add both VectorNeg and VectorMult classes to 
# realize the method of __mul__(). 


class Vector:
    """Represent a vector in a multidimensional space."""
    def __init__(self, d):
        if isinstance(d, int):
            self._coords = [0] * d
        else:                                  
            try: # we test if param is iterable
                self._coords = [val for val in d]
            except TypeError:
                raise TypeError('invalid parameter type')
    def __len__(self):
        # Return the dimension of the vector.
        return len(self._coords)
    def __getitem__(self, j):
        # Return jth coordinate of vector.
        return self._coords[j]
    def __setitem__(self, j, val):
        # Set jth coordinate of vector to given value.
        try:
            self._coords[j] = val
            return True
        except:
            print('Invalid input or index')
            return False
    def __add__(self, other):
        # Return sum of two vectors.
        if len(self) != len(other):          # relies on __len__ method
            raise ValueError('dimensions must agree')
        result = Vector(len(self))           # start with vector of zeros
        for j in range(len(self)):
            result[j] = self[j] + other[j]
        return result
    def __eq__(self, other):
        # Return True if vector has same coordinates as other.
        return self._coords == other._coords
    def __ne__(self, other):
        # Return True if vector differs from other.
        return not self == other             # rely on existing __eq__ definition
    def __str__(self):
        # Produce string representation of vector.
        return '<' + str(self._coords)[1:-1] + '>'  # adapt list representation
    def __sub__(self, other):
        if len(self) != len(other):
            raise ValueError('Dimensions must match')
        result = Vector(len(self))
        for j in range (len(self)):
            result[j] = self[j] - other[j]
        return result
    def __lt__(self, other):
        # Compare vectors based on lexicographical order.
        if len(self) != len(other):
            raise ValueError('dimensions must agree')
        return self._coords < other._coords
    def __le__(self, other):
        # Compare vectors based on lexicographical order.
        if len(self) != len(other):
            raise ValueError('dimensions must agree')
        return self._coords <= other._coords   


class VectorNeg(Vector):
    """
    def __init__(self,d):
        super().__init__(d)
    """
    def __neg__(self):
        result = Vector(len(self))
        for i in range(len(self)):
            result[i] = -self[i]
        return result
            

class VectorMult(VectorNeg):
    def __mul__(self, value):
        result = Vector(len(self))
        for i in range(len(self)):
            result[i] = self[i]*value
        return result


if __name__=="__main__":
    vv = VectorMult      
    v1 = vv(5)
    v2 = vv(5)
    for i in range(5):
        v1[i] = 5
        v2[i] = i   
    print(v1+v2)
    print(v1-v2)
    print(v2-v1)      
    print(-v1, v1)
    print(v1*3)


# Output:

"""
<5, 6, 7, 8, 9>
<5, 4, 3, 2, 1>
<-5, -4, -3, -2, -1>
<-5, -5, -5, -5, -5> <5, 5, 5, 5, 5>
<15, 15, 15, 15, 15>
"""

#---------------------------------------------------------------------------------------------


# (2).Realize the method of __mul__(self). 


class Vector:
    def __init__(self, d):
        self._coords = [0]*d
    def __len__(self):
        return len(self._coords)
    def __getitem__(self, j):
        return self._coords[j]
    def __setitem__(self, j, val):
        try:
            self._coords[j] = val
            return True
        except:
            print('Invalid input or index')
            return False
    def __add__(self, other):
        if len(self)!=len(other):
            raise ValueError('Dimensions must match')
        result = Vector(len(self))
        for j in range(len(self)):
            result[j] = self[j] + other[j]
        return result
    def __eq__(self, other):
        return self._coords == other._coords
    def __ne__(self, other):
        return not self==other
    def __str__(self):
        return '<' + str(self._coords)[1:-1] + '>'
    def __sub__(self, other):
        if len(self) != len(other):
            raise ValueError('Dimensions must match')
        result = Vector(len(self))
        for j in range (len(self)):
            result[j] = self[j] - other[j]
        return result


class VectorNeg(Vector):
    """
    def __init__(self,d):
        super().__init__(d)
    """
    def __neg__(self):
        result = Vector(len(self))
        for i in range(len(self)):
            result[i] = -self[i]
        return result
            

class VectorMult(VectorNeg):
    def __mul__(self, value):
        result = Vector(len(self))
        for i in range(len(self)):
            result[i] = self[i]*value
        return result


if __name__=="__main__":
    vv = VectorMult      
    v1 = vv(5)
    v2 = vv(5)
    for i in range(5):
        v1[i] = 5
        v2[i] = i   
    print(v1+v2)
    print(v1-v2)
    print(v2-v1)      
    print(-v1, v1)
    print(v1*3) 
    print(v1*6)


# Output:

"""
<5, 6, 7, 8, 9>
<5, 4, 3, 2, 1>
<-5, -4, -3, -2, -1>
<-5, -5, -5, -5, -5> <5, 5, 5, 5, 5>
<15, 15, 15, 15, 15>
<30, 30, 30, 30, 30>
"""

#---------------------------------------------------------------------------------------------


# (3).Realize the method of __mul__(self). 


import collections


class Vector:
    """Represent a vector in a multidimensional space."""
    def __init__(self, d):
        if isinstance(d, int):
            self._coords = [0] * d
        else:                                  
            try: # we test if param is iterable
                self._coords = [val for val in d]
            except TypeError:
                raise TypeError('invalid parameter type')
    def __len__(self):
        # Return the dimension of the vector.
        return len(self._coords)
    def __getitem__(self, j):
        # Return jth coordinate of vector.
        return self._coords[j]
    def __setitem__(self, j, val):
        # Set jth coordinate of vector to given value.
        self._coords[j] = val
    def __add__(self, other):
        # Return sum of two vectors.
        if len(self) != len(other):          # relies on __len__ method
            raise ValueError('dimensions must agree')
        result = Vector(len(self))           # start with vector of zeros
        for j in range(len(self)):
            result[j] = self[j] + other[j]
        return result
    def __eq__(self, other):
        # Return True if vector has same coordinates as other.
        return self._coords == other._coords
    def __ne__(self, other):
        # Return True if vector differs from other.
        return not self == other             # rely on existing __eq__ definition
    def __str__(self):
        # Produce string representation of vector.
        return '<' + str(self._coords)[1:-1] + '>'  # adapt list representation
    def __neg__(self):
        # Return copy of vector with all coordinates negated.
        result = Vector(len(self))           # start with vector of zeros
        for j in range(len(self)):
            result[j] = -self[j]
        return result
    def __lt__(self, other):
        # Compare vectors based on lexicographical order.
        if len(self) != len(other):
            raise ValueError('dimensions must agree')
        return self._coords < other._coords
    def __le__(self, other):
        # Compare vectors based on lexicographical order.
        if len(self) != len(other):
            raise ValueError('dimensions must agree')
        return self._coords <= other._coords


class PredatoryVector(Vector):
    """d is a len of list or a list"""
    def __init__(self,d):
        super().__init__(d)
    def get_vector(self):
        return self._coords
    def __mul__(self,d):
        if type(d)==int:
            try:
                mid = self.get_vector()
                for i in range(d-1):
                    self+=mid
                return self
            except:
                print('your input is wrong')
        else:
            try:
                result = PredatoryVector(len(d))
                for i in range(len(d)):
                    result[i]=self[i]*d[i]
                return result
            except:
                print('your input is wrong')
                raise TypeError


if __name__=="__main__":
    p1=PredatoryVector((1,2,3))
    print('p1*3:',p1*3)


# Output:

"""
# 1*3: <3, 6, 9>
"""

##############################################################################################


# 2.13 Exercise R-2.12 asks for an implementation of mul , for the Vector
# class of Section 2.3.3, to provide support for the syntax v 3. Implement
# the rmul method, to provide additional support for syntax 3 v. 


# (1).Adopt a base class and three subclass 

class Vector:
    """Represent a vector in a multidimensional space."""
    def __init__(self, d):
        if isinstance(d, int):
            self._coords = [0] * d
        else:                                  
            try: # we test if param is iterable
                self._coords = [val for val in d]
            except TypeError:
                raise TypeError('invalid parameter type')
    def __len__(self):
        # Return the dimension of the vector.
        return len(self._coords)
    def __getitem__(self, j):
        # Return jth coordinate of vector.
        return self._coords[j]
    def __setitem__(self, j, val):
        # Set jth coordinate of vector to given value.
        try:
            self._coords[j] = val
            return True
        except:
            print('Invalid input or index')
            return False
    def __add__(self, other):
        # Return sum of two vectors.
        if len(self) != len(other):          # relies on __len__ method
            raise ValueError('dimensions must agree')
        result = Vector(len(self))           # start with vector of zeros
        for j in range(len(self)):
            result[j] = self[j] + other[j]
        return result
    def __eq__(self, other):
        # Return True if vector has same coordinates as other.
        return self._coords == other._coords
    def __ne__(self, other):
        # Return True if vector differs from other.
        return not self == other             # rely on existing __eq__ definition
    def __str__(self):
        # Produce string representation of vector.
        return '<' + str(self._coords)[1:-1] + '>'  # adapt list representation
    def __sub__(self, other):
        if len(self) != len(other):
            raise ValueError('Dimensions must match')
        result = Vector(len(self))
        for j in range (len(self)):
            result[j] = self[j] - other[j]
        return result
    def __lt__(self, other):
        # Compare vectors based on lexicographical order.
        if len(self) != len(other):
            raise ValueError('dimensions must agree')
        return self._coords < other._coords
    def __le__(self, other):
        # Compare vectors based on lexicographical order.
        if len(self) != len(other):
            raise ValueError('dimensions must agree')
        return self._coords <= other._coords   


class VectorNeg(Vector):
    def __neg__(self):
        result = Vector(len(self))
        for i in range(len(self)):
            result[i] = -self[i]
        return result
            

class VectorMult(VectorNeg):
    def __mul__(self, value):
        result = Vector(len(self))
        for i in range(len(self)):
            result[i] = self[i]*value
        return result


class VectorRMult(VectorMult):
    def __rmul__(self, value):
        return (self * value)  #Treat it like vector*value instead of value*vector


if __name__=="__main__":
    vv = VectorRMult    
    v1 = vv(5)
    v2 = vv(5)
    for i in range(5):
        v1[i] = 5
        v2[i] = i
    print(v1+v2)
    print(v1-v2)
    print(v2-v1)      
    print(-v1, v1)
    print(v1*6)
    print(7*v1)


# Output:

"""
<5, 6, 7, 8, 9>
<5, 4, 3, 2, 1>
<-5, -4, -3, -2, -1>
<-5, -5, -5, -5, -5> <5, 5, 5, 5, 5>
<30, 30, 30, 30, 30>
<35, 35, 35, 35, 35>
"""

#---------------------------------------------------------------------------------------------


# (2).Adopt a base class and its subclass 

import collections


class Vector:
    """Represent a vector in a multidimensional space."""
    def __init__(self, d):
        if isinstance(d, int):
            self._coords = [0] * d
        else:                                  
            try: # we test if param is iterable
                self._coords = [val for val in d]
            except TypeError:
                raise TypeError('invalid parameter type')
    def __len__(self):
        # Return the dimension of the vector.
        return len(self._coords)
    def __getitem__(self, j):
        # Return jth coordinate of vector.
        return self._coords[j]
    def __setitem__(self, j, val):
        # Set jth coordinate of vector to given value.
        self._coords[j] = val
    def __add__(self, other):
        # Return sum of two vectors.
        if len(self) != len(other):          # relies on __len__ method
            raise ValueError('dimensions must agree')
        result = Vector(len(self))           # start with vector of zeros
        for j in range(len(self)):
            result[j] = self[j] + other[j]
        return result
    def __eq__(self, other):
        # Return True if vector has same coordinates as other.
        return self._coords == other._coords
    def __ne__(self, other):
        # Return True if vector differs from other.
        return not self == other             # rely on existing __eq__ definition
    def __str__(self):
        # Produce string representation of vector.
        return '<' + str(self._coords)[1:-1] + '>'  # adapt list representation
    def __neg__(self):
        # Return copy of vector with all coordinates negated.
        result = Vector(len(self))           # start with vector of zeros
        for j in range(len(self)):
            result[j] = -self[j]
        return result
    def __lt__(self, other):
        # Compare vectors based on lexicographical order.
        if len(self) != len(other):
            raise ValueError('dimensions must agree')
        return self._coords < other._coords
    def __le__(self, other):
        # Compare vectors based on lexicographical order.
        if len(self) != len(other):
            raise ValueError('dimensions must agree')
        return self._coords <= other._coords


class PredatoryVector(Vector):
    """d is a len of list or a list"""
    def __init__(self,d):
        super().__init__(d)
    def get_vector(self):
        return self._coords
    def __rmul__(self,d):
        try:
            mid = self.get_vector()
            for i in range(d-1):
                self+=mid
            return self
        except:
            print('your input is wrong')


if __name__=="__main__":
    p1=PredatoryVector((1,2,3))
    print('3*p1:',3*p1)


# Output:

"""
#2.13 3*p1: <3, 6, 9>
"""

##############################################################################################


# R2.14 Add __mul__() method with u*v: Implement the mul method for the Vector class
# of Section 2.3.3, sothat the expression u v returns a scalar that represents the
# dot product of the vectors. 


# (1).Adopt one base class and 4 consecutive subclasses


class Vector:
    """Represent a vector in a multidimensional space."""
    def __init__(self, d):
        if isinstance(d, int):
            self._coords = [0] * d
        else:                                  
            try: # we test if param is iterable
                self._coords = [val for val in d]
            except TypeError:
                raise TypeError('invalid parameter type')
    def __len__(self):
        # Return the dimension of the vector.
        return len(self._coords)
    def __getitem__(self, j):
        # Return jth coordinate of vector.
        return self._coords[j]
    def __setitem__(self, j, val):
        # Set jth coordinate of vector to given value.
        try:
            self._coords[j] = val
            return True
        except:
            print('Invalid input or index')
            return False
    def __add__(self, other):
        # Return sum of two vectors.
        if len(self) != len(other):          # relies on __len__ method
            raise ValueError('dimensions must agree')
        result = Vector(len(self))           # start with vector of zeros
        for j in range(len(self)):
            result[j] = self[j] + other[j]
        return result
    def __eq__(self, other):
        # Return True if vector has same coordinates as other.
        return self._coords == other._coords
    def __ne__(self, other):
        # Return True if vector differs from other.
        return not self == other             # rely on existing __eq__ definition
    def __str__(self):
        # Produce string representation of vector.
        return '<' + str(self._coords)[1:-1] + '>'  # adapt list representation
    def __sub__(self, other):
        if len(self) != len(other):
            raise ValueError('Dimensions must match')
        result = Vector(len(self))
        for j in range (len(self)):
            result[j] = self[j] - other[j]
        return result
    def __lt__(self, other):
        # Compare vectors based on lexicographical order.
        if len(self) != len(other):
            raise ValueError('dimensions must agree')
        return self._coords < other._coords
    def __le__(self, other):
        # Compare vectors based on lexicographical order.
        if len(self) != len(other):
            raise ValueError('dimensions must agree')
        return self._coords <= other._coords   


class VectorNeg(Vector):
    def __neg__(self):
        result = Vector(len(self))
        for i in range(len(self)):
            result[i] = -self[i]
        return result
            

class VectorMult(VectorNeg):
    def __mul__(self, value):
        result = Vector(len(self))
        for i in range(len(self)):
            result[i] = self[i]*value
        return result


class VectorRMult(VectorMult):
    def __rmul__(self, value):
        return (self * value)  # Treat it like vector*value instead of value*vector


class VectorWMult(VectorRMult):
    def __mul__(self, other):  # Overriding the original definition
        if type(other) == int or type(other) == float: 
            result = Vector(len(self))
            for i in range(len(self)):
                result[i] = self[i]*other
            return result                
        else:
            len(other)
            print(len(other), len(self))
            if len(other) != len(self):
                raise ValueError('Vector lengths do not match')
            sum = 0
            for i in range(len(self)):
                sum += self[i]*other[i]
            return sum


if __name__ == '__main__':       
    vv = VectorWMult      
    v1 = vv(5)
    v2 = vv(5)
    for i in range(5):
        v1[i] = 5
        v2[i] = i
    print(v1+v2)
    print(v1-v2)
    print(v2-v1)      
    print(-v1, v1)
    print(v1*6)
    print(7*v1)
    print(v1*v2)
    try:
        print (v1*vv(7))
    except Exception as e:
        print(e)
    print (v1*3.3)


# Output:

"""
<5, 6, 7, 8, 9>
<5, 4, 3, 2, 1>
<-5, -4, -3, -2, -1>
<-5, -5, -5, -5, -5> <5, 5, 5, 5, 5>
<30, 30, 30, 30, 30>
<35, 35, 35, 35, 35>
5 5
50
7 5
Vector lengths do not match
<16.5, 16.5, 16.5, 16.5, 16.5>
"""

#---------------------------------------------------------------------------------------------


# (2).Adopt one base class and its subclass 


import collections


class Vector:
    """Represent a vector in a multidimensional space."""
    def __init__(self, d):
        if isinstance(d, int):
            self._coords = [0] * d
        else:                                  
            try: # we test if param is iterable
                self._coords = [val for val in d]
            except TypeError:
                raise TypeError('invalid parameter type')
    def __len__(self):
        # Return the dimension of the vector.
        return len(self._coords)
    def __getitem__(self, j):
        # Return jth coordinate of vector.
        return self._coords[j]
    def __setitem__(self, j, val):
        # Set jth coordinate of vector to given value.
        self._coords[j] = val
    def __add__(self, other):
        # Return sum of two vectors.
        if len(self) != len(other):          # relies on __len__ method
            raise ValueError('dimensions must agree')
        result = Vector(len(self))           # start with vector of zeros
        for j in range(len(self)):
            result[j] = self[j] + other[j]
        return result
    def __eq__(self, other):
        # Return True if vector has same coordinates as other.
        return self._coords == other._coords
    def __ne__(self, other):
        # Return True if vector differs from other.
        return not self == other             # rely on existing __eq__ definition
    def __str__(self):
        # Produce string representation of vector.
        return '<' + str(self._coords)[1:-1] + '>'  # adapt list representation
    def __neg__(self):
        # Return copy of vector with all coordinates negated.
        result = Vector(len(self))           # start with vector of zeros
        for j in range(len(self)):
            result[j] = -self[j]
        return result
    def __lt__(self, other):
        # Compare vectors based on lexicographical order.
        if len(self) != len(other):
            raise ValueError('dimensions must agree')
        return self._coords < other._coords
    def __le__(self, other):
        # Compare vectors based on lexicographical order.
        if len(self) != len(other):
            raise ValueError('dimensions must agree')
        return self._coords <= other._coords


class PredatoryVector(Vector):
    """d is a len of list or a list"""
    def __init__(self,d):
        super().__init__(d)
    def get_vector(self):
        return self._coords
    def __mul__(self,d):
        if type(d)==int:
            try:
                mid = self.get_vector()
                for i in range(d-1):
                    self+=mid
                return self
            except:
                print('your input is wrong')
        else:
            try:
                result = PredatoryVector(len(d))
                for i in range(len(d)):
                    result[i]=self[i]*d[i]
                return result
            except:
                print('your input is wrong')
                raise TypeError


if __name__=="__main__":
    p1=PredatoryVector((1,2,3))
    p2=PredatoryVector([4,5,6])
    print('p1*p2:',p1*p2)


# Output:

"""
p1*p2: <4, 10, 18>
"""

##############################################################################################


# R2.15 The Vector class of Section 2.3.3 provides a constructor that takes an 
# integer d, and produces a d-dimensional vector with all coordinates equal to
# 0. Another convenient form for creating a new vector would be to send the
# constructor a parameter that is some iterable type representing a sequence
# of numbers, and to create a vector with dimension equal to the length of
# that sequence and coordinates equal to the sequence values. For example,
# Vector([4, 7, 5]) would produce a three-dimensional vector with coordi-
# nates <4, 7, 5>. Modify the constructor so that either of these forms is
# acceptable; that is, if a single integer is sent, it produces a vector of that
# dimension with all zeros, but if a sequence of numbers is provided, it pro-
# duces a vector with coordinates based on that sequence.


import collections


class Vector:
    """Represent a vector in a multidimensional space."""
    def __init__(self, d):
        if isinstance(d, int):
            self._coords = [0] * d
        else:                                  
            try: # we test if param is iterable
                self._coords = [val for val in d]
            except TypeError:
                raise TypeError('invalid parameter type')
    def __len__(self):
        # Return the dimension of the vector.
        return len(self._coords)
    def __getitem__(self, j):
        # Return jth coordinate of vector.
        return self._coords[j]
    def __setitem__(self, j, val):
        # Set jth coordinate of vector to given value.
        try:
            self._coords[j] = val
            return True
        except:
            print('Invalid input or index')
            return False
    def __add__(self, other):
        # Return sum of two vectors.
        if len(self) != len(other):          # relies on __len__ method
            raise ValueError('dimensions must agree')
        result = Vector(len(self))           # start with vector of zeros
        for j in range(len(self)):
            result[j] = self[j] + other[j]
        return result
    def __eq__(self, other):
        # Return True if vector has same coordinates as other.
        return self._coords == other._coords
    def __ne__(self, other):
        # Return True if vector differs from other.
        return not self == other             # rely on existing __eq__ definition
    def __str__(self):
        # Produce string representation of vector.
        return '<' + str(self._coords)[1:-1] + '>'  # adapt list representation
    def __sub__(self, other):
        if len(self) != len(other):
            raise ValueError('Dimensions must match')
        result = Vector(len(self))
        for j in range (len(self)):
            result[j] = self[j] - other[j]
        return result
    def __lt__(self, other):
        # Compare vectors based on lexicographical order.
        if len(self) != len(other):
            raise ValueError('dimensions must agree')
        return self._coords < other._coords
    def __le__(self, other):
        # Compare vectors based on lexicographical order.
        if len(self) != len(other):
            raise ValueError('dimensions must agree')
        return self._coords <= other._coords   


class VectorNeg(Vector):
    def __neg__(self):
        result = Vector(len(self))
        for i in range(len(self)):
            result[i] = -self[i]
        return result
            

class VectorMult(VectorNeg):
    def __mul__(self, value):
        result = Vector(len(self))
        for i in range(len(self)):
            result[i] = self[i]*value
        return result


class VectorRMult(VectorMult):
    def __rmul__(self, value):
        return (self * value)  # Treat it like vector*value instead of value*vector


class VectorWMult(VectorRMult):
    def __mul__(self, other): # Overriding the original definition
        if type(other) == int or type(other) == float: 
            result = Vector(len(self))
            for i in range(len(self)):
                result[i] = self[i]*other
            return result             
        else:
            len(other)
            print(len(other), len(self))
            if len(other) != len(self):
                raise ValueError('Vector lengths do not match')
            sum = 0
            for i in range(len(self)):
                sum += self[i]*other[i]
            return sum

class VectorSequence(VectorWMult):
    def __init__(self, param):  #Override the original constructor
        if isinstance(param, int):
            super().__init__(param)
        else:
            self._coords = param


if __name__ == '__main__':
    vv = VectorSequence   
    v1 = vv(5)
    v2 = vv(5)
    for i in range(5):
        v1[i] = 5
        v2[i] = i
    print(v1+v2)
    print(v1-v2)
    print(v2-v1)      
    print(-v1, v1)
    print(v1*6)
    print(7*v1)
    print(v1*v2)
    try:
        print(v1*vv(7))
    except Exception as e:
        print(e)
    print(v1*3.3)
    print(vv([1,2,3]), vv(3))


# Output:

"""
<5, 6, 7, 8, 9>
<5, 4, 3, 2, 1>
<-5, -4, -3, -2, -1>
<-5, -5, -5, -5, -5> <5, 5, 5, 5, 5>
<30, 30, 30, 30, 30>
<35, 35, 35, 35, 35>
5 5
50
7 5
Vector lengths do not match
<16.5, 16.5, 16.5, 16.5, 16.5>
<1, 2, 3> <0, 0, 0>
"""

##############################################################################################


# 2.16. Our Range class, from Section 2.3.5, relies on the formula max(0, 
# (stop − start + step − 1) // step) to compute the number of elements 
# in the range. It is not immediately evident why this formula provides the 
# correct calculation, even if assuming a positive step size. Justify this 
# formula, in your own words.

"""
ex. (0,10,1) -> max(0, 5)
ex. (0, 11, 1) -> max(0, (11//2)) -> (0, 5)
ex. (0, 1, 2) -> max(0, (2//2)) -> max(0,1)
ex. (0,0,1) -> max(0, 0) -> max(0, 0)
ex. (0, 1, -2) -> max(0, (-2//2)) -> max(0, -1)

The max(0, ...) is to account for cases where the step size means that
 the stop value is actually "further away" from the start value
 
Adding the (+ step -1) ensures that you include a step that has less than 
a full step size between itself and the stop value ex (the 6 in range(0, 7)).  
The -1 prevents it from adding an extra number to the iterator
"""

##############################################################################################


# R2.17 类继承图

"""
               Object
           /      |     \
       Horse    Goat    Pig
    /        \
 Racer   Equestrian
 
 
 
 example Class Diagrma
|-------------------------|
|Class: Horse             |
|-------------------------|
| Fields:                 |
| _height                 |
| _color                  |
|-------------------------|
| Behaviours:             |
| run()                   |
| jump()                  |
|-------------------------|
"""

##############################################################################################


# R2.18 Give a short fragment of Python code that uses the progression classes
# from Section 2.4.2 to find the 8 th value of a Fibonacci progression that
# starts with 2 and 2 as its first two values.


# (1).Fibonacci: F(0)=1，F(1)=1,F(n)=F(n-1)+F(n-2), of which n ≥ 2，n ∈ N*；


class Progression:
    """
    Iterator producing a generic progression. Default iterator produces the 
    whole numbers 0, 1, 2, ...
    """
    def __init__(self, start=0):
        # Initialize current to the first value of the progression.
        self._current = start
    def _advance(self):
        """
        Update self._current to a new value.
        This should be overridden by a subclass to customize progression.
        By convention, if current is set to None, this designates the
        end of a finite progression.
        """
        self._current += 1
    def __next__(self):
        # The convention to end a progression
        if self._current is None:    
            raise StopIteration()
        else:
            answer = self._current     # record current value to return
            self._advance()            # advance to prepare for next time
            return answer              # return the answer
    def __iter__(self):
        # By convention, an iterator must return itself as an iterator.
        return self                  
    def print_progression(self, n):
        # Print next n values of the progression.
        print(' '.join(str(next(self)) for j in range(n)))

        
class Fibonacci(Progression):
    def __init__(self, first=0, second=1):
        self._current = first 
        self._previous = second - first
    def __next__(self):
        answer = self._current
        self._current, self._previous = self._current+self._previous, self._current
        return answer
    def __getitem__(self, item):  # Note, not check against negative numbers
        current = self._current
        previous = self._previous
        for i in range(item+1):
            answer = next(self)
        self._current, self._previous = current, previous # Restore the original values
        return answer


if __name__ == '__main__':        
    p = Progression()
    p.print_progression(10)
    f = Fibonacci(2,2)
    for i in range (8):
        print(f'Value Number {i+1} is {f[i]}')
    f.print_progression(8)


# Output:

"""
0 1 2 3 4 5 6 7 8 9
Value Number 1 is 2
Value Number 2 is 2
Value Number 3 is 4
Value Number 4 is 6
Value Number 5 is 10
Value Number 6 is 16
Value Number 7 is 26
Value Number 8 is 42
2 2 4 6 10 16 26 42
"""

#---------------------------------------------------------------------------------------------


# (2).Fibonacci: F(0)=1，F(1)=1,F(n)=F(n-1)+F(n-2)


class Progression(object):
    """
    Iterator producing a generic progression. Default iterator produces the 
    whole numbers 0, 1, 2, ...
    """
    def __init__(self, start=0):
        # Initialize current to the first value of the progression.
        self._current = start
    def _advance(self):
        """
        Update self._current to a new value.
        This should be overridden by a subclass to customize progression.
        By convention, if current is set to None, this designates the
        end of a finite progression.
        """
        self._current += 1
    def __next__(self):
        # The convention to end a progression
        if self._current is None:    
            raise StopIteration()
        else:
            answer = self._current     # record current value to return
            self._advance()            # advance to prepare for next time
            return answer              # return the answer
    def __iter__(self):
        # By convention, an iterator must return itself as an iterator.
        return self                  
    def print_progression(self, n):
        # Print next n values of the progression.
        print(' '.join(str(next(self)) for j in range(n)))


class Fibonacci(Progression):
    def __init__(self, start=0, second=1):
        super(Fibonacci, self).__init__(start)        
        self._previous = second - start
    def __next__(self):
        answer = self._current
        self._current, self._previous = self._current+self._previous, self._current
        return answer
    def __getitem__(self, item):  # Note, not check against negative numbers
        current = self._current
        previous = self._previous
        for i in range(item+1):
            answer = next(self)
        self._current, self._previous = current, previous # Restore the original values
        return answer


if __name__ == '__main__':        
    p = Progression()
    p.print_progression(10)
    f = Fibonacci(2,2)
    for i in range (8):
        print (f'Value Number {i+1} is {f[i]}')
    f.print_progression(8)


# Output:

"""
0 1 2 3 4 5 6 7 8 9
Value Number 1 is 2
Value Number 2 is 2
Value Number 3 is 4
Value Number 4 is 6
Value Number 5 is 10
Value Number 6 is 16
Value Number 7 is 26
Value Number 8 is 42
2 2 4 6 10 16 26 42
"""

#---------------------------------------------------------------------------------------------


# (3). Adopt Progresion calss and its Fibonacci subclass/  


class Progression:
    """
    Iterator producing a generic progression. Default iterator produces the 
    whole numbers 0, 1, 2, ...
    """
    def __init__(self, start=0):
        # Initialize current to the first value of the progression.
        self._current = start
    def _advance(self):
        """
        Update self._current to a new value.
        This should be overridden by a subclass to customize progression.
        By convention, if current is set to None, this designates the
        end of a finite progression.
        """
        self._current += 1
    def __next__(self):
        # The convention to end a progression
        if self._current is None:    
            raise StopIteration()
        else:
            answer = self._current     # record current value to return
            self._advance()            # advance to prepare for next time
            return answer              # return the answer
    def __iter__(self):
        # By convention, an iterator must return itself as an iterator.
        return self                  
    def print_progression(self, n):
        # Print next n values of the progression.
        print(' '.join(str(next(self)) for j in range(n)))


class Fibonacci(Progression):
    def __init__(self, start=0, second=1):
        self._previous = second - start
        super().__init__(start)  
    def __next__(self):
        answer = self._current
        self._current, self._previous = self._current+self._previous, self._current
        return answer
    def __getitem__(self, item):  # Note, not check against negative numbers
        current = self._current
        previous = self._previous
        for i in range(item+1):
            answer = next(self)
        self._current, self._previous = current, previous # Restore the original values
        return answer


if __name__ == '__main__':        
    p = Progression()
    p.print_progression(10)
    f = Fibonacci(2,2)
    for i in range (8):
        print(f'Value Number {i+1} is {f[i]}')
    f.print_progression(8)

# Output:

"""
0 1 2 3 4 5 6 7 8 9
Value Number 1 is 2
Value Number 2 is 2
Value Number 3 is 4
Value Number 4 is 6
Value Number 5 is 10
Value Number 6 is 16
Value Number 7 is 26
Value Number 8 is 42
2 2 4 6 10 16 26 42
"""

##############################################################################################


# R2.19. When using the ArithmeticProgression class of Section 2.4.2 with 
# an increment of 128 and a start of 0, how many calls to next can we make
# before we reach an integer of 2 63 or larger?


# ArithmeticProgression with 2^63 / 2^7


class Progression:
    """
    Iterator producing a generic progression. Default iterator produces the 
    whole numbers 0, 1, 2, ...
    """
    def __init__(self, start=0):
        # Initialize current to the first value of the progression.
        self._current = start
    def _advance(self):
        """
        Update self._current to a new value.
        This should be overridden by a subclass to customize progression.
        By convention, if current is set to None, this designates the
        end of a finite progression.
        """
        self._current += 1
    def __next__(self):
        # The convention to end a progression
        if self._current is None:    
            raise StopIteration()
        else:
            answer = self._current     # record current value to return
            self._advance()            # advance to prepare for next time
            return answer              # return the answer
    def __iter__(self):
        # By convention, an iterator must return itself as an iterator.
        return self                  
    def print_progression(self, n):
        # Print next n values of the progression.
        print(' '.join(str(next(self)) for j in range(n)))


class ArithmeticProgression(Progression): 
    """Iterator produces an arithmetic progression."""
    def __init__(self, start=0, step=1):
        """
        Create a new arithmetic progression.
        increment  the fixed constant to add to each term (default 1)
        start      the first term of the progression (default 0)
        """
        super().__init__(start)       # initialize base class
        self._step = step
    """
    def _advance(self):               # override inherited version
        # Update current value by adding the fixed increment.
        self._current += self._increment
    """
    def __next__(self):
        answer = self._current
        self._current = self._current + self._step
        return answer
    def __getitem__(self, index):
        current = self._current
        for i in range(index + 1):
            answer = next(self)
        self._current = current
        return (answer)


# It takes a quite longer running time to use goal = 2**63

if __name__ == '__main__':
    p = Progression()
    p.print_progression(10)
    a = ArithmeticProgression(1,1)
    for i in range(8):
        print(f'Value Number {i+1} is {a[i]}')
    a.print_progression(8)
    b = ArithmeticProgression(0, 128)
    i = 0
    goal = 2**63
    value = 0
    while value < goal:
        i+=1
        value = next(b)
    print(f'It requires {i-1} iterations to get to 2**63')


# Output:

"""
0 1 2 3 4 5 6 7 8 9
Value Number 1 is 1
Value Number 2 is 2
Value Number 3 is 3
Value Number 4 is 4
Value Number 5 is 5
Value Number 6 is 6
Value Number 7 is 7
Value Number 8 is 8
1 2 3 4 5 6 7 8
........
"""

##############################################################################################


# R2.20. What are some potential efficiency disadvantages of having very deep in-
# heritance trees, that is, a large set of classes, A, B, C, and so on, such that
# B extends A, C extends B, D extends C, etc.?


# Very Deep Tree I nheritance 

"""
If behaviour changes in A without D knowing (ex. different teams or people working on it), 
it can be very difficult to troubleshoot the problems


You also have a larger chance of namespace conflicts that you aren't aware of 
(ex. C overrides a function from B that you don't know about)
"""

##############################################################################################


# R.21 Modify R2.14

"""
If any of the classes change, it will mess up the entire Z subclass
Namespace conflicts are probable more difficult to resolve??  Not sure about that one
"""

##############################################################################################


# R2.22 The collections.Sequence abstract base class does not provide support 
# for comparing two sequences to each other. Modify our Sequence class from
# Code Fragment 2.14 to include a definition for the eq method, so that expression 
# seq1 == seq2 will return True precisely when the two sequences are element by 
# element equivalent.


# Add a subclass - CompareSequence


# collections.abc is deprecated 
# from collections.abc import ABCMeta, abstractmethod 
from abc import ABCMeta, abstractmethod            


class Sequence(metaclass=ABCMeta):
    """Our own version of collections.Sequence abstract base class."""
    @abstractmethod
    def __len__(self):
        # Return the length of the sequence.
        pass
    @abstractmethod
    def __getitem__(self, j):
        # Return the element at index j of the sequence.
        pass
    def __contains__(self, val):
        # Return True if val found in the sequence; False otherwise.
        for j in range(len(self)):
            if self[j] == val:                        # found match
                return True
        return False
    def index(self, val):
        # Return leftmost index at which val is found (or raise ValueError).
        for j in range(len(self)):
            if self[j] == val:                        # leftmost match
                return j
        raise ValueError('value not in sequence')     # never found a match
    def count(self, val):
        # Return the number of elements equal to given value.
        k = 0
        for j in range(len(self)):
            if self[j] == val:                        # found a match
                k += 1
        return k


class CompareSequence(Sequence):
    def __init__(self, arm):
        self._arm = arm
    def __len__(self):
        len(self._arm)
    def __getitem__(self,val):
        return arm[val-1]
    def __eq__(self,other):
        if self._arm == other._arm:
            return True
        else:
            return False
    def __lt__(self,other):
        if len(self) > len(other):
            return True
        else:
            return False


if __name__=="__main__":
    cs1 = CompareSequence('1,2,3')
    cs2 = CompareSequence('1,3,3')
    print("Compare the length of the two dicts")
    print(cs1==cs2)


# Output:

"""
Compare the length of the two dicts
False
"""

##############################################################################################


# R2.23 In similar spirit to the previous problem, augment the Sequence class with
# method lt , to support lexicographic comparison seq1 < seq2.

# Please see the above R2.22

##############################################################################################
##############################################################################################


# Part Two. Creativity

##############################################################################################


# C2.24 Suppose you are on the design team for a new e-book reader. What are 
# the primary classes and methods that the Python software for your reader will
# need? You should include an inheritance diagram for this code, but you
# do not need to write any actual code. Your software architecture should
# at least include ways for customers to buy new books, view their list of
# purchased books, and read their purchased books. 

# EBook classes and methods (P2.38 Write an ebook program)


"""
Methods:
purchase_books()
view_purchased()
read_purchased()


Class Hierarchy:
E-book Class -> Class for a specific model (Different models may have different features)
Book Class (Nested or not)
"""

##############################################################################################


# C2.25. Exercise R-2.12 uses the mul method to support multiplying a Vector
# by a number, while Exercise R-2.14 uses the mul method to support
# computing a dot product of two vectors. Give a single implementation of
# Vector. mul that uses run-time type checking to support both syntaxes
# u v and u k, where u and v designate vector instances and k represents
# a number.


# Realize u*v and k*u, u and v are vectors and k is scalar

# Please take R2.12 and R2.14 for reference


##############################################################################################


# C2.26. The SequenceIterator class of Section 2.3.4 provides what is known as a
# forward iterator. Implement a class named ReversedSequenceIterator that
# serves as a reverse iterator for any Python sequence type. The first call to
# next should return the last element of the sequence, the second call to next
# should return the second-to-last element, and so forth.


# (1).With adopt super() to inherit: Realize a reverser sequence iterator


class SequenceIterator:
    """An iterator for any of Python's sequence types."""
    def __init__(self, sequence):
        # Create an iterator for the given sequence.
        self._seq = sequence            # keep a reference to the underlying data
        self._k = -1                    # will increment to 0 on first call to next
    def __next__(self):
        # Return the next element, or else raise StopIteration error.
        self._k += 1                    # advance to next index
        if self._k < len(self._seq):
            return(self._seq[self._k])  # return the data element
        else:
            raise StopIteration()       # there are no more elements
    def __iter__(self):
        # By convention, an iterator must return itself as an iterator.
        return self


class ReverseSequenceIterator(SequenceIterator):
    def __init__(self, sequence):
        super().__init__(sequence)
        self._k = len(sequence)
    def __next__(self):
        self._k -= 1
        if self._k >=0:
            return self._seq[self._k]
        else:
            raise StopIteration()
    def __iter__(self):
        return self


if __name__ == '__main__':
    s = ReverseSequenceIterator([1,2,3,4,5, 6, 7, 8])
    print([x for x in ReverseSequenceIterator([1,2,3,4,5, 6, 7, 8])])
    print([x for x in ReverseSequenceIterator([1,2,'d',4,56, 7, 8])])


# Output:

"""
[8, 7, 6, 5, 4, 3, 2, 1]
[8, 7, 56, 4, 'd', 2, 1]
"""

#---------------------------------------------------------------------------------------------


# (2).No super() function
    

class ReverseSequenceIterator():
    def __init__(self, sequence):
        self._seq = sequence
        self._k = len(sequence)
    def __next__(self):
        self._k -= 1
        if self._k >=0:
            return self._seq[self._k]
        else:
            raise StopIteration()   
    def __iter__(self):
        return self


if __name__ == '__main__':
    s = ReverseSequenceIterator([1,2,3,4,5, 6, 7, 8])
    print([x for x in ReverseSequenceIterator([1,2,3,4,5, 6, 7, 8])])
    print([x for x in ReverseSequenceIterator([1,2,'d',4,56, 7, 8])])


# Output:

"""
[8, 7, 6, 5, 4, 3, 2, 1]
[8, 7, 56, 4, 'd', 2, 1]
"""

##############################################################################################


# C2.27. In Section 2.3.5, we note that our version of the Range class has im-
# plicit support for iteration, due to its explicit support of both len
# and getitem . The class also receives implicit support of the Boolean
# test, “k in r” for Range r. This test is evaluated based on a forward itera-
# tion through the range, as evidenced by the relative quickness of the test
# 2 in Range(10000000) versus 9999999 in Range(10000000). Provide a
# more efficient implementation of the contains method to determine
# whether a particular value lies within a given range. The running time of
# your method should be independent of the length of the range.


# (1).Add the method of __contains__()


class Range:
    def __init__(self, start, stop=None, step=1):
        if step == 0: 
            raise ValueError('step cannot be 0')
        if stop is None:    # This is more robust than if stop == None
            start, stop = 0, start
        self._length = max(0, (stop - start + step -1)//step)
        self._start = start
        self._step = step
    def __len__(self):
        return self._length
    def __getitem__(self, k):
        if k < 0:
            k += len(self)
        if not 0 <= k < self._length:
            raise IndexError('index out of range')
        return self._start + k*self._step
    def __contains__(self, value):
        # The number will be in the sequence if (value - start)% step == 0
        factor, remainder = divmod((value - self._start), self._step)
        if remainder == 0:    #It is a part of the infinite range in either directiom
            # Now we just need to check if it's within the defined range...
            if factor < len(self) and factor >=0: 
                return True
            else: 
                return False
        else:
            return False


if __name__ == '__main__':         
    r = Range(1,100,2)
    print(len(r), r[3], 4 in r, 5 in r)
    r = Range(-100, step = -1)
    print(len(r), r[3], 4 in r, 5 in r)


# Output:

"""
50 7 False True
102 -3 False False
"""

#---------------------------------------------------------------------------------------------


# (2).Use super() to construct subclass


class Range:
    """A class that mimic's the built-in range class."""
    def __init__(self, start, stop=None, step=1):
        """
        Initialize a Range instance.
        Semantics is similar to built-in range class.
        """
        if step == 0:
            raise ValueError('step cannot be 0')
        if stop is None:                    # special case of range(n)
            start, stop = 0, start          # should be treated as if range(0,n)
        # Calculate the effective length once
        self._length = max(0, (stop - start + step - 1) // step)
        # Need knowledge of start and step to support __getitem__()
        self._start = start
        self._step = step
    def __len__(self):
        # Return number of entries in the range.
        return self._length
    def __getitem__(self, k):
        # Return entry at index k (using standard interpretation if negative).
        if k < 0:
            k += len(self)                  # attempt to convert negative index
        if not 0 <= k < self._length:
            raise IndexError('index out of range')
        return self._start + k * self._step


class SubRange(Range): 
    def __init__(self, start, stop=None, step=1):
        super().__init__(start, stop, step)
    def __len__(self, k):
        super().__len__(k)
    def __getitem__(self, k):
        super().__getitem__(k)
    def __contains__(self, value):
        # The number will be in the sequence if (value - start)% step == 0
        factor, remainder = divmod((value - self._start), self._step)
        if remainder == 0:    #It is a part of the infinite range in either directiom
            #Now we just need to check if it's within the defined range...
            if factor < len(self) and factor >=0: 
                return True
            else: 
                return False
        else:
            return False


if __name__ == '__main__':         
    r = Range(1,100,2)
    print (len(r), r[3], 4 in r, 5 in r)
    r = Range(-100, step = -1)
    print (len(r), r[3], 4 in r, 5 in r)


# Output:

"""
50 7 False True
102 -3 False False
"""

##############################################################################################


# C2.28  The PredatoryCreditCard class of Section 2.4.1 provides a process 
# month method that models the completion of a monthly cycle. Modify the class
# so that once a customer has made ten calls to charge in the current month,
# each additional call to that function results in an additional $1 surcharge.


# (1).Modify Predatory class to keep 10 free calls and charges fees on additional calls


class CreditCard:
    """A consumer credit card."""
    def __init__(self, customer, bank, acnt, limit):
        """
        Create a new credit card instance.
        The initial balance is zero.
        customer  the name of the customer (e.g., 'John Bowman')
        bank      the name of the bank (e.g., 'California Savings')
        acnt      the acount identifier (e.g., '5391 0375 9387 5309')
        limit     credit limit (measured in dollars)
        """
        self._customer = customer
        self._bank = bank
        self._account = acnt
        self._limit = limit
        self._balance = 0
    def get_customer(self):
        # Return name of the customer.
        return self._customer
    def get_bank(self):
        # Return the bank's name.
        return self._bank
    def get_account(self):
        # Return the card identifying number (typically stored as a string).
        return self._account
    def get_limit(self):
        # Return current credit limit.
        return self._limit
    def get_balance(self):
        # Return current balance.
        return self._balance
    def charge(self, price):
        # Charge given price to the card, assuming sufficient credit limit.
        # Return True if charge was processed; False if charge was denied.
        if price + self._balance > self._limit:  # if charge would exceed limit,
            return False                         # cannot accept charge
        else:
            self._balance += price
            return True
    def make_payment(self, amount):
        # Process customer payment that reduces balance.
        self._balance -= amount


class PredatoryCreditCard(CreditCard):
    """An extension to CreditCard that compounds interest and fees."""
    def __init__(self, customer, bank, acnt, limit, apr):
        """
        Create a new predatory credit card instance.
        The initial balance is zero.
        customer  the name of the customer (e.g., 'John Bowman')
        bank      the name of the bank (e.g., 'California Savings')
        acnt      the acount identifier (e.g., '5391 0375 9387 5309')
        limit     credit limit (measured in dollars)
        apr       annual percentage rate (e.g., 0.0825 for 8.25% APR)
        """
        super().__init__(customer, bank, acnt, limit)  # call super constructor
        self._apr = apr
        self._num_charges = 0
    def charge(self, price):
        """
        Charge given price to the card, assuming sufficient credit limit.
        Return True if charge was processed.
        Return False and assess $5 fee if charge is denied.
        """
        success = super().charge(price)          # call inherited method
        if not success:
            self._balance += 5                   # assess penalty
        else:
            self._num_charges += 1
            if self._num_charges > 10:
                self._balance += 1
        return success                           # caller expects return value
    def process_month(self):
        # Assess monthly interest on outstanding balance.
        if self._balance > 0:
            # if positive balance, convert APR to monthly multiplicative factor
            monthly_factor = pow(1 + self._apr, 1/12)
            self._balance *= monthly_factor
            self._num_charges = 0


if __name__ == '__main__':
    wallet = []
    wallet.append(PredatoryCreditCard('John Bowman', 'California Savings',
                           '5391 0375 9387 5309', 2500, 0.15))
    wallet.append(PredatoryCreditCard('John Bowman', 'California Federal',
                           '3485 0399 3395 1954', 3500, 0.15))
    wallet.append(PredatoryCreditCard('John Bowman', 'California Finance',
                           '5391 0375 9387 5309', 5000, 0.30))   
    for val in range(1, 100):
        wallet[0].charge(val)
        wallet[1].charge(2*val)
        wallet[2].charge(3*val)
    for c in range(3):
        print('Customer =', wallet[c].get_customer())
        print('Bank =',     wallet[c].get_bank())
        print('Account =',  wallet[c].get_account())
        print('Limit =',    wallet[c].get_limit())
        print('Balance =',   wallet[c].get_balance())
        while wallet[c].get_balance() > 100:
            wallet[c].make_payment(100)
            print('New balance =', wallet[c].get_balance())
    print()


#---------------------------------------------------------------------------------------------


# (2).Modify Predatory class 

# keep 10 free calls and charges fees on additional calls based on R2.5

class CreditCard:
    """A consumer credit card."""
    def __init__(self, customer, bank, acnt, limit):
        """
        Create a new credit card instance.
        The initial balance is zero.
        customer  the name of the customer (e.g., 'John Bowman')
        bank      the name of the bank (e.g., 'California Savings')
        acnt      the acount identifier (e.g., '5391 0375 9387 5309')
        limit     credit limit (measured in dollars)
        """
        self._customer = customer
        self._bank = bank
        self._account = acnt
        self._limit = limit
        self._balance = 0
    def get_customer(self):
        # Return name of the customer.
        return self._customer
    def get_bank(self):
        # Return the bank's name.
        return self._bank
    def get_account(self):
        # Return the card identifying number (typically stored as a string).
        return self._account
    def get_limit(self):
        # Return current credit limit.
        return self._limit
    def get_balance(self):
        # Return current balance.
        return self._balance
    def charge(self, price):
        # Charge given price to the card, assuming sufficient credit limit.
        try:
            price = float(price)
        except:
            print('Invalid input')
        # Return True if charge was processed; False if charge was denied.
        if price + self._balance > self._limit:  # if charge would exceed limit,
            print(f'Your deposit of {price} exceeds your remainder of {self.get_limit()-self.get_balance()}')
            return False                         # cannot accept charge
        else:
            self._balance += price
            return True
    def make_payment(self, amount):
        # Process customer payment that reduces balance."""
        try:
            amount = float(amount)
        except:
            print('Invalid input')
        self._balance -= amount
        return True


class PredatoryCreditCard(CreditCard):
    """An extension to CreditCard that compounds interest and fees."""
    def __init__(self, customer, bank, acnt, limit, apr):
        """
        Create a new predatory credit card instance.
        The initial balance is zero.
        customer  the name of the customer (e.g., 'John Bowman')
        bank      the name of the bank (e.g., 'California Savings')
        acnt      the acount identifier (e.g., '5391 0375 9387 5309')
        limit     credit limit (measured in dollars)
        apr       annual percentage rate (e.g., 0.0825 for 8.25% APR)
        """
        super().__init__(customer, bank, acnt, limit)  # call super constructor
        self._apr = apr
        self._num_charges = 0
    def charge(self, price):
        """
        Charge given price to the card, assuming sufficient credit limit.
        Return True if charge was processed.
        Return False and assess $5 fee if charge is denied.
        """
        success = super().charge(price)          # call inherited method
        if not success:
            self._balance += 5                   # assess penalty
        else:
            self._num_charges += 1
            if self._num_charges > 10:
                self._balance += 1
        return success                           # caller expects return value
    def process_month(self):
        # Assess monthly interest on outstanding balance.
        if self._balance > 0:
            # if positive balance, convert APR to monthly multiplicative factor
            monthly_factor = pow(1 + self._apr, 1/12)
            self._balance *= monthly_factor
            self._num_charges = 0

 
if __name__ == '__main__':
    wallet = []
    wallet.append(PredatoryCreditCard('John Bowman', 'California Savings',
                           '5391 0375 9387 5309', 2500, 0.15))
    wallet.append(PredatoryCreditCard('John Bowman', 'California Federal',
                           '3485 0399 3395 1954', 3500, 0.15))
    wallet.append(PredatoryCreditCard('John Bowman', 'California Finance',
                           '5391 0375 9387 5309', 5000, 0.30))   
    for val in range(1, 100):
        wallet[0].charge(val)
        wallet[1].charge(2*val)
        wallet[2].charge(3*val)
    for c in range(3):
        print('Customer =', wallet[c].get_customer())
        print('Bank =',     wallet[c].get_bank())
        print('Account =',  wallet[c].get_account())
        print('Limit =',    wallet[c].get_limit())
        print('Balance =',   wallet[c].get_balance())
        while wallet[c].get_balance() > 100:
            wallet[c].make_payment(100)
            print('New balance =', wallet[c].get_balance())
    print()


# Output:

"""
...
True
Your deposit of 171.0 exceeds your remainder of 166.0
False
True
True
Your deposit of 174.0 exceeds your remainder of 161.0
False
True
Your deposit of 118.0 exceeds your remainder of 30.0
False
Your deposit of 177.0 exceeds your remainder of 156.0
False
True
Your deposit of 120.0 exceeds your remainder of 25.0
False
...
"""

##############################################################################################


# C2.29 Modify the PredatoryCreditCard class from Section 2.4.1 so that a customer 
# is assigned a minimum monthly payment, as a percentage of the balance, and so that 
# a late fee is assessed if the customer does not subse-quently pay that minimum 
# amount before the next monthly cycle.


# (1).Give a minimum payment, otherwise appriase delayed fees


class CreditCard:
    """A consumer credit card."""
    def __init__(self, customer, bank, acnt, limit):
        """
        Create a new credit card instance.
        The initial balance is zero.
        customer  the name of the customer (e.g., 'John Bowman')
        bank      the name of the bank (e.g., 'California Savings')
        acnt      the acount identifier (e.g., '5391 0375 9387 5309')
        limit     credit limit (measured in dollars)
        """
        self._customer = customer
        self._bank = bank
        self._account = acnt
        self._limit = limit
        self._balance = 0
    def get_customer(self):
        # Return name of the customer.
        return self._customer
    def get_bank(self):
        # Return the bank's name.
        return self._bank
    def get_account(self):
        # Return the card identifying number (typically stored as a string).
        return self._account
    def get_limit(self):
        # Return current credit limit.
        return self._limit
    def get_balance(self):
        # Return current balance(透支额)
        return self._balance
    def charge(self, price):
        # Charge given price to the card, assuming sufficient credit limit.
        # Return True if charge was processed; False if charge was denied.
        if price + self._balance > self._limit:  # if charge would exceed limit,
            return False                         # cannot accept charge
        else:
            self._balance += price
            return True
    def make_payment(self, amount):
        # Process customer payment that reduces balance.
        self._balance -= amount


class PredatoryCreditCard(CreditCard):
    MAX_CHARGES = 10
    def __init__(self, customer, bank, acnt, limit, apr):
        super().__init__(customer, bank, acnt, limit)
        self._apr = apr
        self._num_charges = 0
    def charge(self, price):
        success = super().charge(price)
        if not success:
            self._balance += 5
        else:
            self._num_charges += 1
            if self._num_charges > self.MAX_CHARGES:
                self._balance+=1
        return success
    def process_month(self):
        if self._balance > 0:
            monthly_factor = pow(1+self._apr, 1/12)
            self._balance *= monthly_factor
        self._num_charges = 0 # reset the counter at the beginning of each month


class PCCMonthly(PredatoryCreditCard):
    MIN_PCT = 0.1
    LATE_FEE = 10
    def __init__(self, customer, bank, acnt, limit, apr):
        super().__init__(customer, bank, acnt, limit, apr)
        self._min_payment = 0
    def process_month(self):
        super().process_month()
        if self._min_payment > 0:
            self._balance += self.LATE_FEE
        if self._balance > 0:
            self._min_payment = self._balance * self.MIN_PCT
    """
    def make_payment(self, amount):
        super().make_payment(amount)
        self._min_payment = max(0, self._min_payment - amount)
    """
    def make_payment(self, amount):
        if super().make_payment(amount): # amount为实际还款
            self._min_payment = max(0, self._min_payment - amount)


if __name__ == '__main__':
    cc1 = PCCMonthly('John Bowman' , 'California Savings' ,'56 5391 0375 9387 5309' , 2500, 0.15)
    cc1.charge(100)
    cc1.charge(200)
    cc1.process_month()
    print(cc1.get_balance(), cc1._min_payment)
    cc1.process_month()
    print(cc1.get_balance(), cc1._min_payment)


# Output:

"""
True
True
303.514475075956 30.3514475075956
317.07012193544375 31.707012193544376
"""

#---------------------------------------------------------------------------------------------


# (2).Build a subclass PCCMonthly 


class PCCMonthly(PredatoryCreditCard):
    MIN_PCT = 0.05
    LATE_FEE = 10
    def __init__(self, customer, bank, acnt, limit, apr):
        super().__init__(customer, bank, acnt, limit, apr)
        self._min_payment = 0
    def process_month(self, amount):
        super().process_month()
        if self._min_payment > 0:
            self._balance += self.LATE_FEE
        if self._balance > 0:
            self._min_payment = (self._balance - amount) * self.MIN_PCT
    """
    def make_payment(self, amount):
        super().make_payment(amount)
        self._min_payment = max(0, self._min_payment - amount)
    """
    def make_payment(self, amount):
        if super().make_payment(amount): # amount为实际还款
            self._min_payment = max(0, self._min_payment - amount)


if __name__ == '__main__':
    cc1 = PCCMonthly('John Bowman' , 'California Savings' ,'56 5391 0375 9387 5309' , 2500, 0.15)
    cc1.charge(100)
    cc1.charge(200)
    cc1.process_month(80)
    print(cc1.get_balance(), cc1._min_payment)
    cc1.process_month(90)
    print(cc1.get_balance(), cc1._min_payment)


# Output:

"""
True
True
303.514475075956 11.1757237537978
317.07012193544375 11.353506096772188
"""

#---------------------------------------------------------------------------------------------


# (3).Add concecutive subclass. 


class CreditCard:
    """A consumer credit card."""
    def __init__(self, customer, bank, acnt, limit):
        """
        Create a new credit card instance.
        The initial balance is zero.
        customer  the name of the customer (e.g., 'John Bowman')
        bank      the name of the bank (e.g., 'California Savings')
        acnt      the acount identifier (e.g., '5391 0375 9387 5309')
        limit     credit limit (measured in dollars)
        """
        self._customer = customer
        self._bank = bank
        self._account = acnt
        self._limit = limit
        self._balance = 0
    def get_customer(self):
        # Return name of the customer.
        return self._customer
    def get_bank(self):
        # Return the bank's name.
        return self._bank
    def get_account(self):
        # Return the card identifying number (typically stored as a string).
        return self._account
    def get_limit(self):
        # Return current credit limit.
        return self._limit
    def get_balance(self):
        # Return current balance.
        return self._balance
    def charge(self, price):
        # Charge given price to the card, assuming sufficient credit limit.
        # Return True if charge was processed; False if charge was denied.
        if price + self._balance > self._limit:  # if charge would exceed limit,
            return False                         # cannot accept charge
        else:
            self._balance += price
            return True
    def make_payment(self, amount):
        # Process customer payment that reduces balance.
        self._balance -= amount


class PredatoryCreditCard(CreditCard):
    MAX_CHARGES = 10
    def __init__(self, customer, bank, acnt, limit, apr):
        super().__init__(customer, bank, acnt, limit)
        self._apr = apr
        self._num_charges = 0
    def charge(self, price):
        success = super().charge(price)
        if not success:
            self._balance += 5
        else:
            self._num_charges += 1
            if self._num_charges > self.MAX_CHARGES:
                self._balance+=1
        return success
    def process_month(self):
        if self._balance > 0:
            monthly_factor = pow(1+self._apr, 1/12)
            self._balance *= monthly_factor
        self._num_charges = 0 # reset the counter at the beginning of each month


class PCCMonthly(PredatoryCreditCard):
    MIN_PCT = 0.1
    LATE_FEE = 10
    DUE_DATES = 30
    def __init__(self, customer, bank, acnt, limit, apr):
        super().__init__(customer, bank, acnt, limit, apr)
        self._min_payment = 0
    def process_month(self):
        super().process_month()
        if self._min_payment > 0:
            self._balance += self.LATE_FEE
        if self._balance > 0:
            self._min_payment = self._balance * self.MIN_PCT
    def make_payment(self, amount):
        if super().make_payment(amount): 
            if self._min_payment - amount > 0:
                self._balance = self._balance + self.balance * 0.0005 * self.DUE_DATES


if __name__ == '__main__':
    cc1 = PCCMonthly('John Bowman' , 'California Savings' ,'56 5391 0375 9387 5309' , 2500, 0.15)
    cc1.charge(100)
    cc1.charge(200)
    cc1.process_month()
    print(cc1.get_balance(), cc1._min_payment)
    cc1.process_month()
    print(cc1.get_balance(), cc1._min_payment)
    print(cc1.make_payment(300))


# Output:

"""
True
True
303.514475075956 30.3514475075956
317.07012193544375 31.707012193544376
None
"""

##############################################################################################


# C2.30. At the close of Section 2.4.1, we suggest a model in which the CreditCard
# class supports a nonpublic method, set balance(b), that could be used
# by subclasses to affect a change to the balance, without directly accessing
# the balance data member. Implement such a model, revising both the
# CreditCard and PredatoryCreditCard classes accordingly.


# (1).Add the method of _set_balance_() to inrectly access to _balance


class Descriptor(object):
    def __init__(self, name =''):
        self.name = name
    def __get__(self, obj, objtype):
        return "{}for{}".format(self.name, self.name)
    def __set__(self, obj, name): # obj.attr = ''value'
        if isinstance(name, str):
            self.name = name
        else:
            raise TypeError("Name should be string")

        
class GFG(object):
    name = Descriptor()


if __name__ == '__main__':    
    g = GFG()
    g.name = "GreeceforGreece"
    print(g.name)


# Outout:

"""
GreeceforGreeceforGreeceforGreece
"""

#-------------------------------------------------------------------------------------------------


# (2).Add Descriptor class 


class Descriptor(object):
    def __init__(self, name =''):
        self.name = name
    def __get__(self, obj, objtype):
        return "{}for{}".format(self.name, self.name)
    def __set__(self, obj, name):
        if isinstance(name, str):
            self.name = name
        else:
            raise TypeError("Name should be string")

        
class GFG(object):
    name = Descriptor()


if __name__ == '__main__':    
    g = GFG()
    g.name = "Geeks"
    print(g.name)

#-------------------------------------------------------------------------------------------------


# (3).property_function.py


class Verbose_attribute():
    def __get__(self, obj, type=None) -> object:
        print("accessing the attribute to get the value")
        return 42
    def __set__(self, obj, value) -> None:
        print("accessing the attribute to set the value")
        raise AttributeError("Cannot change the value")


class Foo():
    attribute1 = Verbose_attribute()


if __name__ == '__main__':
    my_foo_object = Foo()
    x = my_foo_object.attribute1
    print(x)


# Output:

"""
accessing the attribute to get the value
42
"""


# or the following equivalence


class Foo:
    def getter(self) -> object:
        print("accessing the attribute to get the value")
        return 42
    def setter(self, value) -> None:
        print("accessing the attribute to set the value")
        raise AttributeError("Cannot change the value")
    attribute1 = property(getter, setter)



if __name__ == '__main__':
    my_foo_object = Foo()
    x = my_foo_object.attribute1
    print(x)


# Output:

"""
accessing the attribute to get the value
42
"""

#-------------------------------------------------------------------------------------------------


# (4).descriptors2.py


class OneDigitNumericValue():
    def __init__(self):
        self.value = 0
    def __get__(self, obj, type=None) -> object:
        return self.value
    def __set__(self, obj, value) -> None:
        if value > 9 or value < 0 or int(value) != value:
            raise AttributeError("The value is invalid")
        self.value = value


class Foo():
    number = OneDigitNumericValue()


if __name__ == '__main__':
    my_foo_object = Foo()
    my_second_foo_object = Foo()
    my_foo_object.number = 3
    print(my_foo_object.number)
    print(my_second_foo_object.number)
    my_third_foo_object = Foo()
    print(my_third_foo_object.number)


# Output:

"""
3
3
3
"""

#-------------------------------------------------------------------------------------------------


# (5).Adopt one base class and one subcalss


class CreditCard():  # self is CreditCard 
    def __init__(self, customer, bank, acnt, limit):
        self._customer = customer
        self._bank = bank
        self._account = acnt
        self._limit = limit
        self._balance = 0  # Start with a balance of zero
    def get_customer(self):
        return self._customer
    def get_bank(self):
        return self._bank
    def get_account(self):
        return self._account
    def get_limit(self):
        return self._limit
    def get_balance(self):
        return self._balance
    def set_balance(self, value):  # 新设置透支额
        self._balance = value
    def charge(self, price):
        try:
            price = float(price)  # Accept an int, float or string that can be converted to a float
        except:
            print('Invalid input')
            return False       
        if price + self._balance > self._limit:
            print(f'Your deposit of {price} exceeds your remainder of {self.get_limit() - self.get_balance()}')
            return False #You are going over your limit
        else:
            self._balance += price
            return True
    def make_payment(self, amount):
        try:
            amount = float(amount)  # Accept an int, float or string that can be converted to a float
        except:
            print('Invalid input')
            return False 
        self._balance -= amount
        return True


class PredatoryCreditCard2(CreditCard):
    MAX_CHARGES = 10
    def __init__(self, customer, bank, acnt, limit, apr):
        super().__init__(customer, bank, acnt, limit)
        self._apr = apr
        self._num_charges = 0
    def charge(self, price):
        success = super().charge(price)
        if not success:
            super().set_balance(super().get_balance() + 5)
        else:
            self._num_charges += 1
            if self._num_charges > self.MAX_CHARGES:
                super().set_balance(super().get_balance() + 1)
        return success
    def process_month(self):
        if self._balance > 0:
            monthly_factor = pow(1+self._apr, 1/12)
            super().set_balance(super().get_balance() * monthly_factor)
        self._num_charges = 0 # reset the counter at the beginning of each month


if __name__ == '__main__':
    wallet = []
    wallet.append(PredatoryCreditCard2('John Bowman' , 'California Savings' ,'56 5391 0375 9387 5309' , 2500, 0.15))
    wallet.append(PredatoryCreditCard2('John Bowman' , 'California Federal' ,'3485 0399 3395 1954' , 3500, 0.15))
    wallet.append(PredatoryCreditCard2('John Bowman' , 'California Finance' ,'5391 0375 9387 5309' , 5000, 0.30))
    for val in range (1,100):
        wallet[0].charge(val)
        wallet[1].charge(2*val)
        wallet[2].charge(3*val)
    for c in range(3):
        print ('Customer = ', wallet[c].get_customer())
        print ('Bank = ', wallet[c].get_bank())
        print('Account = ', wallet[c].get_account())
        print ('Limit = ', wallet[c].get_limit())
        print('Balance = ', wallet[c].get_balance())
        while wallet[c].get_balance() > 100:
            wallet[c].make_payment(100)
            print('New Balance = ', wallet[c].get_balance())
        print()


# Output:

"""
...
True
...
Your deposit of 171.0 exceeds your remainder of 166.0
False
True
True
Your deposit of 174.0 exceeds your remainder of 161.0
False
True
Your deposit of 118.0 exceeds your remainder of 30.0
False
Your deposit of 177.0 exceeds your remainder of 156.0
False
True
Your deposit of 120.0 exceeds your remainder of 25.0
False
Your deposit of 180.0 exceeds your remainder of 151.0
False
True
Your deposit of 122.0 exceeds your remainder of 20.0
False
Your deposit of 183.0 exceeds your remainder of 146.0
False
True
Your deposit of 124.0 exceeds your remainder of 15.0
False
Your deposit of 186.0 exceeds your remainder of 141.0
False
True
Your deposit of 126.0 exceeds your remainder of 10.0
False
Your deposit of 189.0 exceeds your remainder of 136.0
False
True
Your deposit of 128.0 exceeds your remainder of 5.0
False
...
Customer =  John Bowman
Bank =  California Savings
Account =  56 5391 0375 9387 5309
Limit =  2500
Balance =  2624.0
True
New Balance =  2524.0
True
New Balance =  2424.0
True
New Balance =  2324.0
True
New Balance =  2224.0
True
New Balance =  2124.0
True
"""

#-------------------------------------------------------------------------------------------------


 # (6).Adopt consecutive class inheritence


class CreditCard:
    """A consumer credit card."""
    def __init__(self, customer, bank, acnt, limit):
        """
        Create a new credit card instance.
        The initial balance is zero.
        customer  the name of the customer (e.g., 'John Bowman')
        bank      the name of the bank (e.g., 'California Savings')
        acnt      the acount identifier (e.g., '5391 0375 9387 5309')
        limit     credit limit (measured in dollars)
        """
        self._customer = customer
        self._bank = bank
        self._account = acnt
        self._limit = limit
        self._balance = 0
    def get_customer(self):
        # Return name of the customer.
        return self._customer
    def get_bank(self):
        # Return the bank's name.
        return self._bank
    def get_account(self):
        # Return the card identifying number (typically stored as a string).
        return self._account
    def get_limit(self):
        # Return current credit limit.
        return self._limit
    # __get__(self, onj, type=None)
    def get_balance(self):
        # Return current balance.
        return self._balance
    def set_balance(self, value):  # 新设置透支额
        self._balance = value
    def charge(self, price):
        # Charge given price to the card, assuming sufficient credit limit.
        # Return True if charge was processed; False if charge was denied.
        if price + self._balance > self._limit:  # if charge would exceed limit,
            return False                         # cannot accept charge
        else:
            self._balance += price
            return True
    def make_payment(self, amount):
        # Process customer payment that reduces balance.
        self._balance -= amount


class PredatoryCreditCard(CreditCard):
    """An extension to CreditCard that compounds interest and fees."""
    def __init__(self, customer, bank, acnt, limit, apr):
        """
        Create a new predatory credit card instance.
        The initial balance is zero.
        customer  the name of the customer (e.g., 'John Bowman')
        bank      the name of the bank (e.g., 'California Savings')
        acnt      the acount identifier (e.g., '5391 0375 9387 5309')
        limit     credit limit (measured in dollars)
        apr       annual percentage rate (e.g., 0.0825 for 8.25% APR)
        """
        super().__init__(customer, bank, acnt, limit)  # call super constructor
        self._apr = apr
        self._num_charges = 0
    def charge(self, price):
        """
        Charge given price to the card, assuming sufficient credit limit.
        Return True if charge was processed.
        Return False and assess $5 fee if charge is denied.
        """
        success = super().charge(price)          # call inherited method
        if not success:
            self._balance += 5                   # assess penalty
        return success                           # caller expects return value
    def process_month(self):
        # Assess monthly interest on outstanding balance.
        if self._balance > 0:
            # if positive balance, convert APR to monthly multiplicative factor
            monthly_factor = pow(1 + self._apr, 1/12)
            self._balance *= monthly_factor
        self._num_charges = 0


class PredatoryCreditCard2(CreditCard):
    MAX_CHARGES = 10
    def __init__(self, customer, bank, acnt, limit, apr):
        super().__init__(customer, bank, acnt, limit)
        self._apr = apr
        self._num_charges = 0
    def charge(self, price):
        success = super().charge(price)
        if not success:
            super().set_balance(super().get_balance() + 5)
        else:
            self._num_charges += 1
            if self._num_charges > self.MAX_CHARGES:
                super().set_balance(super().get_balance() + 1)
        return success
    def process_month(self):
        if self._balance > 0:
            monthly_factor = pow(1+self._apr, 1/12)
            super().set_balance(super().get_balance() * monthly_factor)
        self._num_charges = 0 # reset the counter at the beginning of each month


if __name__ == '__main__':
    wallet = []
    wallet.append(PredatoryCreditCard2('John Bowman' , 'California Savings' ,'56 5391 0375 9387 5309' , 2500, 0.15))
    wallet.append(PredatoryCreditCard2('John Bowman' , 'California Federal' ,'3485 0399 3395 1954' ,    3500, 0.15))
    wallet.append(PredatoryCreditCard2('John Bowman' , 'California Finance' ,'5391 0375 9387 5309' ,    5000, 0.30))
    for val in range (1,100):
        wallet[0].charge(val)
        wallet[1].charge(2*val)
        wallet[2].charge(3*val)
    for c in range(3):
        print ('Customer = ', wallet[c].get_customer())
        print ('Bank = ',     wallet[c].get_bank())
        print('Account = ',   wallet[c].get_account())
        print ('Limit = ',    wallet[c].get_limit())
        print('Balance = ',   wallet[c].get_balance())
        while wallet[c].get_balance() > 100:
            wallet[c].make_payment(100)
            print('New Balance = ', wallet[c].get_balance())
        print()


# Output:

"""
True
...
False
...
"""  
##############################################################################################


# C2.31. Write a Python class that extends the Progression class so that each value
# in the progression is the absolute value of the difference between the pre-
# vious two values. You should include a constructor that accepts a pair of
# numbers as the first two values, using 2 and 200 as the defaults. 


# Absolute value between previous values' difference 


class Progression:
    """
    Iterator producing a generic progression. Default iterator produces the 
    whole numbers 0, 1, 2, ...
    """
    def __init__(self, start=0):
        # Initialize current to the first value of the progression.
        self._current = start
    def _advance(self):
        """
        Update self._current to a new value.
        This should be overridden by a subclass to customize progression.
        By convention, if current is set to None, this designates the
        end of a finite progression.
        """
        self._current += 1
    def __next__(self):
        # The convention to end a progression
        if self._current is None:    
            raise StopIteration()
        else:
            answer = self._current     # record current value to return
            self._advance()            # advance to prepare for next time
            return answer              # return the answer
    def __iter__(self):
        # By convention, an iterator must return itself as an iterator.
        return self                  
    def print_progression(self, n):
        # Print next n values of the progression.
        print(' '.join(str(next(self)) for j in range(n)))


class AbsoluteDiffProgression(Progression):
    def __init__(self, first=2, second=200):
        self._current = first
        self._prev = 202
    def __next__(self):
        answer = self._current
        self._current, self._prev = abs(self._current-self._prev), self._current
        return answer


if __name__ == '__main__':
    p = Progression()
    p.print_progression(10)
    f = AbsoluteDiffProgression()
    # for i in range (8):
    #     print (f'Value Number {i+1} is {f[i]}')
    f.print_progression(8)


# Output:

"""
0 1 2 3 4 5 6 7 8 9
2 200 198 2 196 194 2 192
"""

##############################################################################################


# C3.32 Square root of the previous value 


class Progression:
    """
    Iterator producing a generic progression. Default iterator produces the 
    whole numbers 0, 1, 2, ...
    """
    def __init__(self, start=0):
        # Initialize current to the first value of the progression.
        self._current = start
    def _advance(self):
        """
        Update self._current to a new value.
        This should be overridden by a subclass to customize progression.
        By convention, if current is set to None, this designates the
        end of a finite progression.
        """
        self._current += 1
    def __next__(self):
        # The convention to end a progression
        if self._current is None:    
            raise StopIteration()
        else:
            answer = self._current     # record current value to return
            self._advance()            # advance to prepare for next time
            return answer              # return the answer
    def __iter__(self):
        # By convention, an iterator must return itself as an iterator.
        return self                  
    def print_progression(self, n):
        # Print next n values of the progression.
        print(' '.join(str(next(self)) for j in range(n)))


class SqrtProgression(Progression):
    def __init__(self, start=65536):
        self._current = start
    def __next__(self):
        answer = self._current
        self._current = self._current**0.5
        return answer
    def __getitem__(self, index):
        return(self._current**(1/(2**index)))


if __name__ == '__main__':
    p = Progression()
    p.print_progression(10)
    f = SqrtProgression()
    for i in range (8):
        print (f'Value Number {i+1} is {f[i]}')
    f.print_progression(8)


# Output:

"""
0 1 2 3 4 5 6 7 8 9
Value Number 1 is 65536.0
Value Number 2 is 256.0
Value Number 3 is 16.0
Value Number 4 is 4.0
Value Number 5 is 2.0
Value Number 6 is 1.4142135623730951
Value Number 7 is 1.189207115002721
Value Number 8 is 1.0905077326652577
65536 256.0 16.0 4.0 2.0 1.4142135623730951 1.189207115002721 1.0905077326652577
"""

##############################################################################################
##############################################################################################


# Part Three. OPP Projects

##############################################################################################


# P2.33 Input a ponynomial and output its derivative 


# (1).Define Polynomial class 


class Polynomial():
    def __init__(self, length = 3):
        self._coords = [0]*length 
    def __len__(self):
        return len(self._coords) 
    def __getitem__(self, index):
        if index >= len(self): raise IndexError('Index out of range') 
        return self._coords[index]
    def __repr__(self):
        output_string = []
        for i in range(len(self)):
            output_string.append(f'{self[i]}x^{i} ')
        return ''.join(output_string)
    def __setitem__(self, index, value):
        try:
            self._coords[index] = value
        except Exception as e:
            print (e)    
    def derivative(self):
        result = Polynomial(len(self)-1)
        for i in range(1, len(self)):
            result[i-1] = self[i]*i
        return result


if __name__ == '__main__':        
    p = Polynomial(10)
    for i in range(len(p)):
        p[i] = i
    print(p)
    p.derivative()


# Output:


"""
0x^0 1x^1 2x^2 3x^3 4x^4 5x^5 6x^6 7x^7 8x^8 9x^9 
1x^0 4x^1 9x^2 16x^3 25x^4 36x^5 49x^6 64x^7 81x^8 
"""

#-----------------------------------------------------------------------------------------------


# (2).Other solution


class Polynomial():
    def __init__(self, length = 3):
        self._coords = [0]*length 
    def __len__(self):
        return len(self._coords) 
    def __getitem__(self, index):
        if index >= len(self): 
            raise IndexError('Index out of range') 
        return self._coords[index]
    def __repr__(self):
        output_string = []
        for i in range(len(self)):
            output_string.append(f'{self[i]}x^{i} ')
            print(output_string)
        return ''.join(output_string)
    def __setitem__(self, index, value):
        try:
            self._coords[index] = value
        except Exception as e:
            print(e)    
    def derivative(self):
        result = Polynomial(len(self)-1)
        for i in range(1, len(self)):
            result[i-1] = self[i]*i
        return result


if __name__ == '__main__':        
    p = Polynomial(10)
    for i in range(len(p)):
        p[i] = i
    print(p)
    p.derivative()


# Output:

"""
['0x^0 ']
['0x^0 ', '1x^1 ']
['0x^0 ', '1x^1 ', '2x^2 ']
['0x^0 ', '1x^1 ', '2x^2 ', '3x^3 ']
['0x^0 ', '1x^1 ', '2x^2 ', '3x^3 ', '4x^4 ']
['0x^0 ', '1x^1 ', '2x^2 ', '3x^3 ', '4x^4 ', '5x^5 ']
['0x^0 ', '1x^1 ', '2x^2 ', '3x^3 ', '4x^4 ', '5x^5 ', '6x^6 ']
['0x^0 ', '1x^1 ', '2x^2 ', '3x^3 ', '4x^4 ', '5x^5 ', '6x^6 ', '7x^7 ']
['0x^0 ', '1x^1 ', '2x^2 ', '3x^3 ', '4x^4 ', '5x^5 ', '6x^6 ', '7x^7 ', '8x^8 ']
['0x^0 ', '1x^1 ', '2x^2 ', '3x^3 ', '4x^4 ', '5x^5 ', '6x^6 ', '7x^7 ', '8x^8 ', '9x^9 ']
0x^0 1x^1 2x^2 3x^3 4x^4 5x^5 6x^6 7x^7 8x^8 9x^9 
['1x^0 ']
['1x^0 ', '4x^1 ']
['1x^0 ', '4x^1 ', '9x^2 ']
['1x^0 ', '4x^1 ', '9x^2 ', '16x^3 ']
['1x^0 ', '4x^1 ', '9x^2 ', '16x^3 ', '25x^4 ']
['1x^0 ', '4x^1 ', '9x^2 ', '16x^3 ', '25x^4 ', '36x^5 ']
['1x^0 ', '4x^1 ', '9x^2 ', '16x^3 ', '25x^4 ', '36x^5 ', '49x^6 ']
['1x^0 ', '4x^1 ', '9x^2 ', '16x^3 ', '25x^4 ', '36x^5 ', '49x^6 ', '64x^7 ']
['1x^0 ', '4x^1 ', '9x^2 ', '16x^3 ', '25x^4 ', '36x^5 ', '49x^6 ', '64x^7 ', '81x^8 ']
1x^0 4x^1 9x^2 16x^3 25x^4 36x^5 49x^6 64x^7 81x^8 
"""

#-----------------------------------------------------------------------------------------------


# (3).Polynomial class ould set constant for derivative() method 


class Polynomial():
    def __init__(self, length=3):
        self._coords = [0]*length 
    def __len__(self):
        return len(self._coords) 
    def __getitem__(self, index):
        if index >= len(self): 
            raise IndexError('Index out of range') 
        return self._coords[index]
    def __repr__(self):
        output_string = []
        for i in range(1, len(self)): # add 1 
            output_string.append(f'{self[i]}x^{i} ')
            print(output_string)
        return ''.join(output_string)
    def __setitem__(self, index, value):
        try:
            self._coords[index] = value
        except Exception as e:
            print(e)    
    def derivative(self):
        result = Polynomial(len(self)-1)
        # for i in range(0, len(self)):
        for i in range(1, len(self)):
            result[i-1] = self[i]*i
            # print(result)
        return result


if __name__ == '__main__':        
    p = Polynomial(6)
    for i in range(len(p)):
        p[i] = i
    print(p)
    p.derivative()


# Output:

"""
['1x^1 ']
['1x^1 ', '2x^2 ']
['1x^1 ', '2x^2 ', '3x^3 ']
['1x^1 ', '2x^2 ', '3x^3 ', '4x^4 ']
['1x^1 ', '2x^2 ', '3x^3 ', '4x^4 ', '5x^5 ']
1x^1 2x^2 3x^3 4x^4 5x^5 
['4x^1 ']
['4x^1 ', '9x^2 ']
['4x^1 ', '9x^2 ', '16x^3 ']
['4x^1 ', '9x^2 ', '16x^3 ', '25x^4 ']
4x^1 9x^2 16x^3 25x^4 
"""

#-----------------------------------------------------------------------------------------------


# (4).Polynomial: x^0 + x^1 + ... + x^5


import math 


class Polynomial:
    def __init__(self, x):
        self.x = x 
    def function(self):
        poly = 0
        for i in range(6):
            poly += pow(self.x, i)
        return poly


if __name__ == '__main__':
    c = Polynomial(3)
    c.function()


# Output:

"""
364
"""

################################################################################################


# (5). Use Horner method to solve polynomial 


class Polynomial:
    def __init__(self, x):
        self.x = x 
    def horner(self, poly, n):
        # Initialize result
        result = poly[0]
        # Evaluate value of polynomial using Horner's method
        for i in range(1, n):
            result = result * self.x + poly[i]
            print(result)
        return result


if __name__ == '__main__':
    p = Polynomial(3)
    poly = [1,2,3,4,5,6]
    n = len(poly)
    print("Value of polynomial is:", p.horner(poly, n))


# Output:

"""
5
18
58
179
543
Value of polynomial is: 543
"""

#-------------------------------------------------------------------------------------------------


# + poly[1]x(n-2) + .. + poly[n-1]

def horner(poly, n, x):
    # Initialize result
    result = poly[0]
    # Evaluate value of polynomial
    # using Horner's method
    for i in range(1, n):
        result = result*x + poly[i]
    return result


if __name__ == '__main__':
    # Let us evaluate value of
    # 2x3 - 6x2 + 2x - 1 for x = 3
    poly = [1,2,3,4,5,6]
    x = 3
    n = len(poly)
    print("Value of polynomial is:", horner(poly, n, x))


# Output:

"""
Value of polynomial is: 543
"""

#-------------------------------------------------------------------------------------------------


# Polynomial：(x^0 + x^1 + ... + x^5) + ... + (6x^0 +6x^1+...6x^5)

class Polynomial:
    def __init__(self, x):
        self.x = x 
    def function(self):
        poly = 0
        num = [1,2,3,4,5,6]
        for i in num:
            for j in range(6):
                poly += i * pow(self.x, j)
        return poly


if __name__ == '__main__':
    c = Polynomial(3)
    c.function()


# Output:

# 7644

##############################################################################################


# P2.34 Write a Python program that inputs a document and then outputs a bar-
# chart plot of the frequencies of each alphabet character that appears in
# that document.

# (1).Show the frequency of every alphabat occcruency in a text 
# Sample text: Alice_in_Wonderland.txt


class DocumentReader():
    def __init__(self, filepath):
        self._filepath = filepath
        self._total_characters = 0
        self._charcount = self._initialize_array()
        self._read_document()
    def _read_document(self):
        fp = open(self._filepath)
        all_text = fp.read().lower()
        for char in all_text:
            if self._check_if_character(char):
                self._charcount[ord(char) - ord('a')] += 1
        self._total_characters = sum(self._charcount)      
    def _initialize_array(self):
        return [0]*(ord('z') - ord('a') + 1)
    def _check_if_character(self, char):
        number = ord(char)
        # Only need the first one since we .lower() -ed the original text. It will short-circuit
        # most of the time, so the second expression won't even be checked
        if (number<=ord('z') and number>=ord('a')) or (number<=ord('Z') and number>=ord('A')):
            return True
        else:
            return False
    def output_graph(self):
        max_value = max(self._charcount)
        for i in range(len(self._charcount)):
            print(chr(i+ord('a')), 'X'*int(self._charcount[i]/max_value*100))
        print('Each x represents: ', max_value*100, 'instances of that character(rounded down)')


if __name__ == '__main__': 
    aiw = DocumentReader(r'./Alice_in_Wonderland.txt')
    # aiw._charcount, aiw._total_characters
    aiw.output_graph()


# Output:

"""
a XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
b XXXXXXXXXX
c XXXXXXXXXXXXXXXXX
d XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
e XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
f XXXXXXXXXXXXXX
g XXXXXXXXXXXXXXXXXX
h XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
i XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
j X
k XXXXXXXX
l XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
m XXXXXXXXXXXXXXX
n XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
o XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
p XXXXXXXXXXX
q X
r XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
s XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
t XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
u XXXXXXXXXXXXXXXXXXXXXXXXX
v XXXXXX
w XXXXXXXXXXXXXXXXXXX
x X
y XXXXXXXXXXXXXXXX
z 
Each x represents:  1357900 instances of that character(rounded down)
"""

##############################################################################################


# (2).Define DocumentReader lclas


class DocumentReader():
    def __init__(self, filepath):
        self._filepath = filepath
        self._total_characters = 0
        self._charcount = self._initialize_array()
        self._read_document()
    def _read_document(self):
        fp = open(self._filepath)
        all_text = fp.read().lower()
        for char in all_text:
            if self._check_if_character(char):
                self._charcount[ord(char) - ord('a')] += 1
        self._total_characters = sum(self._charcount)      
    def _initialize_array(self):
        return [0]*(ord('z') - ord('a') + 1)
    def _check_if_character(self, char):
        number = ord(char)
        # Only need the first one since we .lower() -ed the original text. It will short-circuit
        # most of the time, so the second expression won't even be checked
        if (number<=ord('z') and number>=ord('a')) or (number<=ord('Z') and number>=ord('A')):
            return True
        else:
            return False
    def output_graph(self):
        max_value = max(self._charcount)
        for i in range(len(self._charcount)):
            print(chr(i+ord('a')))
            print('X'*int(self._charcount[i]/max_value*100)) # X could be changed as A or 8 
        print('Each X represents: ', max_value*100, 'instances of that character(rounded down)')


if __name__ == '__main__': 
    aiw = DocumentReader(r'./Alice_in_Wonderland.txt')
    # aiw._charcount, aiw._total_characters
    aiw.output_graph()

# Output:

"""
a
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
b
XXXXXXXXXX
c
XXXXXXXXXXXXXXXXX
d
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
e
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
f
XXXXXXXXXXXXXX
g
XXXXXXXXXXXXXXXXXX
h
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
i
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
j
X
k
XXXXXXXX
l
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
m
XXXXXXXXXXXXXXX
n
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
o
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
p
XXXXXXXXXXX
q
X
r
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
s
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
t
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
u
XXXXXXXXXXXXXXXXXXXXXXXXX
v
XXXXXX
w
XXXXXXXXXXXXXXXXXXX
x
X
y
XXXXXXXXXXXXXXXX
z

Each x represents:  1357900 instances of that character(rounded down)
>>> 
"""

##############################################################################################


# P2.35. Write a set of Python classes that can simulate an Internet application in
# which one party, Alice, is periodically creating a set of packets that she
# wants to send to Bob. An Internet process is continually checking if Alice
# has any packets to send, and if so, it delivers them to Bob’s computer, and
# Bob is periodically checking if his computer has a packet from Alice, and,
# if so, he reads and deletes it.


# Alice Bob Online Program 


import random

# Unknowns: What happens if you create a new packet without deleting the old one?
# Assume it overwrites it


class AliceBot():
    CHANCE_OF_ACTING = 0.3
    def __init__(self):
        self._current_packet = None
    def act(self):
        if random.random() <= self.CHANCE_OF_ACTING:
            self._current_packet = self._create_packet()
            return True
        else: 
            return False
    def _create_packet(self):
        length = random.randint(5,20)
        packet = [' ']*length
        for i in range(length):
            packet[i] = chr(random.randint(ord('A'), ord('z')))
        return ''.join(packet)
    def get_packet(self):
        return self._current_packet
    def delete_packet(self):
        self._current_packet = None


class InternetBot():
    def __init__(self):
        self._new_packet = False
        self._Alice = None
    def check_for_packet(self):
        if self._Alice.get_packet() is not None:
            return True
        else:
            return False
    def read_packet(self):
        if self._new_packet:
            return self._Alice.get_packet()
        else:
            return None
    def delete_packet(self):
        self._Alice.delete_packet()
    def assign_Alice(self, alice):
        self._Alice = alice


class BobBot():
    def check_for_packet(self, other):
        if other.check_for_packet():
            return True
        else:
            return False
    def delete_packet(self, other):
        other.delete_packet()


if __name__ == '__main__': 
    # Simulator for this process
    Alice = AliceBot()
    Inter = InternetBot()
    Inter.assign_Alice(Alice)
    Bob = BobBot()
    for i in range(50):
        print(f'Time is {i}')
        if Alice.act(): 
            print('Created the packet', Alice.get_packet())    
        if Bob.check_for_packet(Inter): 
            print('Bob detected the packet')
            Bob.delete_packet(Inter)


##############################################################################################


# P2.36. Write a Python program to simulate an ecosystem containing two types
# of creatures, bears and fish. The ecosystem consists of a river, which is
#modeled as a relatively large list. Each element of the list should be a
#Bear object, a Fish object, or None. In each time step, based on a random
# process, each animal either attempts to move into an adjacent list location
# or stay where it is. If two animals of the same type are about to collide in
# the same cell, then they stay where they are, but they create a new instance
# of that type of animal, which is placed in a random empty (i.e., previously
# None) location in the list. If a bear and a fish collide, however, then the
# fish dies (i.e., it disappears).


# Bear and fish ecosystem 


import random


# These should be nested in theory and then accessed using self.Bear, or self.Fish

class RiverEcosystem():
    class Bear():
        def __init__(self, location):
            self._location = location
    class Fish():
        def __init__(self, location):
            self._location = location
    MOVE_CHANCE = 0.3
    LR_CHANCE = 0.5
    def __init__(self, length=100, bears=3, fish=10):
        self._ecosystem = [None]*length
        self._bears = self.assign_object(self.Bear, bears)
        self._fish = self.assign_object(self.Fish, fish)
        self._time = 0
    def __len__(self):
        return (len(self._ecosystem))
    def __getitem__(self, index):
        return self._ecosystem[index]
    def __setitem__(self, index, value):
        self._ecosystem[index] = value
    def assign_object(self, obj, number):
        assigned = 0
        object_list = []
        maximum_attempts = 100
        attempts = 0
        while assigned < number and attempts < maximum_attempts:
            attempts += 1
            i = random.randint(0, len(self)-1)
            if self[i] is None:
                new_obj = obj(i)
                assigned += 1
                self[i] = new_obj
                object_list.append(new_obj)
        return object_list
    def __repr__(self):
        output_string = []
        for element in self._ecosystem:
            if element is None:
                output_string += '-'
            elif isinstance(element, self.Bear):
                output_string += 'B'
            elif isinstance(element, self.Fish):
                output_string += 'F'
            else:
                output_string += '?'   
        return ''.join(output_string)
    def _delete_object(self, obj, obj_list):
        # Challenge is to also delete it from the list of bears/fish
        target = None
        for i in range(len(obj_list)):
            if obj is obj_list[i]:
                target = i
        if target is not None: 
            del (obj_list[target])
    def _attempt_move(self, obj, target_location):
        if target_location < 0 or target_location >=　len(self):
            # print('Move is out of bounds')
            return False
        elif self[target_location] is None:
            self[obj._location], self[target_location] = self[target_location], self[obj._location]
        elif type(obj) == type(self[target_location]):
            # if they are the same type, create one new instance of that object
            self.assign_object(type(obj), 1)
        # if not the same, check who is the fish...
        elif isinstance(obj, self.Fish):
            self._delete_object(obj, self._fish)
        elif isinstance(self[target_location], self.Fish):
            self._delete_object(self[target_location], self._fish)
    def determine_action(self, obj):
        if random.random() < self.MOVE_CHANCE:
            if random.random() < self.LR_CHANCE:
                self._attempt_move(obj, obj._location - 1)
            else:
                self._attempt_move(obj, obj._location + 1)
    def timestep(self):
        self._time += 1
        for f in self._fish:
            self.determine_action(f)
        for b in self._bears:
            self.determine_action(b)

    
if __name__ == '__main__':  
    Game1 = RiverEcosystem(100)
    print('Currently playing a game with 3 bears and 10 fish')
    for _ in range(40):
        print (Game1)
        Game1.timestep()
    print('\n\n')
    Game2 = RiverEcosystem (100, 10, 10)
    print ('Currently playing a game with 10 bears and 10 fish')
    for _ in range(40):
        print (Game2)
        Game2.timestep()

##############################################################################################


# P2.37. Write a simulator, as in the previous project, but add a Boolean gender
# field and a floating-point strength field to each animal, using an Animal
# class as a base class. If two animals of the same type try to collide, then
# they only create a new instance of that type of animal if they are of differ-
# ent genders. Otherwise, if two animals of the same type and gender try to
# collide, then only the one of larger strength survives.


class RiverEcosystem2(RiverEcosystem):
    class Bear():
        def __init__(self, location):
            self._location = location
            self._strength = random.random()
            self._gender = True if random.random()>0.5 else False
    class Fish():
        def __init__(self, location):
            self._location = location
            self._strength = random.random()
            self._gender = True if random.random()>0.5 else False
    def _attempt_move(self, obj, target_location):
        if target_location < 0 or target_location >= len(self):
            # print ('Move is out of bounds')
            return False
        elif self[target_location] is None:
            self[obj._location], self[target_location] = self[target_location], self[obj._location]
        elif type(obj) == type(self[target_location]):
            # if they are the same type and gender, create one new instance of that object
            if obj._gender == self[target_location]._gender:
                self.assign_object(type(obj), 1)
            else:
                to_delete = min(obj, self[target_location], key = lambda x: x._strength)
                object_list = self._fish if isinstance(obj, self.Fish) else self._bears
                # print(f'A fight!!  Of strengths {obj._strength} and {self[target_location]._strength}, {to_delete._strength} loses')
                self._delete_object(to_delete, object_list)
        # if not the same, check who is the fish...
        elif isinstance(obj, self.Fish):
            self._delete_object(obj, self._fish)
        elif isinstance(self[target_location], self.Fish):
            self._delete_object(self[target_location], self._fish)

            
if __name__ == '__main__':            
    Game1 = RiverEcosystem2(100)
    print('Currently playing a game with 3 bears and 10 fish')
    for _ in range(40):
        print (Game1)
        Game1.timestep()
    print('\n\n')  
    Game2 = RiverEcosystem2(100, 10, 10)
    print('Currently playing a game with 10 bears and 10 fish')
    for _ in range(40):
        print (Game2)
        Game2.timestep()
    b1, b2 = Game2._bears[0], Game2._bears[1]


# Output:

"""
Omit 
"""

##############################################################################################


# P2.38. Write a Python program that simulates a system that supports the func-
# tions of an e-book reader. You should include methods for users of your
# system to “buy” new books, view their list of purchased books, and read
# their purchased books. Your system should use actual books, which have
# Zexpired copyrights and are available on the Internet, to populate your set
# of available books for users of your system to “purchase” and read

# Write a book with buy, check and read methods. 


import random
from pathlib import Path
from IPython.display import clear_output


"""
Areas for improvement:
- Page select
- Improve the flow between the book class and the main program
"""


class EbookReader():
    class Book():
        MIN_PRICE = 2
        MAX_PRICE = 20
        LINES_PER_PAGE = 15
        def __init__(self, filepath):
            self._name = str(filepath.name).replace('.txt', '')
            self._filepath = filepath
            self._price = random.random()*(self.MAX_PRICE-self.MIN_PRICE) + self.MIN_PRICE
            self._purchased = False
            self._current_position = 0
            self._iostream = open(self._filepath, encoding = 'latin-1')
            self._length = self.determine_length()
        def __repr__(self):
            return(f'Book: {self._name}, Price: {self._price}, Purchased: {self._purchased}')
        def purchase_book(self):
            self._purchased = True
        def open_book(self):
            if self._purchased:
                return open(self._filepath)
            else:
                print('Please purchase this book first!')
                return None
        def seek_path(self, page=0):
            self._iostream.seek(0)
            num_lines = page*self.LINES_PER_PAGE
            for _ in range(num_lines):
                self._iostream.readline()
        def read_book(self, page = None):
            if not self._purchased:
                print('Please purchase this book first!')
                return False
            else:
                start = self._current_position if page is None else page
                print(start)
                fp = self._iostream
                self.seek_path(start)
                for _ in range(self.LINES_PER_PAGE):
                    print(fp.readline())
                self._current_position = start + 1
                return True
        def __len__(self):
            return self._length
        def __getitem__(self, value):
            #Choose this order to shortcircuit in the event that it is not an int
            if isinstance(value, int) and value < len(self) and value>0:
                self.read_book(value)
            else:
                print('Invalid input')
        def determine_length(self):
            self._iostream.seek(0)
            lines = self._iostream.readlines()
            return len(lines)
    # Need a sample file
    def __init__(self, book_dir = './Chapter2_Books'):
        self._book_dir = Path(book_dir)
        self._library = self._build_book_dictionary()
        self._balance = 0
        self._currentbook = None
        self._statusmessage = 'Nothing to report...'
    def load_money(self, value):
        try:
            self._balance += float(value)
            return True
        except Exception as e:
            self.out(f'Invalid input: {e}')
            return False
    def out(self, message):
        self._statusmessage = message
    def purchase_book(self, bookname):
        if bookname in self._library:
            book = self._library[bookname]
            if book._purchased:
                self.out('You have already purchased this book')
                return False
            elif self._balance >= book._price: 
                book.purchase_book()
                self._balance -= book._price
                return True
            else:
                self.out('You have insufficient funds for that purchase')
                return False
        else:
            self.out('Book not in library')
            return False
    def read_book(self, bookname, page = None):
        #Need to add more error handling here...
        if bookname in self._library:
            self._library[bookname].read_book(page = page)
            self._currentbook = self._library[bookname]
            return True
        else:
            self.out('Book not found')
            return False
    def _read_page(self, book, page = None):
        book.read_book(page = page)
        return True
    def _build_book_dictionary(self):
        #create a list of all the books
        booklist = {str(x.name).replace('.txt', ''):self.Book(x) for x in self._book_dir.iterdir() if str(x).endswith('.txt')}
        return booklist
    def _print_catalog(self):
        print("The following books are available for purchase:")
        for book in self._library.values():
            if not book._purchased: print(book)      
    def _print_owned(self):
        print('You have purchased the following books:')
        for book in self._library.values():
            if book._purchased: print(book) 
    def _print_balance(self):
        print('\nYour current balance is: ', self._balance)
    def __repr__(self):
        #clear_output()
        print('Current message is:', self._statusmessage, '\n')
        self._print_owned()
        print('')
        self._print_catalog()
        self._print_balance()
        print('Your current book is:', self._currentbook)
        return('')  #Note: a call to print expects a returned string
    def console(self):
        clear_output()
        self._read_page(self._currentbook)
        print(self)
        print('Commands are: Purchase, Open, Next (for the next page)')
        input_results = self.get_input()
        return input_results
    def get_input(self):
        input_string = input()
        if input_string == 'exit':
            return False
        elif input_string.lower() == 'purchase':
            input_purchase = input('Which book would you like to purchase')
            self.purchase_book(input_purchase)
            return True #purchase a new book if you can
        elif input_string == 'next':
            #self.current_book
            return True #read the next page of the book
        elif input_string == 'open':
            input_book = input('Which book would you like to open')
            self._currentbook = input_book
            # open a new book (position of the old one is still saved)
            return True
        else:
            self.out('Invalid input')
            return True


if __name__ == '__main__':          
    eb1 = EbookReader()       
    eb1.load_money(1000)
    eb1.purchase_book('Alice in Wonderland')
    eb1.purchase_book('Frankenstein')
    print(eb1)
    eb1.read_book('Alice in Wonderland')
    for _ in range(10):
        eb1.read_book('Alice in Wonderland')
    eb1.read_book ('Alice in Wonderland', 500)
    eb1._library['Alice in Wonderland'][20]
    eb1._library['Alice in Wonderland']['ollo']


##############################################################################################


# P2.39 Develop an inheritance hierarchy based upon a Polygon class that has
# abstract methods area( ) and perimeter( ). Implement classes Triangle,
# Quadrilateral, Pentagon, Hexagon, and Octagon that extend this base
# class, with the obvious meanings for the area( ) and perimeter( ) methods.
# Also implement classes, IsoscelesTriangle, EquilateralTriangle, Rectan-
#gle, and Square, that have the appropriate inheritance relationships. Fi-
# nally, write a simple program that allows users to create polygons of the
# various types and input their geometric dimensions, and the program then
# outputs their area and perimeter. For extra effort, allow users to input
#polygons by specifying their vertex coordinates and be able to test if two
# such polygons are similar.


# It wasn't as fleshed out as the other answers since the final objective wasn't as 
# clear/interesting


from abc import abstractmethod, ABCMeta
import math


class Polygon(metaclass = ABCMeta):
    def __init__(self, side_lengths = [1,1,1], num_sides = 3):
        self._side_lengths = side_lengths
        self._num_sizes = 3
    @abstractmethod
    def area(self):
        pass
    @abstractmethod
    def perimeter(self):
        pass
    def __repr__(self):
        return (str(self._side_lengths))


class Triangle(Polygon):
    def __init__(self, side_lengths):
        super().__init__(side_lengths, 3)
        self._perimeter = self.perimeter()
        self._area = self.area()
    def perimeter(self):
        return(sum(self._side_lengths))
    def area(self):
        s = self._perimeter/2
        product = s
        for i in self._side_lengths:
            product*=(s-i)
        return product**0.5


class EquilateralTriangle(Triangle):
    def __init__(self, length):
        super().__init__([length]*3)


if __name__ == '__main__':         
    t1 = Triangle([1,2,2])
    print(t1.perimeter(), t1.area())
    t2 = EquilateralTriangle(3)
    print(t2.perimeter(), t2.area())
    print(t2)


# Output:

"""
5 0.9682458365518543
9 3.897114317029974
[3, 3, 3]
"""