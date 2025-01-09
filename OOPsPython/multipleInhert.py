class university:
    def title(self):
        print("Home university")

class college:
    def award(self):
        print("Autonomos")

#Class state inherits class university and class college same time!
class state(university,college):
    def priority(self):
        print("Priority goes to university!")

test = state()

print(test.award(),
      test.title(),
      test.priority())