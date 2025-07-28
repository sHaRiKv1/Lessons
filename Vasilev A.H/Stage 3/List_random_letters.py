#Программа с функцией для создания вложенных списков с рандомными буквами
from random import randint

def list_in_list(count_list, element_list):
  list = [[] for j in range(count_list)]
  for i in range(len(list)):
    while len(list[i]) < element_list:
      list[i].append(chr(randint(65, 90)))
  return list

print(list_in_list(5, 4))
