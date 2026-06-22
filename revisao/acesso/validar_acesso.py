SISTEMA_ATIVO = True 

def validar_acesso(usuario, senha, prioridade=1):
    pode_entrar = SISTEMA_ATIVO and (usuario == "admin" or prioridade > 5)
    
    return pode_entrar

def menu_acesso():
    user = input("Digite seu usuário: ")
    senha = input("Digite sua senha: ")
    try:
        prio = int(input("Digite sua prioridade: "))
    except ValueError:
        prio = None
    finally:
        if prio != None:
            print(validar_acesso(user, senha, prio))
        else:
            print(validar_acesso(user, senha))