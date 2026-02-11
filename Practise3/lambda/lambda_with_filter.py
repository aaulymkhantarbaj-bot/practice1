#1
numbers = [1, 2, 3, 4, 5, 6, 7, 8]
odd_numbers = list(filter(lambda x: x % 2 != 0, numbers))
print(odd_numbers)

#2
# filter() функциясымен
sandar = [3, 7, 12, 15, 18, 21]

# 10-нан үлкендер
ulken = list(filter(lambda x: x > 10, sandar))
print(ulken)

# 3-ке бөлінетіндер
bolinetin = list(filter(lambda x: x % 3 == 0, sandar))
print(bolinetin)
