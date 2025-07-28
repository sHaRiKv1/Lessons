#Функция по формированию кортежа из цифр числа
#введённого пользователем (в прямом или обратном порядке)
number = int(input("Введите целое число: "))
rev = str(input("Хотите вывести кортеж в прямом (y) или обратном (n) порядке?\n"))

def make_kort(num, vib):
  list = []
  while num > 0:
      list.insert(0, num % 10)
      num //= 10
  if vib == "y":
    pass
  else:
    list = reversed(list)
  return tuple(list)

print(make_kort(number, rev))
