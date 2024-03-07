category = int(input())
month_name = [range(12)]

income = []
for month in range(12):
    income.append(float(input()))
gross_income = sum(income)

benefit = []
for month in range(12):
    benefit.append(float(input()))
total_benefit = sum(benefit)

tax_base = []
for month in range(12):
    tax_base.append(income[month] - benefit[month])

tax_rate = [10, 15, 25, 28, 33, 35, 39.6]

def total_tax(bottom_limits):
    amount = 0
    for j in range(12:
        for i in range(len(bottom_limits)):
            if i+1 in range(len(bottom_limits)) and bottom_limits[i] <= tax_base[j] < bottom_limits[i+1]:
                amount += (tax_base[j] - bottom_limits[i]) * tax_rate[i] * 0.01
            else:
                amount += (tax_base[j] - bottom_limits[i]) * tax_rate[-1] * 0.01

    return amount

def single_subject():
    bottom_limits = [0, 9076, 36901, 89351, 186351, 405101, 406751]
    total_tax(bottom_limits)

if category in range(1, 4):
    if category == 1:
        single_subject()
    elif category == 2:
        married_couple()
    else:
        single_parent()
print(taxed_amount)
print(non_taxed_amount)
print(annual_tax)
