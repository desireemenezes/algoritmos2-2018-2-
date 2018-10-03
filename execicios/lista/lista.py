#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Leia dez números inseridos pelo usuário e responda:

- Qual o maior número e qual o seu índice?

- Qual o menor número e qual o seu índice?

- Qual a soma dos números pares?

- Qual a soma dos números ímpares?

- Qual a soma da divisão dos números de índice par, pelos números de índice ímpar?

- Imprima os números na ordem inversa em que foram digitados.
"""

#append método para add elementos dentro de uma lista
#para saber o maior numro de uma lista pode-se ultilizar o metodo sum() também decidi ultilizar o for

print("############################################")
print("Digite 10 números para realiizar os calculos! ")
print("\n")

lista = []
lista_pares = []
lista_impares = []
count = 0



while count < 5:
    numero = int(input("Digite um número:"))
    if numero == 0:
        print("ZERO É INVÁLIDO!!")
        break
    count = count + 1
    lista.append(numero)
    print("\n")

    if numero % 2 == 0:
        lista_pares.append(numero)
    else:
        lista_impares.append(numero)
        

def check_maior():
    maior_numero = lista[0]
    for lista_numero_maior in lista:
        if lista_numero_maior > maior_numero:
            maior_numero = lista_numero_maior
        
    posicao_maior = lista.index(maior_numero)
    print("O maior numero digitado é: {}, indice:[{}]".format(maior_numero, posicao_maior))
    return maior_numero;

def check_menor():
    menor_numero = lista[0]
    for lista_numero_menor in lista:
        if lista_numero_menor < menor_numero:
            menor_numero = lista_numero_menor

    posicao_menor = lista.index(menor_numero)
    print("O menor numero digitado é: {}, indice:[{}]".format(menor_numero, posicao_menor))

def check_pares(): 
    soma_par = 0
    for numero in lista_pares :
        soma_par += numero 
    print("Soma dos números pares é: {}" .format(soma_par))

def check_impares():    
    soma_impar = 0
    for numero in lista_impares :
        soma_impar += numero
    print("Soma dos números impares é: {}" .format(soma_impar))
    return soma_impar
 

def calc_soma():
    soma_impar = 0
    for numero in lista_impares :
        soma_impar += numero

    soma_par = 0
    for numero in lista_pares :
        soma_par += numero 

    calc = soma_par // soma_impar
    print("A soma da divisão de número pares por impares é = {}".format(calc))
    
    
check_maior()
check_menor()
check_pares()
check_impares() 
calc_soma()

#print(lista.reverse())

#print("Pares: {}" .format(lista_pares))
#print("Impares: {}" .format(lista_impares))

"""
teste com for
for num in lista:
    print(num)
"""



