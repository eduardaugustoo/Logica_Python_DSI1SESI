# AULA COMPLETA: NUMEROS EM PYTHON
"""
Vamos aprender:
1 - Tipos numéricos 
2 - Conversões de tipos 
3 - Hieraequia numérica 
4 - Operações matemática
5 - Coerção de tipos 
6 - Verificação de tipos 
7 - Entrada de dados 
"""
# PASSO 01 - TIPOS NUMÉRICOS 
# int -> números Inteiros 
# float -> números com casa decimais 
# complex -> numeros complexos (usado em matemática/engenharia ) 

print ("===== TIPOS NUMÉRICOS =====")

# EXEMPLO 01 - NUMERO INTEIRO 

# criamos uma variavel chamada numero_inteiro 
numero_intero = 10

# mostramos o valor 
print ("Valor:",  numero_intero)

# Type () mostra qual é o tipo da variável
print ("tipo:", type (numero_inteiro))

print ("---------------")

# EXEMPLO 02 - NUMERO DECIMAL
 
#  float é um numero com ponto decimal
numero_decimal = 3.14

print ("valor:", numero_decimal)
print ("tipo:", type (numero_decimal))

print ("---------------")

# EXEMPLO 03 - NUMEROS COMPLEXOS 
# Um número complexo possui duas partes:
# Parte real (numero normal)
# Parte Imaginária (multiplicada por j)

# Estrutura Geral:
# numero = a + bj

# a = parte real
# b = parte imaginária 
# j = uniidade imaginária

numero_complexo = 2 + 3j
print ("valor:", numero_complexo)
print (tipo:), type (numero_complexo)

print ("---------------")
