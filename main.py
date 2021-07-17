print('=-=-=-= Bem-vindo ao Caixa Eletrônico =-=-=-=')
print('Tenho cédulas de R$100, R$50, R$20, R$10 e R$5')
valor = float(input('Qual valor deseja sacar: R$ '))
while (valor % 5) != 0:
    print('Não é possível sacar este valor!')
    valor = float(input('Qual valor deseja sacar: R$ '))
else:
    print('Certo, lhe entregarei:')
    if valor >= 100:
        val100 = int(valor/100)
        valor = valor - (val100*100)
        print('{} cédula(s) de R$100'.format(str(val100)))
    if valor >= 50 and valor < 100:
        val50 = int(valor/50)
        valor = valor - (val50*50)
        print('{} cédula(s) de R$50'.format(str(val50)))
    if valor >= 20 and valor < 50:
        val20 = int(valor/20)
        valor = valor - (val20*20)
        print('{} cédula(s) de R$20'.format(str(val20)))
    if valor >= 10 and valor < 20:
        val10 = int(valor/10)
        valor = valor - (val10*10)
        print('{} cédula(s) de R$10'.format(str(val10)))
    if valor >= 5 and valor < 10:
        val5 = int(valor/5)
        valor = valor - (val5*100)
        print('{} cédula(s) de R$5'.format(str(val5)))
