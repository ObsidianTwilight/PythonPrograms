class animal:
    def Sound(self):
        print("Animal has sound")

class dog(animal):
    def dogsound(self):
        print("Dog is barking")

class dogpuppy(dog):
    def __init__(self,sounD):
        self.sound = sounD
        print("puppy are playing")

test = dogpuppy("Bhow")
print(test.sound)
print(
test.dogsound(),
test.Sound())
