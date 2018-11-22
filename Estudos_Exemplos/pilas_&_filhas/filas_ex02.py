#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" SIMULAÇÃO DE FILA ATRAVÉS DE LISTAS """
""" Na fila só remove no inicio e só insere no final """

class Node:
    def __init__(self, dado):
        self.dado = dado
        self.next = None

class Queue:
    def __init__(self): #construtor tem um 
        self.comeco = None # no começo eu quero remover
        self.final = None  # no final eu quero inserir
        self._size = 0

    def push(self, elem):
        #inserir na pilha (ultimo elemneto)
        node = Node(elem)
        if self.final is None:
            self.final = node
        else: # o ultimo tem que saber que alguem chegou atrás dele
            self.final.next = node
            self.final = node 
        #tratar tambem se o primeiro elemento é vazio 
        if self.comeco is None:
            self.comeco = node
        
        self._size += 1

    def pop(self):
        #remover só da posição inicial
        # if self._size > 0:
        if self.comeco is not None:
            elem = self.comeco.dado
            self.comeco =  self.comeco.next
            self._size -= 1
            return elem
        
        raise IndexError("A fila esta vazia")
        
    
    def peek(self):
         #remover só da posição inicial
        # if self._size > 0:
        if self.comeco is not None:
            elem = self.comeco.dado
            return elem
        
        raise IndexError("A fila esta vazia")
        
    
    def __len__(self):
        """Retorna o tamanho da lista"""
        return self._size

    def __repr__(self): #representação do objeto
        r = ""
        aux = self.comeco
        while(aux):
            r = r + str(aux.dado) + " "
            aux = aux.next
        return r
    
    def __str__(self): #representa como string
        return self.__repr__()
    
fila = Queue()
fila.push(5)
fila.push(11)
fila.push(9)
fila.push(10)
print(fila)
fila.pop()
fila.peek()
print(fila)
