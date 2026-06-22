def classificar_dados(colecao):
    if type(colecao) == list:
        print(f"É uma lista com o primeiro item {colecao[0]} e o último {colecao[-1]}")
    
    elif type(colecao) == set:
        print(f"É um conjunto com apenas valores únicos de tamanho {len(colecao)}")
    
    elif type(colecao) == tuple:
        print(f"É uma tupla e a soma de seus valores é {sum(colecao)}")
    
    return "Tipo não suportado"

def menu_classificar():
    print("=== Analisador de coleções numéricas ===")
    op = input("Digite o tipo desejado: (list, tuple, set): ").strip().lower()

    numeros_raw = input("Digite os valores separados por espaço : ")

    try:
        if op == "list":
            classificar_dados([float(n) for n in numeros_raw.split()])
        elif op == "tuple":
            classificar_dados((float(n) for n in numeros_raw.split()))
        elif op == "set":
            classificar_dados({float(n) for n in numeros_raw.split()})
        else:
            print(f"Tipo {op} não suportado")        

    except ValueError:
        print("Erro: Verifique a digitação da coleção.")
    
    finally:
        return