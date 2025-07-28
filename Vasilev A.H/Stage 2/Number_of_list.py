#Программа, которая составляет одно число из списка натуральных чисел
start_list = [12, 3, 456, 78]
string = ""

for i in range(len(start_list)):
  string += str(start_list[i])

print(string)
