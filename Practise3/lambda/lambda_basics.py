#1
def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(2)

print(mydoubler(11))

#2
# Қарапайым лямбда
kos = lambda x, y: x + y
print(kos(10, 5))

# Бір аргумент
kvadrat = lambda x: x ** 2
print(f"5-тің квадраты: {kvadrat(5)}")