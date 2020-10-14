num = 123321
sum_1 = 0
sum_2 = 0
for x in range(3):
    sum_1 = sum_1 + num % 10
    num = num // 10
for x in range(3):
    sum_2 = sum_2 + num % 10
    num = num // 10
if sum_1 == sum_2:
    print("Счастливый билет")
else:
    print("Несчастливый билет")
