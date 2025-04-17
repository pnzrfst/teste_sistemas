def coletarDados(nome,idade,telefone,email):
    if(" " in nome and "48" in telefone and "@" in email and "." in email and idade >= 18):
        return True
    else:
        return "ERRO"


def tabelasDescontos(salario):
    if(salario < 100):
        return 0.1
    elif(salario > 100 and salario < 200):
        return 0.3
    else:
        return 0.9
    


def totalComDescontos(salario, comissao):
    if salario and comissao < 0:
        return "ERRO"
    else:
        totalBruto = salario + (salario * comissao)
        totalDescontos = salario * tabelasDescontos(salario)
        totalLiquido = totalBruto - totalComDescontos
        return f"SALÁRIO LÍQUIDO: ${totalLiquido}, SALÁRIO BRUTO: ${totalBruto}, TOTAL DOS DESCONTOS: ${totalDescontos}"
    


