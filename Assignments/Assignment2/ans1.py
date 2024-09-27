months = ['mar', 'jul', 'dec', 'sep', 'apr', 'nov', 'feb', 'may', 'oct', 'aug', 'jun', 'jan']

month_orders = {
    'jan': 1, 'feb': 2, 'mar': 3, 'apr': 4, 'may': 5,
    'jun': 6, 'jul': 7, 'aug': 8, 'sep': 9, 'oct': 10,
    'nov': 11, 'dec': 12
}

sorted_months = sorted(months, key=lambda month: month_orders[month])

print(sorted_months)
