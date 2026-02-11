# Класс әдістері
class Matematika:
    def kos(self, a, b):
        return a + b
    
    def alu(self, a, b):
        return a - b

class Tin:
    def zhauap(self):
        print("Бұл компьютер")

m = Matematika()
t = Tin()

print(m.kos(15, 7))
print(m.alu(15, 7))
t.zhauap()