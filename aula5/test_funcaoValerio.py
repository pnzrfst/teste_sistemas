import pytest
from funcaoValerio import *

@pytest.mark.parametrize("nome, idade, telefone, email", [
    ("Luiz Carlos", 12, "48 9823113", "Luiz@gmail.com"),
    ("Luiz Carlos", 12414, "489823113", "Luizgmail.com"),
    ("Luiz Carlos", 13, "48 2323113", "Luiz12@gmail.com"),
    ("Luiz Carlos", 15, "48 21323113", "Luiz12@gmail.com")
])

def test_funcaoCadastro(nome, idade, telefone, email):
    assert cadastro(nome, idade, telefone, email)


# @pytest.mark.parametrize('salario, valorEsperado', [
#     [1517, 0.075],
#     [1519, 0.09],
#     [2794, 0.12],
#     [4191, 0.14],
#     [8158, 0.20]

# ])


# def test_tabelaInss():
#     assert tabela_inss(salario)

@pytest.mark.parametrize('salarioLiquido, comissao', [
    (1517, 100),
    (2792, 200),
    (4182, 100),
    (8143, 100)
])


def test_funcaoSalario(salarioLiquido, comissao):
    assert salario(salarioLiquido, comissao)