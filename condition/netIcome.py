def calcNetIncome(state, income):
    stateTax = {"NY":10, "NJ":20, "CA": 30}
    fedTax = 10
    if state in stateTax:
        netIncome = income - (income*fedTax/100) - (income*stateTax[state]/100)
        return netIncome
    else:
        return("State is not valid")

print(calcNetIncome("NY",100000))

