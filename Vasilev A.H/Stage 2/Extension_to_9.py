#Программа для смены цифр в числе на дополнение до 9. 0-9, 1-8, 2-7, ..., 9-0
nums = input("Введите целое число: ")
nums_new = ''

for i in range(len(nums)):
  nums_new += str(9 - int(nums[i]))  

print(nums_new)
