 
# função recursiva para calcular o fatorial de um número
def fatorial(num):
  if num <= 1:
    return 1
  else:
    return num * fatorial(num - 1)
 
# função principal do programa
