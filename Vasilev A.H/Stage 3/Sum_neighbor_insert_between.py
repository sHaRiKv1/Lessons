#Программа подсчёта суммы соседних элементов
#списка и её вставка между этими элементами
from random import randint

list = [randint(0, 100) for i in range(10)]
print(list)

for i in range(0, (len(list) - 1) * 2, 2):
  list.insert(i + 1, list[i] + list[i + 1])
  
print(list)
