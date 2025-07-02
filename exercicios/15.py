# Challenge 15: Write a program that asks for the number of KM traveled by a rented car and the number of days it was rented. Calculate the price to pay, knowing that the car costs R$60 per day and R$0,15 per KM driven.
qtd_km = float(input('Digite a quantidade de km percorridos: '))
qtd_days = int(input('Digite a quantidade de dias que o carro foi alugado: '))
price_day = 60.0
price_km = 0.15
total_price = ((qtd_days * price_day) + (qtd_km * price_km))
print('O total a pagar é de R${:.2f}'.format(total_price))