# amount = float(input('usd = '))

# print('usd {0} = {1} bgn'.format(amount, round(amount*1.79549,2)))

#currency
bgn = float(input('bgn = '))
usd = 1.79549
eur = 1.95583
gbp = 2.53405

#the calculator 
a = bgn/usd
b = bgn/eur
c = bgn/gbp

#output
print('usd =',round(a,2))
print('eur =',round(b,2))
print('gbp =',round(c,2))