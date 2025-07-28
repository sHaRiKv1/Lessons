#Функция возвращающая второе по величине число списка 
list = [5, 10, 1, 60, 25, 3]

def second_max(spisok):
  spisok_sort = sorted(spisok)
  return(spisok_sort[-2])

print(second_max(list))
