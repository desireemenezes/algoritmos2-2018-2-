#!/usr/bin/env python
# -*- coding: utf-8 -*-

from No import No

class ListaEncadeada:
    # não passar nenhum agumento para criação de lista vazia
    def __init__(self): 
        self._cabeca = None
        self._rabo = None
        self.size = 0
        self.index = 0

    def dado(self):
        """Retorna o valor do no."""
        return self.dado
    
    def __repr__(self):
        """Retorna o objeto em forma de string"""
        return "[" + str(self._cabeca) + " ]"
        

    def addInicio(self, e):
        """Insere um valor no início da lista."""
        # Cria um novo objeto do tipo "no" recebendo valor
        self.indice = None  # eu digo que o indice é vaziu e insiro na lista no inicio da listaencadeada
        novo = No(e)
        if self._cabeca is None:
            self._rabo = novo
        else:
            novo.proximo = self._cabeca
            self._cabeca = novo
        self.size += 1 #incrementa o valor que já existia no size

    def removeInicio(self):
        """Remove o primeiro elemento da lista."""
        if self._cabeca is None: #verifica se a cabeca esta vazia se estive retorn none
            return None
        if self._cabeca is self._rabo: 
            self._cabeca = self._rabo = None
        else:
            self._cabeca = self._cabeca.proximo
        self.size -= 1

  
    def addFinal(self, e):
        """Insere elemento no FINAL da lista"""
        self.indice = None  # eu digo que o indice é vaziu e insiro na lista no inicio da listaencadeada
        if self._rabo is None:
            self._cabeca = self._rabo = No(e)
        else:
            self._rabo.proximo = No(e)
            self._rabo = self._rabo.proximo
        self.size += 1 # incrementa o valor que já existia no size

    def removeFinal(self):
        """Remove o ultimo elemento da lista e o retorna."""
        if self._rabo is None:
            return None
        dado = self._rabo.dado 
        if self._cabeca is self._rabo:
            self._cabeca  = self._rabo = None
        else:
            aux = self._cabeca
            while aux.proximo is not self._rabo:
                aux = aux.proximo
            aux.poximo = None
            self._rabo = aux
        self.size -= 1
        return dado


    def buscaIndexada(self, e): #pulando 5
        aux = self._cabeca
        cont = 0
        while aux is not None:
            if (cont % 5) == 0:
                print(aux)
            cont += 1
            aux = aux.proximo

    #    """ Retorna o indice do elemento se ele estiver na lista ou none caso contrario"""
    #   for i in range(len(aux)):
    #         if aux[i] == e:
    #            return i
    #   return None
         
    def tamanho(self):
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
lista.addFinal(15)
lista.addFinal(18)
lista.addFinal(3)
lista.addInicio(55)
lista.buscaIndexada(5)


"""Remove elementos final e inico"""
#lista.removeInicio()
#lista.removeFinal()

print("lista {}".format(lista))
print("primeiro elemento {}".format(lista.primeiro.dado))
print("ultimo elemento {}".format(lista.ultimo.dado))
print("tamanho da lista {}".format(lista.size))



