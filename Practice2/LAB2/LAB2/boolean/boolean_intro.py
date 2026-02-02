#1
a = 200
b = 33

if b > a:
  print(bool("b is greater than a"))
else:
  print(bool("b is not greater than a"))

#2
is_sunny = True
is_raining = False

print("Is it sunny?", is_sunny)
print("Is it raining?", is_raining)

#3
print(bool(False))
print(bool(None))
print(bool(0))
print(bool(""))
print(bool(()))
print(bool([]))
print(bool({}))

#4
def myFunction() :
  return True

if myFunction():
  print("YES!")
else:
  print("NO!")

#5
print(bool("abc"))
print(bool(123))
print(bool(["apple", "cherry", "banana"]))