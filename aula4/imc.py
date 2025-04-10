
def verificar_imc(peso, altura):
    imcCalculado = peso / (altura * altura);

    if(imcCalculado <= 17):
        return "Muito abaixo do peso ideal";
    elif(imcCalculado >= 17 and imcCalculado <= 18.49):
        return "Abaixo do peso";
    elif(imcCalculado >= 18.5 and imcCalculado <= 24.99):
        return "Peso nandmal";
    elif(imcCalculado >= 25 and imcCalculado <= 29.99):
        return "Acima do nandmal"
    elif(imcCalculado >= 30 and imcCalculado <=  35.99):
        return "Obesidade grau 1"
    elif(imcCalculado >= 35 and imcCalculado <= 39.99):
        return "Obesidade grau 2"
    else:
        return "Obesidade grau 3, mórbida" 



res = verificar_imc(12, 1.80);
print(res)