import ru_local as ru

category = int(input(f'{ru.CATEGORY}'))
tax_rates = [10, 15, 25, 28, 33, 35, 39.6]

print(ru.INCOMES_TITLE)
incomes = []
for month in range(12):
    incomes.append(float(input(f'{ru.INCOME}{ru.IN_MONTH[month]} [USD]: ')))
gross_income = sum(incomes)
print(f'{ru.GROSS_INCOME}{gross_income}')

print(ru.BENEFITS_TITLE)
benefits = []
for month in range(12):
    benefits.append(float(input(f'{ru.BENEFIT}{ru.IN_MONTH[month]} [USD]: ')))
total_benefit = sum(benefits)
print(f'{ru.TOTAL_BENEFIT}{total_benefit}')

tax_bases = []
for month in range(12):
    tax_bases.append(incomes[month] - benefits[month])
tax_base = sum(tax_bases)
print(f'{ru.TAXED_INCOME}{tax_base}')


def total_tax(bottom_limits):
    amount = 0
    for income in incomes:
        for n in range(7):
            if n + 1 < 6 and bottom_limits[n] <= income < bottom_limits[n + 1]:
                amount += income * tax_rates[n] * 0.01
                break
            else:
                amount += incomes[i] * tax_rates[-1] * 0.01
    return amount


single_subject = [0, 9076, 36901, 89351, 186351, 405101, 406751]
married_couple = [0, 18151, 73801, 148851, 226851, 405101, 457601]
single_parent = [0, 12951, 49401, 127551, 206601, 405101, 432201]

match category:
    case 1:
        tax = total_tax(single_subject)
    case 2:
        tax = total_tax(married_couple)
    case 3:
        tax = total_tax(single_parent)

print(f'{ru.ANNUAL_TAX}{tax}')
print(f'{ru.MONTH_PAYMENT}{tax / 12}')
