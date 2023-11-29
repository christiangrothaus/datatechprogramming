from decimal import Decimal

gallonsUsed = 0
count = 0
totalMiles = 0
totalGallons= 0

while gallonsUsed != -1:
  gallonsUsed = float(input('Enter the gallons used (-1 to end): '))
  if gallonsUsed == -1:
    continue
  miles = float(input('Enter the miles driven: '))
  mpg = miles / gallonsUsed
  count += 1
  totalMiles += miles
  totalGallons += gallonsUsed
  print(f'The miles/gallon for this tank was {mpg}')

averageMpg = totalMiles / totalGallons
print(f'The overall average miles/gallon was {averageMpg}')