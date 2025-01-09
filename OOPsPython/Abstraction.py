from abc import ABC,abstractmethod

#Abstract class
class softBranch(ABC):
   #We shouldn't pass any argument to abstract method 
    def branch(self):
        pass

class CSE(softBranch):
    def branch(self):
        print("soft branch has CSE branch")

class AIML(softBranch):
    def branch(self):
        print("soft branch has AIML branch")

class IT(softBranch):
    def branch(self):
        print("soft branch has IT branch")

C = CSE()
C.branch()

A = AIML()
A.branch()

I = IT()
I.branch()