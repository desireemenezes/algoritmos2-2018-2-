
class No:
    def __init__(self, dado, proximo_no = None):
        self.dado = dado
        self.proximo = proximo_no #valor simbolico vazio para o proximo que nao foi declarado como atributo

class ListaEncadeada:
    def __init__(self): #init construtor
        self.cabeca = None
        self.tamanho = 0

    def append(self, elem):
        if self.cabeca:
            # o ponteiro esta apontando para o mesmo espaco de memoria que e vaziu
            ponteiro = self.cabeca
            # enquanto tiver proximo eu percorro ate chegar no ultimo
            while(ponteiro.proximo):
                ponteiro = ponteiro.proximo
            ponteiro.proximo = No(elem)   
        else:
            #primeira insercao
           self.cabeca = No(elem)
        self.tamanho += 1

    def __len__(self):
        """retorna o tamanho da lista"""
        return self.tamanho
    
    def get(self, indice):
        pass

    def __getitem__(self, indice):
        # a = lista[6]
        # a = lista.get(6)
        ponteiro = self.cabeca
        for i in range(indice):
            if ponteiro:
                ponteiro = ponteiro.proximo
            else:
                #palavra reservada raise index error
                raise IndentationError("Indice da lista fora do range")
        if ponteiro:
            return ponteiro.dado
        else:
            raise IndentationError("Indice da lista fora do range")

    def set(self, elem):
        pass
    
    def __setitem__(self, indice):
        # lista[6] = 3
        #lista.set(6) = 3
        ponteiro = self.cabeca
        for i in range(indice):
            if ponteiro:
                ponteiro = ponteiro.proximo
            else:
                #palavra reservada raise index error
                raise IndentationError("Indice da lista fora do range")
        if ponteiro:
            ponteiro.dado = elem
        else:
            raise IndentationError("Indice da lista fora do range")
    

lista = ListaEncadeada()
lista.append(7)
lista.append(8)
ultimo = lista.last()
print(len(lista))
print(lista.tamanho)
print(lista[1])
print(ultimo)
print("{}" .format(lista))



"""class No:
    # no defi declaramos os atributos da classe que nem no java (declarei atributos privados)
    # o  sel e que nem o this do java
    def __init__(self, dado, anterior = None, proximo = None):
        self._dado = dado
        self._proximo = proximo
        self._anterior = anterior

    #metodos GET e SET
    def getAnterior(self):
        return self._anterior
    
    def setAnterior(self, novo):
        self._anterior = novo


    def getProximo(self):
        return self._proximo
    
    def setProximo(self, novo):
        self._proximo = novo

    
    def getDado(self):
        return self._dado
    
    def setDado(self, novo):
        self._dado = novo

    # funcao de retorno sem ela retorna so o endereco da memoria
    def __str__(self):
        return str(self.getDado())


# class lista encadeada vai herdar todos atributos de No
class listaEncadeada(No):
    def __init__(self, inicio =  None, fim = None): #cria construtores
        #atributos privados
        self._inicio = inicio
        self._fim = fim
    
    def Vazia(self):
        # retorna true ou false se inicio for vaziu
        return self.inicio is None
    
    def BuscarElemento(self, valor):
        if self.Vazia == True:
            return None
            print("Lista vazia!")
        #crio uma variavel auxiliar para pegar o inicio (i)
        i = self._inicio
        while i != None:
            if i.getDado() == valor:
                return i
            i = getProximo()
        
        return None
    
    def inserir(self, valor):
        novo = No(valor)
        if self.Vazia() == True:
           self._inicio = novo
           self._fim = novo
        else:
            novo.setProximo(self._inicio)
            self._inicio.setAnterior(novo)
            self._inicio = novo """