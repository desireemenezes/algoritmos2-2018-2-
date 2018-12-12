"""Testa a insercao da Lista Duplamente Encadeada."""

from behave import given, then, when
from ListaEncadeada import ListaEncadeada

#teste1
@given('que eu tenho uma lista vazia e quero inserir um valor no inicio')
def given_tenho_uma_lista_(context):
    context.lista = ListaEncadeada()


@when('eu adc um numero {num:d}')
def when_adiciono_no_final(context, num):
    context.lista.addInicio(num)
    

@then('a lista tem {num:d} valor')
def then_lista_tem_n_elementos(context, num):
    assert context.lista.tamanho() == num

#teste2
@given('que eu tenho uma lista vazia e quero inserir um valor no final')
def given_tenho_uma_lista_(context):
    context.lista = ListaEncadeada()


@when('eu adc um numero {num:d}')
def when_adiciono_no_final(context, num):
    context.lista.addFinal(num)
    

@then('a lista tem {num:d} valor')
def then_lista_tem_n_elementos(context, num):
    assert context.lista.tamanho() == num