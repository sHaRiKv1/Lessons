#Программа для сортировки элементов списка с чётными и нечётными 
#индексами по возрастанию и убыванию соответственно
from random import randint

list = [randint(0, 100) for i in range(10)]
print(list)

for j in range(len(list)):
  for i in range(len(list) - 2):
    if i % 2 == 0:
      if list[i] > list[i + 2]:
        a = list[i + 2]
        list[i + 2] = list[i]
        list[i] = a
    else:
      if list[i] < list[i + 2]:
        a = list[i + 2]
        list[i + 2] = list[i]
        list[i] = a

print(list)
