import unittest

from Aluno import Aluno
from financeiro import Financeiro
from Nota import Nota

class TestAluno(unittest.TestCase):
    def setUp(self):
        self.aluno = Aluno("João")
        self.aluno.adicionar_nota(8)
        self.aluno.adicionar_nota(7)

    def test_calcular_media(self):
        self.assertEqual(self.aluno.calcular_media(), 7.5)

class TestFinanceiro(unittest.TestCase):
    def setUp(self):
        self.financeiro = Financeiro()
        self.financeiro.adicionar_valor_devido(500)
        self.financeiro.adicionar_valor_pago(300)

    def test_calcular_valor_em_aberto(self):
        self.assertEqual(self.financeiro.calcular_valor_em_aberto(), 200)

if __name__ == "__main__":
    unittest.main()