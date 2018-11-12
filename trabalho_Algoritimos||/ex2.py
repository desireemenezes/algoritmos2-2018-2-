#!/usr/bin/env python
# -*- coding: utf-8 -*-

#ultilizando get e set

class No:   
    def __init__(self, dado, anterior = None, proximo = None):
        self._dado = dado
        self._anterior = anterior
        self.proximo = proximo

    # o get serve para você retornar o valor, acessa o atributo
    def getAnterior(self): 
        return self._anterior

    # o set serve para você passar um valor para um atributo privado da classe no qual você não tem acesso
    def setAnterior(self, novo):
        return self._anterior = novo

    def getProximo(self): 
        return self._proximo

    def setProximo(self, novo):
        return self._proximo = novo
    
    def getDado(self): 
        return self._dado

    def setDado(self, novo):
        return self._dado = novo
    
    #função str que transforma em string 
    def __str__(self):
        return str(self.getDado())

    # herda os atributos de nó
class listaEncadeada(No):
    def __init__(self, inicio = None, fim = None):
        self._inicio = inicio
        self._fim = fim

    def listaVazia(self):
        return self.inicio is None

    def inserirDadoInicio(self, dado):
        novo_no = No(dado)
        if self.Vazia() == True
            self._inicio = novo_no
            self._fim = novo_no
        else:
            novo_no.setProximo(self._inicio)
            self._inicio.setAnterior(novo_no)
            self._inicio = novo_no

    def inserirDadoFinal(self, dado):
        novo_no = No(dado)
        if self.Vazia() == True
           self._inicio = novo_no
           self._fim = novo_no
        else:
            self._fim.setPrximo(novo_no)
            novo_no.setAnterior(self._fim)
            self._fim = novo_no
      
    def buscaDado(self, dado):
        if self.listaVazia == True:
            print("Vazia")
            return None
        aux = self.inicio
        while i != None
            if i.getDado() == dado:
                return i
            else:
                i = i.getProximo()
        return None
        
    
    
    