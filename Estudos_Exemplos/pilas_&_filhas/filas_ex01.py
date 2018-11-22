#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" SIMULAÇÃO DE FILA ATRAVÉS DE LISTAS """
""" Na fila só remove no inicio e só insere no final """


class fila:
    #construtor self = instancia
    def __init__(self):
        self.fila = []

    def __repr__(self):
        return "[" + str(self.fila) + " ]"

    #método de inserção
    def inserir(self, final):
        self.fila.append(final)
     
    #método que retorna o tamanho da fila
    def tamanho(self):
        return len(self.fila)

    #método que verifica o tamanho da fila
    def veriricaFilaVazia(self):
        return self.tamanho() == 0
    
     #método de remoção  (sempre remove do inico da fila)
    def excluir(self):
        if not self.veriricaFilaVazia():
            del self.fila[0]

fila = fila()
print(fila.veriricaFilaVazia())
fila.inserir(1)
fila.inserir(3)
fila.inserir(9)
print("Fila {}".format(fila.tamanho()))
fila.excluir()
print("Fila {}".format(fila.excluir()))
print("Fila {}".format(fila.tamanho()))

        