#Формирование нового списка на основе двух предыдущих
#поочерёдной вставкой элементов из каждого списка
from random import randint

list_1 = [randint(0, 100) for i in range(10)]
list_2 = [randint(0, 100) for i in range(10)]
list_3 = []
print(list_1)
print(list_2)

for i in range(len(list_1)):
  list_3.append(list_1[i])
  list_3.append(list_2[i])

print(list_3)
