#Программа считающая возраст пользователя
year_now = int(input("Какой сейчас год?\n"))
year_burn = int(input("Введите год вашего рождения:\n"))
if year_now < 0 or year_burn < 0 or year_now - year_burn <= 0:
  print("Вас либо ещё нет на этом свете, либо вы ввели отрицательное число, что тоже недопустимо!")
elif year_now - year_burn == 1:
  print("Вам " + str(year_now - year_burn) + " год!")
elif year_now - year_burn in range(2, 5):
  print("Вам " + str(year_now - year_burn) + " года!")
else:
  print("Вам " + str(year_now - year_burn) + " лет!")
