# Challenge 14: Write a program that converts a temperature entered in Celsius to Fahrenheit.
num = float(input('Digite a temperatura em graus celsius: '))
fah = (num * 9/5) + 32
print('A temperatura de {} graus celsius corresponde a {:.2f} graus fahrenheit.'.format(num, fah))