# input statements
salary = float(input("Please enter salary: "))
numDependents = float(input("Please enter number of dependents: "))

# calculate taxes here
stateTax=(salary * 0.065)
federalTax=(salary * 0.28)
dependentDeduction=((salary * 0.025) * (numDependents))
totalWithholding=(stateTax + federalTax + dependentDeduction)
takeHomePay=(salary - totalWithholding)

# output statements
print("State Tax: $" + str(stateTax))
print("Federal Tax: $" + str(federalTax))
print("Dependents: $" + str(dependentDeduction))
print("Salary: $" + str(salary))
print("Take Home Pay: $" + str(takeHomePay))