

fila_pedidos = []

def criar_pedido(dados):
    fila_pedidos.append(dados)
    print("Pedido adicionado à fila:", dados)

def obter_fila():
    return fila_pedidos

def processar_pedido():
    if fila_pedidos:
        return fila_pedidos.pop(0)
    return None
