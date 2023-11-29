number = int(input('Enter a non-negative number: '))
while number < 0:
  number = int(input('Enter a non-negative number: '))
factorial = number
if number == 0:
  factorial = 1
count = 1
while number - count != 0 and number:
  factorial *= number - count
  count += 1
print(factorial)