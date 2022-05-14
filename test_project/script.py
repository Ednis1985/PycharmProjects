per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
money = int(input('Enter integer '))
x = list(per_cent.values())
tbk = round((float(x[0]) / 100) * money)
skb = round((float(x[1]) / 100) * money)
vtb = round((float(x[2]) / 100) * money)
sber = round((float(x[3]) / 100) * money)

print('Накопление за год в банке ТКБ -', (tbk))
print('Накопление за год в банке СКБ -', (skb))
print('Накопление за год в банке ВТБ -', (vtb))
print('Накопление за год в банке СБЕР -', round(sber))

deposit = list({tbk, skb, vtb, sber})
print(deposit)


max_number = max(deposit)
print("Максимальная сумма, которую вы можете заработать -", max_number)