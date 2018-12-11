#!/usr/bin/env python
# -*- coding: utf-8 -*-

class No:
    
    def __init__(self, dado): #Construtor da classe.
        """atributos"""
        self.dado = dado
        self.proximo = None
        self.anterior = None

    def __repr__(self):
        return '%s <-> %s' % (self.dado, self.proximo)