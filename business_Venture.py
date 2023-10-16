
## A local business venture capitalist wants you to write a program that they can use to conduct a cost benefit analysis of any given new business startup, to determine the capital investment, operational expenditures, unit costs, sales volume, and calculate the monthly profit or loss based on user input.  This software tool will then be used by the venture capitalist to compare different businesses to determine which business would provide the greatest return on investment.

# Module 1: Initial Capital Investment

initialCapitalInvestment = float(input("Enter amount of initial Capital Investment: $ "))
print("")
# Module 2: Monthly Location Expenditures

locationLeaseCosts = float(input("Enter the Monthly Location Lease Costs: $"))
locationUtilitiesCosts = float(input("Enter the Monthly Location Utilities Costs: $"))
monthlyLocationExpenditures = locationLeaseCosts + locationUtilitiesCosts

print("The projected Monthly Loation Expenditures = ${0:,.2f}".format(monthlyLocationExpenditures),)
print("")
# Module 3: Monthly Employeee Expenditures

employees = int(input("How many employees do you have:"))
payrate = float(input("What is their hourly pay rate: $"))
hours = float(input("How many hours a week do they work: "))
monthlyEmployeeExpenditures = ((employees * payrate * hours) * 52) / 12

print("The projected Monthly Employee Expenditures = ${0:,.2f}".format(monthlyEmployeeExpenditures))
print("")
# Module 4: Monthly Operational Expenditures
monthlyOperationalExpenditures = monthlyLocationExpenditures + monthlyEmployeeExpenditures

print("The Monthly Operational Expenditures = ${0:,.2f}".format(monthlyOperationalExpenditures),)
print("")
# Module 5: Monthly Uit Sales Volume

numberOfProducts = int(input("How many products do you sell: "))
unitSalesVolume = 0
for i in range(numberOfProducts):
    product = input("What is product {}: ".format(i + 1))
    unitCost = float(input("\tUnit Cost: $"))
    unitSalesPrice = float(input("\tUnit Sales Price: $"))
    unitsSoldAMonth = int(input("\tUnits Sold a Month: "))
    salesVolume = (unitSalesPrice * unitsSoldAMonth) - (unitCost * unitsSoldAMonth)

    print("\tThe projected Monthly", product, "Sales Volume = ${0:,.2f}".format(salesVolume))
    unitSalesVolume += salesVolume

print("The total Monthly Unit Sales Volume = ${0:,.2f}".format(unitSalesVolume))
print("")  
# Module 6: Profit or Loss Summary
coverage = initialCapitalInvestment / monthlyOperationalExpenditures

print("The Capital Investment of ${0:,.2f}".format(initialCapitalInvestment),"will cover", round(coverage),"months of Operational Expenditures.")
totalMonthlyUnitSales = unitSalesVolume * coverage

print("The Total Mothly Unit Sales will generate ${0:,.2f}".format(totalMonthlyUnitSales), "in", round(coverage), "months.")
businessVenture = totalMonthlyUnitSales - initialCapitalInvestment
if businessVenture < 0:
    print("This business venture will generate ${0:,.2f}".format(businessVenture), "in LOSS in", round(coverage), "months.")
else:
    print("This business venture will generate ${0:,.2f}".format(businessVenture), "in GAIN in", round(coverage), "months.")

