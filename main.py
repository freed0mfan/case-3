def main():
    #Case-study #3
    #Creators: Markelov E.,
    #          Sokolova S.,
    #          Kosheleva A.,
    #          Rusakova M.
    #
    # Description: This program calculates the amount of tax to be paid
    # depending on a taxpayer's monthly incomes. It's based on a progressive
    # taxation scale being used in the US. It also considers all the benefits the subject got.

    import ru_local as ru

    category = int(input(f'{ru.CATEGORY}'))
    tax_rates = [10, 15, 25, 28, 33, 35, 39.6]

    # Here we ask a user about their incomes.
    print(ru.INCOMES_TITLE)
    incomes = []
    for month in range(12):
        incomes.append(float(input(f'{ru.INCOME}{ru.IN_MONTH[month]} [USD]: ')))
    gross_income = sum(incomes)
    print(f'{ru.GROSS_INCOME}{round(gross_income, 2)}')

    # Here we ask them about benefits.
    print(ru.BENEFITS_TITLE)
    benefits = []
    for month in range(12):
        benefits.append(float(input(f'{ru.BENEFIT}{ru.IN_MONTH[month]} [USD]: ')))
    total_benefit = sum(benefits)
    print(f'{ru.TOTAL_BENEFIT}{round(total_benefit, 2)}')

    # Here we calculate their tax bases for each month.
    tax_bases = []
    for month in range(12):
        tax_bases.append(incomes[month] - benefits[month])
    tax_base = sum(tax_bases)
    print(f'{ru.TAXED_INCOME}{round(tax_base, 2)}')


    def total_tax(bottom_limits):
        '''
            This function calculates total amount of annual tax to be paid
        depending on the list of bottom limits of income ranges in which different
        tax rates are used for a certain category of taxpayers.

        :param bottom_limits: bottom limits of income ranges in which different
        tax rates are used for a certain category of taxpayers
        :return: amount of annual tax to be paid
        '''
        amount = 0
        for income in incomes:
            for n in range(7):
                if n + 1 < 6 and bottom_limits[n] <= income < bottom_limits[n + 1]:
                    amount += income * tax_rates[n] * 0.01
                    break
                else:
                    amount += income * tax_rates[-1] * 0.01
        return amount


    # Bottom limits for 3 categories according to the name of a list
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
    print(f'{ru.AVG_MONTH_PAYMENT}{tax / 12}')


if __name__ == '__main__':
    main()