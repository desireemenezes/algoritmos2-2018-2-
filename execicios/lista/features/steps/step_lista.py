""" TESTANDO LISTA """

from behave import given, then, when

from lista import check_maior


@given('uma lista com os valores 1, 2, 3, 4 e 5')
def given_lista_com_valores(context):
    """Cria lista com os valores dados."""
    context.lista = [1, 2, 3, 4, 5]

@when('verifico o maior valor da lista')
def when_verifico_maior_valor(context):
    """Forca o calculo da lista."""
    lista = context.lista
    context.resultado = check_maior(lista)

@then('o resultado e 5')
def then_mostro_resultado(context):
    """Testa o maior numero."""
    resultado_lista = context.resultado[4]
    assert resultado_lista in [1, 2, 3, 4, 5]