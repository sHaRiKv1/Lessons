#Программа выводящая в прямом и обратном порядке список чисел, которые при делении на 5 дают остаток 3
list_1 = [5 * k + 3 for k in range(1, 10)]
list_reverse = list(reversed(list_1))

print(list_1)
print(list_reverse)
