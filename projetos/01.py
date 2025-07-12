# Age calculator
# This program calculates a person's age
# based on the date of birth and the current date
# import datetime

from datetime import datetime

data_atual = datetime.today()
data_nasc = input('Digite sua data de nascimento (dd/mm/aaaa): ')
data_nasc = datetime.strptime(data_nasc, '%d/%m/%Y')
data_dif = data_atual - data_nasc
idade = data_dif.days // 365

print('Sua idade é:', idade, 'anos')
print('Obrigado por usar a calculadora de idade!!!')
print('Até a próxima!')
print('---')
print('Versão 1.0')
print('Desenvolvido por: Cardoso Welington')
print('Data: 12/07/2025')
print('---')