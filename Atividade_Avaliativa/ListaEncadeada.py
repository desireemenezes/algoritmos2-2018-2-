#!/usr/bin/env python
# -*- coding: utf-8 -*-

from No import No

class ListaEncadeada:
    # não passar nenhum agumento para criação de lista vazia
    def __init__(self): 
        self._cabeca = None
        self._rabo = None
        self.size = 0
    
    def __repr__(self):
        """Retorna o objeto em forma de string"""
        return "[" + str(self._cabeca) + " ]"
        return "[" + str(self._rabo) + " ]"
        

    def addInicio(self, e):
        """Insere um valor no início da lista."""
        # Cria um novo objeto do tipo "no" recebendo valor
        novo = No(e)
        if self._cabeca is None:
            self._rabo = novo
        else:
            novo.proximo = self._cabeca
            self._cabeca = novo
        self.size += 1

    
    def addFinal(self, e):
        """Insere elemento no FINAL da lista"""
        if self._cabeca is not None:
            #inserção quando a lista já possui elementos
            ponteiro  =  self._cabeca
            while (ponteiro.proximo):
                pointeiro = ponteiro.proximo
            ponteiro.proximo = No(e)
        else:
            #primeira inserção
            self._cabeca = No(e)
        self.size += 1 #incrementa o valor que já existia no size



    def __len__(self):
        """Retorna o tamanho da lista"""
        return self.size

    @property
    def primeiro(self):
        """Retorna o primeiro elemento da lista."""
        return self._cabeca

    @property
    def ultimo(self):
        """Retorna o ultimo elemento da lista."""
        return self._rabo


 

lista = ListaEncadeada()
lista.addFinal(8)
lista.addFinal(9)
lista.addInicio(10)
print("lista {}".format(lista))
print("tamanho da lista {}".format(lista.size))
print("primeiro elemento {}".format(lista.primeiro.dado))
print("umtimo elemento {}".format(lista.ultimo.dado))