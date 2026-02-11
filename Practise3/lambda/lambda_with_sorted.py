#1
students = [("Emil", 25), ("Tobias", 22), ("Linus", 28)]
sorted_students = sorted(students, key=lambda x: x[1])
print(sorted_students)

#2
words = ["apple", "pie", "banana", "cherry"]
sorted_words = sorted(words, key=lambda x: len(x))
print(sorted_words)

#3
# sorted() - лямбдамен
adamdar = [
    {"aty": "Айша", "zhasy": 25},
    {"aty": "Бекзат", "zhasy": 20},
    {"aty": "Самат", "zhasy": 30}
]

# Жасы бойынша сұрыптау
suroptalgan = sorted(adamdar, key=lambda x: x["zhasy"])
print("Жасы бойынша:")
for adam in suroptalgan:
    print(f"{adam['aty']}: {adam['zhasy']}")