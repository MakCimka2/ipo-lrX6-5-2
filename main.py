import random
numbers = [-3, -5, -2, -12, 0, 15, 4, 7, 2]
sum = 0
y = list()
weight =random.randint(4, 4)
length = random.randint(4, 4)
for i in range(weight) :
    y = [random.choice(numbers) for i in range(length)]
    print(y)
for i in numbers: 
    if i < 0:
        sum += i
print(f"Сумма всех отрицательных элементов равнa : {sum}")

