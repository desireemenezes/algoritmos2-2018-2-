#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" O último elemento inserido é o primeiro a ser removido (LIFO) """

#importante saber inserir da pilha
#importante saber remover da pilha
#observar o valor do topo

class Node:
    def __init__(self, dado):
        self.dado = dado
        self.next = None

class Stack:
    def __init__(self): #construtor tem um topo vazio e o tamanho da lista = 0
        self.top = None
        self._size = 0

    def push(self, elem):
        #insere um elemento na pilha
        node = Node(elem)
        node.next = self.top #quem esta abaixo vai ser o antigo topo
        self.top = node
        self._size += 1

    def pop(self):
        #remove o elemento do topo da pilha
        if self._size > 0:
            node = self.top
            self.top = self.top.next
            #tem que reduzir o tamanho da pilha
            self._size -= 1
            return node
        raise IndexError("a pilha esta vazia")
    
    def peek(self):
        #retorna o topo sem remover
        if self._size > 0:
            return self.top.dado
        raise IndexError("a pilha esta vazia")

        
    
    def __len__(self):
        """Retorna o tamanho da lista"""
        return self._size

    def __repr__(self): #representação do objeto
        r = ""
        aux = self.top
        while(aux):
            r = r + str(aux.dado) + "\n"
            aux = aux.next
        return r
    
    def __str__(self): #representa como string
        return self.__repr__()

pilha = Stack()
print(len(pilha))
pilha.push(3)
pilha.push(7)
pilha.push('python')
pilha.push(True)
print(pilha)
pilha.peek()
pilha.pop()
print(pilha)
pilha.pop()
print(pilha)
