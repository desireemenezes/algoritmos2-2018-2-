#!/usr/bin/env python
# -*- coding: utf-8 -*-

class No:
    def __init__(self, dado):
        self.dado = dado
        self.proximo = None
    def __repr__(self):
        return '%s -> %s' % (self.dado, self.proximo)

class ListaEncadeada:
    """Esta classe representa uma lista encadeada."""
    def __init__(self): 
        self.cabeca = None
        self.rabo = None
        self._size = 0

    def __repr__(self):
        return "[" + str(self.cabeca) + " ]"
        

    def addFirst(self, novo_dado):
        # 1) Cria um novo no com o dado a ser armazenado.
        novo_no = No(novo_dado)
        # 2) Faz com que o novo no seja a cabeca da lista.
        novo_no.proximo = self.cabeca
        # 3) Faz com que a cabeca da lista referencie o novo no.
        self.cabeca = novo_no

    def addLast(self, elem):
        if self.cabeca:
            # o ponteiro esta apontando para o mesmo espaco de memoria 
            ponteiro = self.cabeca
            # enquanto tiver proximo eu percorro ate chegar no ultimo
            while(ponteiro.proximo):
                ponteiro = ponteiro.proximo
            ponteiro.proximo = No(elem)   
        else:# se a lista não tiveritens add adcionar
            #primeira insercao
           self.cabeca = No(elem)
        self._size += 1
        
    
    def removeFirst(self):
        assert self.cabeca 
        """ assert é uma verificação em tempo de execução de uma condição qualquer. 
            Se a condição não for verdadeira, uma exceção AssertionError acontece e o programa pára.7
            *** Impossível remover valor de lista vazia. *** """
        self.cabeca = self.cabeca.proximo
        self._size -= 1
        

        
lista = ListaEncadeada()
print("Lista vazia:{}" .format(lista))

lista.addFirst(10)
print("Inserindo um novo elemento na primeira posição da lista:{}" .format(lista))

lista.addFirst(5)
print("Inserindo um novo elemento na primeira posição da lista:{}" .format(lista))

lista.addFirst(8)
print("Inserindo um novo elemento na primeira posição da lista:{}" .format(lista))

lista.addLast(12)
print("Adicionando no último elemento da lista:{}" .format(lista))

lista.removeFirst()
print("Removendo o primeiro elemento da lista:{}" .format(lista))

#lista.removeLast()
#print("Removendo o último elemento da lista:{}".format(lista))








