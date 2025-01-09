#WE CAN USE 'SUPER' WHEN YOU WANT TO ACCESS THE STATEMENT OF CONSTRUCTOR IN SUPER CLASS
# SUPER CLASS MEANS THE PROPERTIES OF CLASS YOU INHERITED IN ANOTHER CLASS BY USING 
#INHERITANCE!

class customer:
    statement = "this is the customer class"

    def __init__(self):
        self.var = "I'm in constructor of class costomer"
        self.statement = "This is instance variable" #Instance variable
        self.IMP = "This is IMP statement, before using super function"
        self.special = "This is special statement after using super function"

class seller(customer):
    statement = "I'm in the class seller"#Method overriding
    
    #super()
    #Constructor overriding ie. same constructor present in customer class
    def __init__(self):
        super().__init__()
        self.var = "I'm in constructor of class seller"
        self.statement = "This is instance variable in class seller"#Instance variable
    
#Making instances of class customer and class seller
cus = customer()
se = seller()

#If I do the constructor overriding in class seller, I can't use the other statements of constructor in customer class
#Hence to use the other statements ie. statements other than in overrided const.
#I have to use super function to access 'self.special' statement!

#print(se.var)
#print(se.statement)
#I want to run constructor of class customer
print(se.IMP)#Before using super, it throwing error!
#Error is: You can't access constructor of class cutomer by using instance 'se', cause 
#the constructor of class customer is overrided!
print(se.special)
