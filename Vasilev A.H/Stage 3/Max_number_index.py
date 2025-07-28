#Функция для поиска максимального значения и его индекса в списке
from random import randint

list = [randint(0, 100) for i in range(10)]
print(list)

def max_index_list(spisok):
  max = 0
  ind = 0
  for i in range(len(spisok)):
    if spisok[i] > max:
      max = spisok[i]
      ind = spisok.index(spisok[i])
    else:
      continue
  list = [max, ind]
  return list

print(max_index_list(list))
