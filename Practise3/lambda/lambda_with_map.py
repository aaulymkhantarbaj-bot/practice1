#1
numbers = [1, 2, 3, 4, 5]
doubled = list(map(lambda x: x * 2, numbers))
print(doubled)

#2
# map() - лямбдамен
sandar = [1, 2, 3, 4, 5]

# Квадраттар
kvadrattar = list(map(lambda x: x ** 2, sandar))
print(f"Квадраттар: {kvadrattar}")

# 2-ге көбейту
ekilang = list(map(lambda x: x * 2, sandar))
print(f"Екі есе: {ekilang}")