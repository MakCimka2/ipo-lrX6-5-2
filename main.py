import random
numbers = [-3, -5, -2, -12, 0, 15, 4, 7, 2]
sum = 0
weight = random.randint (4, 8)
length = random.randint(4, 8)
y = [[random.choice(numbers) for i in range(weight)] for j in range(length)]
for i in range (length):
    for j in range(weight):
        print(y[i][j], end = ' ')
    print()
for row in y:
    for element in row: 
            if element < 0:
                sum += element
print(f"Сумма всех отрицательных элементов равнa : {sum}")
