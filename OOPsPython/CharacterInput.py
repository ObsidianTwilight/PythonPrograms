"""Create a program that asks the user to enter their name and their age. Print out a message addressed to them that tells them the year that they will turn 100 years old"""

import datetime

class Character:
    def __init__(self, name, age):
        self.name =  name
        self.age = age

    # Function for age after 100 years 
    # Method 1 
    def AgeCalculator(self):
        current_date = datetime.date.today()
        current_year = current_date.year
        
        key = 100 - self.age
        centenary = current_year + key

        print(f"The age of {self.name} after 100 years is:", centenary)

    # Method 2
    def AgeCalculator2(self):
        current_date = datetime.date.today()
        current_year = current_date.year
        
        yob = current_year - self.age
        centenary = yob + 100
        
        print(f"The age of {self.name} after 100 years is:", centenary)
        
    
person1 = Character("Sourabh", 22)
person1.AgeCalculator()
