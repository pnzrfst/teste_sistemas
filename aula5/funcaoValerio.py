def cadastro(nome, idade, telefone, email):    
    if (not nome_valido(nome) or not email_valido(email) or not telefone_valido(telefone)):
        return "Favor preencher todas as informações"   
    if idade < 18: 
        return "Idade invalida"    
    return f"Dados cadastrado com sucesso: Nome: {nome}, Idade: {idade}, Telefone: {telefone}, Email: {email}"

def nome_valido(nome):
    return " " in nome

def email_valido(email):
    return "@" in email and ".com" in email

def telefone_valido(telefone):
    return "48" in telefone or "47" in telefone

def tabela_inss(salario):
    if salario <= 1518:
        return 0.075
    elif salario > 1518 and salario <= 2793.88:
        return 0.09
    elif salario > 2793.88 and salario <= 4190.83:
        return 0.12
    elif salario > 4190.83 and salario <= 8157.41:
        return 0.14
    else:
        return 0.20

def salario(salario, comissao):
    if salario <= 0 and comissao <= 0:
        return "Salario ou comissão invalida.."    
    inss = salario * tabela_inss(salario) 
    c1 = salario * comissao
    return f"Salario Liquido: R$ {salario:.2f} - INSS: R$ {inss:.2f} - Comissão: R$ {c1:.2f} - Salario Bruto: R$ {((salario + c1) - inss):.2f}"
