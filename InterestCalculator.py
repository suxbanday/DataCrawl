#interest calculator

principle = input('Please enter principle\n>>')
interestRate = input('Please enter the annual interest rate (example 5.2 for 5.2%)\n>>')
years = input('Please enter the term in years\n>>')
times = input('Please enter number of times the interest will compound per year\n>>')
principleFloat = float(principle)
interestRateFloat = float(interestRate)/100
yearsFloat = float(years)
timesFloat = float(times)
nt = timesFloat*yearsFloat
futureValue = principleFloat*((1+(interestRateFloat/timesFloat))**nt)
print('In', years, 'years,','at the interest rate of','{}%'.format(interestRate),\
      'compounded',times,'times per year,','the initial amount of','${0:,.2f}'.format(principleFloat),\
      'will be worth','${0:,.2f}'.format(futureValue)+'.')

