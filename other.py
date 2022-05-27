a = None
b = None
if a and b:
    print("Обе переменные истинные")
    print(a,b)
elif a or b:
    print("Одна из переменных истинная")
    print(a or b) # печать одной переменной, той, которая является истинной
else:
    print("Обе переменные ложные")