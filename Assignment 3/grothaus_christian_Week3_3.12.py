num = int(input('Enter a five digit number: '))
firstNumber = num // 10000
secondNumber = num // 1000 % 10
thirdNumber = num // 100 % 10
fourthNumber = num // 10 % 10
fifthNumber = num % 10

if firstNumber == fifthNumber and secondNumber == fourthNumber:
  print('The number is a palindrome.')
else:
  print('The number is not a palindrome')