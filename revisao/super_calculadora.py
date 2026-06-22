def super_calculadora(operacao, *args):
    if not args:
        return 0
    resultado = args[0]
    for n in args[1:]:
        if operacao == "soma":
            resultado += n
        elif operacao == "sub":
            resultado -= n
        elif operacao == "mult":
            resultado *= n
        elif operacao == "div":
            if n != 0:
                resultado /= n
            else:
                return "Não é possível dividir por zero"
        else:
            return "Operação inválida"
    return f"O resultado de {operacao} é {resultado}"

def menu_calculadora():
    print("=== Super Calculadora ===")
    op = input("Digite a operação (soma, sub, mult, div): ").strip().lower()

    numeros_raw = input("Digite os números separados por espaço: ")

    try:
        lista_numeros = [float(n) for n in numeros_raw.split()]
        print(super_calculadora(op, *lista_numeros))

    except ValueError:
        print("Erro: Certifique-se de digitar apenas números separados por espaço.")
    
    finally:
        return