def filtrar_estoque(limite, **kwargs):
    aprovados = {}
    
    for produto, preco in kwargs.items():
        if preco >= limite:
            aprovados[produto] = preco
            
    return aprovados


def menu_estoque():
    print("=== Filtro de Estoque ===")
    items = int(input("Digite a quantidade de itens a cadastrar no estoque: "))
    dicio = {}
    for a in range(0,items):
        key = input("Digite o item a ser cadastrado: ").strip()
        value = int(input("Digite a quantidade do item: "))
        dicio[key] = value
    
    qtd = int(input("Digite a quantidade em estoque para filtrar: "))
    resultado = filtrar_estoque(qtd, **dicio)
    print(f"Estes são os itens com mais de {qtd} em estoque:\n{resultado}")
