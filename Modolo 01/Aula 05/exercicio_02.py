accounts = [0.12, 0.90, 0.89, 0.076, -0.0087, 0.78, 0.65]
percentage_accounts = []

for valor in accounts:
    percentage_accounts.append(f'{valor: .2%}')

print(*percentage_accounts, sep=', ')