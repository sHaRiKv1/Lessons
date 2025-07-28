#Программа, которая подсчитывает кол-во 0, 1, 2, ..., 9
nums = input("Введите целове число: ")
counts = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

for i in range(len(nums)):
  for j in range(10):
    if int(nums[i]) == j:
      counts[j] += 1
    else:
      continue

print(counts)
