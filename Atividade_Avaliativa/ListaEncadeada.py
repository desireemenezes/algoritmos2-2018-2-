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
        

    def addInicio(self, e):
        """Insere um valor no início da lista."""
        # Cria um novo objeto do tipo "no" recebendo valor
        novo = No(e)
        if self._cabeca is None:
            self._rabo = novo
        else:
            novo.proximo = self._cabeca
            self._cabeca = novo
        self.size += 1 #incrementa o valor que já existia no size

  
    def addFinal(self, e):
        """Insere elemento no FINAL da lista"""
        if self._rabo is None:
            self._cabeca = self._rabo = No(e)
        else:
            self._rabo.proximo = No(e)
            self._rabo = self._rabo.proximo
        self.size += 1 # incrementa o valor que já existia no size


    def buscaIndice(self, e):
        aux = self._cabeca
        cont = 0
        while aux is not None:
            if (cont % 4) == 0:
                print(aux)
            cont += 1
            aux = aux.proximo
    
    def __str__(self):
        aux = self._cabeca
        texto = "Lista: \n"
        while aux is not None:
            texto += str(aux)+"\n"
            aux = aux.proximo
        return texto



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
lista.addInicio(10)
lista.addFinal(9)
lista.addFinal(11)
lista.addFinal(112)
lista.addFinal(13)
lista.addInicio(55)
lista.buscaIndice(3)
print("lista {}".format(lista))
print("tamanho da lista {}".format(lista.size))
print("primeiro elemento {}".format(lista.primeiro.dado))
print("umtimo elemento {}".format(lista.ultimo.dado))
print("busca por indice {}".format(lista))
