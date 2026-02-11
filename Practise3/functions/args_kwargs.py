# *args - көп сандар
def ortasha(*sandar):
    print(sum(sandar) / len(sandar))

# **kwargs - көп мәлімет
def student(**akparat):
    print(akparat["aty"], akparat["baga"])

# Қолдану
ortasha(4, 6, 8, 10)
student(aty="Ayau", baga=100, pan="pp2")

# *args - көп аргумент
def songy(*sandar):
    print(f"Барлығы: {sum(sandar)}")

songy(1, 2, 3, 4, 5)