#Функция выводящая сумму нечётных чисел в ведённом диапазоне
number = 10

def sum_nechet(count):
  summa = sum(list(2 * i + 1 for i in range(count + 1)))
  return summa

print(sum_nechet(number))