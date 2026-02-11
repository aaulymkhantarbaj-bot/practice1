# Класс айнымалылары
class Student:
    mektep = "1 мектеп"  # Класс айнымалысы
    
    def __init__(self, name):
        self.name = name  # Инстанс айнымалысы

s1 = Student("Айша")
s2 = Student("Бекзат")

print(f"{s1.name}: {s1.mektep}")
print(f"{s2.name}: {s2.mektep}")

Student.mektep = "2 мектеп"  # Барлығына өзгереді
print(f"{s1.name}: {s1.mektep}")