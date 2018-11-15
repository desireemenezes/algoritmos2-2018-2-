#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Pilha:
    def __init__(self):
        self.itens = []
    
    def vazia(self):
        return self.itens == []

    #método topo retorna o elemento, o total da minha lista -1
    def topo(self):
        return self.intens[len(self.itens)-1]

    def tamanho(self):
        return len(self.itens)
    
    def empilha(self, el):
        self.itens.append(el)
    
    def desemplinha(self):
        return self.itens.pop()
                    

pilha = Pilha()
pilha.empilha('prato')
pilha.empilha('garfo')
pilha.empilha('faca')
print(pilha.tamanho())
        
