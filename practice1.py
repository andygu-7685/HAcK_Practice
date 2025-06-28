import math
print("Hello World")
def mean(input):
  sum = 0
  for entry in input:
    sum += entry
  return sum / len(input)

my_list = [0, 1, 2, 3, 4, 5]
print(mean(my_list))


def median(input):
  isOdd = len(input) % 2
  half = len(input) // 2
  if isOdd:
    return input[half]
  else:
    return (input[half] + input[half - 1]) / 2

my_list = [0, 1, 2, 6, 4, 9]
print(median(my_list))