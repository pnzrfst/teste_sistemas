def calcular_imc(peso,altura):

if altura <=0:
    return "Altura invalida"

    imc = peso/(altura*altura)


    if valor_imc < 17:
        return "Muito abaixo do peso ideal"
    elif valor_imc >= 17 and valor_imc < 18.49 :
        return "Abaixo do peso"
    elif valor_imc >= 18.50 and valor_imc < 24.99 :
        return "Peso normal"
    elif valor_imc >= 25 and valor_imc < 29.99 :
        return "Acima do peso"
    elif valor_imc >= 30 and valor_imc < 34.99 :
        return "Obesidade grau 1"
    elif valor_imc >= 35 and valor_imc < 39.99 :
        return "Obesidade grau 2"
    elif valor_imc > 40 :
        return "Obesidade grau 3"


