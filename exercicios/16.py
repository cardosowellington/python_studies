# challenge 16: Create a program that reads any real number from the keyboard and shows its integer part on tthe screen.
import math
num = float(input('Digite um número real: '))
print('A porção inteira de {} é {}'.format(num, math.trunc(num)))