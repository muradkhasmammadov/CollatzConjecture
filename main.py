n = int(input(str("Enter the number: ")))
result = 0
numbers = []
while n != 1:
  if n%2 == 0:
    n = n/2
  else:
    n = (3 * n) + 1
  result += 1
  numbers.append(n)
  print("#", result, "->", n)
  
print("Total stopping time:", result)
print("Highest number reached:", max(numbers))