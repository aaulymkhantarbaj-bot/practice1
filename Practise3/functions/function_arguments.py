#1
# Аргументтері бар функциялар
def ate_zhas(ate, zhas):
    print(f"Аты: {ate}, Жасы: {zhas}")

def kobeitu(a, b):
    print(f"{a} * {b} = {a * b}")

# Шақыру
ate_zhas("Ayau", 18)
kobeitu(4, 5)

#2
# Позициялық аргументтер
def student(name, age):
    print(f"Аты: {name}, Жасы: {age}")

student("Daryn", 20)

#3
# Default аргумент
def country(city, country="Қазақстан"):
    print(f"{city} - {country}")

country("Астана")
country("Мәскеу", "Ресей")
