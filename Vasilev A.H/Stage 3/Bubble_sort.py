#Сортировка списка методом пузырька (по возрастанию)
from random import randint

list = [randint(0, 100) for i in range(10)]
print(list)

for j in range(len(list)):
  for i in range(len(list) - 1):
    if list[i] > list[i + 1]:
      a = list[i + 1]
      list[i + 1] = list[i]
      list[i] = a

print(list)
