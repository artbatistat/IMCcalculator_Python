# Calculadora de IMC - ÍNDICE DE MASSA CORPORAL

altura = int(input('Qual é a sua altura em cm?'))
peso = int(input('Qual é o seu peso em kg?'))

def calcularIMC(altura,peso):
    imc = peso/ (altura/100)**2
    if (imc < 18.5):
        print('O resultudado do seu IMC é: Magro')
    elif (imc >= 18.5 and imc <= 24.9):
        print('O resultudado do seu IMC é: Normal')
    elif (imc >= 25 and imc <= 29.9):
        print('O resultudado do seu IMC é: Sobrepeso')
    elif (imc >= 30 and imc <= 39.9):
        print('O resultudado do seu IMC é: Obesidade')
    else:
        print('O resultudado do seu IMC é: Obesidade grave')

calcularIMC(altura,peso)