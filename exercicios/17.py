# Challenge 17: Create a program that reads the lengths of the opposite and adjacent sides of a right triangle, calculates, and displays the length of the hypotenuse.
import math
def calc_hipotenusa(cat1, cat2):
  hipotenusa = math.sqrt(cat1**2 + cat2**2)
  return hipotenusa
cat_oposto = float(input('Digite o comprimento do cateto oposto: '))
cat_adjacente = float(input('Digite o comprimento do cateto adjacente: '))
hipotenusa = calc_hipotenusa(cat_oposto, cat_adjacente)
print('O comprimento da hipotenusa é: {:.2f}'.format(hipotenusa))