#Программа для выявления арифметической прогрессии
list_nums = sorted(list(eval(input("Введите три числа через запятую: "))), reverse=True)

if list_nums[0] - list_nums[1] == list_nums[1] - list_nums[2]:
  print("Это арифметическая последовательность")
else:
  print("Это не арифметическая последовательность")
