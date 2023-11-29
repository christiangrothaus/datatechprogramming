numbers = list(range(1, 11))

evenNumbersFunc = list(filter(lambda num: num % 2 == 0, numbers))
triplesFunc = list(map(lambda num: num ** 3, evenNumbersFunc))
print(sum(triplesFunc))

evenNumbers = [num for num in numbers if num % 2 == 0]
triples = [num ** 3 for num in evenNumbers]
print(sum(triples))