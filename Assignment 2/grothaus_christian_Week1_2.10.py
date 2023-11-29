from math import prod 

numOne = int(input('Number 1: '))
numTwo = int(input('Number 2: '))
numThree = int(input('Number 3: '))

numbers = [numOne, numTwo, numThree]

print("Sum:", sum(numbers))
print('Average:', sum(numbers) / len(numbers))
print('Product:', prod(numbers))
print('Smallest Integer:', min(numbers))
print('Largest Integer:', max(numbers))