def getInvestmentReturn(n):
    return 1000 * (1 + 0.07) ** n

years = [10, 20, 30]

for year in years:
    print(getInvestmentReturn(year))