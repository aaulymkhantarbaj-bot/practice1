#1
class Mom:
    def sing(self):
        print("sing")

class Dad:
    def swim(self):
        print("swim")

class Child(Mom, Dad):
    def code(self):
        print("code")

c = Child()
c.sing()   # Mom-нан
c.swim()   # Dad-тан
c.code()   # Өзінің