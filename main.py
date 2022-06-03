__author__ = 'Samuel Assis'

a = int(input('\nColoque um número: '))
print('---------------------------')
b = int(input('\nColoque outro número: '))
print('---------------------------')
c = a + b
print('\nA soma deles é: ',c)
print('---------------------------')
print('\n\n...........................\n\n')

print('~~~~~Aumento Anual de Salário~~~~~')
sal = float(input('\nInsira o seu salário atual: ').replace(',','.'))
print('---------------------------------------------')

novosal = sal * 1.5
print('\nO seu salário daqui um ano será de R$ %.2f'%novosal)
print('---------------------------------------------')
print('\n\n...........................\n\n')

