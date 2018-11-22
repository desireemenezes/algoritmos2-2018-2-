#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Pilha(object):
    
    def __init__(self):
        self.dados = []
    
    def __repr__(self):
        return str(self.dados) 
 
    def empilha(self, elemento):
        self.dados.append(elemento)
        
    def desempilha(self):
        return self.dados.pop(-1)
         #return self.dados.pop(len(dados)-1)
        #Ou então, podemos usar self.dados.pop(-1). O acesso ao índice -1é a forma pythônica de se referir ao último elemento de uma sequência.
        
    def vazia(self):
        return len(self.dados) == 0

pilha = Pilha()
pilha.empilha(4)
pilha.empilha(5)
pilha.empilha(6)
pilha.desempilha()
print(pilha)