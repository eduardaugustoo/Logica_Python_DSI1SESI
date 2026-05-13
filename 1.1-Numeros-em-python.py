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
print ("type:") , type (numero_complexo)

print ("---------------")

# EXEMPLO 03 - ACESSANDO CADA PARTE DO NÚMERO

# .real retorna a parte real
print ("Parte Real:" , numero_complexo.real)

# .imag retorna a parte imaginária 
print ("Parte imaginária:" , numero_complexo.imag)
 
 #apenas para separar visualmente a saída no terimal
# print ("\n\n")

## PASSO 02 - CONVERSÃO TIPOS

## Exemplo Clássico:
## Dados vindos do usuário são texto (string) , muitas vezes é necessario converter eles.

print ("===== Conversões =====")

# float -> int
valor = int (3.9)

print ("int(3.9):", valor)
print ( "tipo:", type (valor))
 
 #String -> int
valor1 = "10"
print (type(valor1))
print ("int( valor1):", int (valor1))
print ("tipo:", type (int(valor1)))

valor2 = int ("10")
print ('int(10):',valor2)
print ("tipo", type (valor2))

#int --> float
valor3 = float (10)
print ("float(10):", valor3)
print ("tipo:", type(valor3))

    