#Программа для сравнения двух списков
list_1 = [10, 21, 13, 52, 100]
list_2 = [10, 21, 13, 52, 100]

if len(list_1) == len(list_2):
  trfa = True
  index = 0

  while index < len(list_1):
    if list_1[index] != list_2[index]:
      trfa = False
      break
    else:
      index += 1
  
  if trfa:
    print("Списки равны")
  else:
    print("Списки не равны")
else:
  print("Списки не равны")
  