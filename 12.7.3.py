per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
a=per_cent.values()
money=int(input("Введите сумму"))
c=([i*money for i in a])
c=list(map(int,c))
print("deposit", c)
print("Максимальная сумма, которую вы можете заработать —", max(c))


