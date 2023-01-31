altura = float(input('Qual altura? '))

if altura < 0.3:
	print ('Essa tomada é baixa')

elif altura > 0.3 and altura < 1.8:
	print('Essa tomada é média')

else:
	print('Essa tomada é alta')

input()