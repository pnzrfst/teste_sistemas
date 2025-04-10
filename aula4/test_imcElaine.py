import pytest    
from imc_elaine import verificar_imc

@pytest.mark.parametrize(
    "peso, altura, esperado", 
    [
        (89.90, 1.45, "Obesidade grau 3")
    ]
)
def test_imcElaine(peso, altura, esperado):
    assert verificar_imc(peso, altura) == esperado
