# Қосу функциясы
def qos(a, b):
    return a + b

natije = qos(5, 3)
print(f"5 + 3 = {natije}")

# Екі мәнді қайтару
def esep(a, b):
    qos = a + b
    kobeitu = a * b
    return qos, kobeitu

q, k = esep(4, 5)
print(f"Қосынды: {q}, Көбейтінді: {k}")

# Мән қайтаратын функциялар
def zhasy_10(zhas):
    return zhas + 10

def auparym(sóz):
    return sóz[::-1]

# Қолдану
print(zhasy_10(15))
print(auparym("Python"))