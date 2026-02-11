#1
class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

class Student(Person):
  def __init__(self, fname, lname):
    super().__init__(fname, lname)

x = Student("Mike", "Olsen")
x.printname()

#2
# super() қолдану
class Ata:
    def __init__(self, ate):
        self.ate = ate

class Bala(Ata):
    def __init__(self, ate, zhas):
        super().__init__(ate)
        self.zhas = zhas

b = Bala("Айдар", 12)
print(b.ate, b.zhas)
