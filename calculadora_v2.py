
saida = ''  

def adicao(a, b):
    """Retorna a soma entre dois números"""
    return a + b

def subracao(a, b):
    """Retorna a subtração entre dois números"""
    return a - b

def multiplicacao(a, b):
    """Retorna a multiplicação entre dois números"""
    return a * b

def divisao(a, b):
    """Retorna a divisão entre dois números com tratamento de divisão por 0"""
    if b == 0:
        return "Não foi possível realizar a divisão por 0"
    return a / b

def calculadora(num1, num2, operacao):
    """
    Recebe dois números e a operação desejada.
    Aceita tanto o símbolo quanto o nome: +, -, *, /, adicao, subracao, multiplicacao, divisao
    """
    resultado = None
    
   
    if operacao == '+' or operacao.lower() == 'adicao':
        resultado = adicao(num1, num2)
    elif operacao == '-' or operacao.lower() == 'subracao':
        resultado = subracao(num1, num2)
    elif operacao == '*' or operacao.lower() == 'multiplicacao':
        resultado = multiplicacao(num1, num2)
    elif operacao == '/' or operacao.lower() == 'divisao':
        resultado = divisao(num1, num2)
    else:
        resultado = "Operação inválida. Use: +, -, *, / ou adicao, subracao, multiplicacao, divisao"
    
    return resultado


while saida.lower() != 'n':
    print("\n=== CALCULADORA V2 ===")
    
   
    try:
        primeiro_numero = float(input("Digite o primeiro número: "))
        segundo_numero = float(input("Digite o segundo número: "))
        operacao = input("Digite a operação (+, -, *, / ou nome): ")
        
   
        resultado = calculadora(primeiro_numero, segundo_numero, operacao)
        
    
        print(f"Resultado da operação: {resultado}")
        
    except ValueError:
        print("Erro: Digite apenas números válidos!")
    
   
    saida = input("\nDeseja continuar? [S/N]: ")
    
print("Calculadora encerrada. Até mais!")