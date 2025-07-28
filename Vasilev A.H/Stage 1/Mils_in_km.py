#Программа переводящая мили в км
miles = input("Введите расстояние в милях: ")

if float(miles) < 0:
  print("Расстояние не бывает  отрицательным!")
else:
  print(str(miles) + " миль, это - " + str(float(miles) * 1.6) + " км.")
