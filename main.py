print(ru.INCOMES_TITLE)
incomes = []
for month in range(12):
    incomes.append(float(input(f'{ru.INCOME}{ru.IN_MONTH[month]} [USD]: ')))
gross_income = sum(incomes)
print(f'{ru.GROSS_INCOME}{round(gross_income, 2)}')