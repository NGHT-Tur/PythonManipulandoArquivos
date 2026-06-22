def resumo_vendas(lista_vendas):
    total_geral = 0
    item_mais_caro = ""
    maior_preco_unitario = 0
    
    for venda in lista_vendas:
        subtotal = venda["valor"] * venda["quantidade"]
        total_geral += subtotal
        
        if venda["valor"] > maior_preco_unitario:
            maior_preco_unitario = venda["valor"]
            item_mais_caro = venda["item"]
            
    return total_geral, item_mais_caro

def relatorio_teste():
    vendas = [
        {"item": "Mouse", "valor": 50, "quantidade": 3},
        {"item": "Monitor", "valor": 900, "quantidade": 1},
        {"item": "Fone", "valor": 120, "quantidade": 2}
    ]
    print(resumo_vendas(vendas))