import math
print("Hello World")
def median(input):
  isOdd = len(input) % 2
  half = len(input) // 2
  if isOdd:
    return input[half]
  else:
    return (input[half] + input[half - 1]) / 2

my_list = [0, 1, 2, 6, 4, 9]
print(median(my_list))