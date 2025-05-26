/*
Termos
context:
É uma forma de compartilhar dados entre componentes sem precisar passar props manualmente de pai para filho.

Aprendizados:
| Elemento     | Papel                            |
| ------------ | -------------------------------- |
| `cliente`    | Valor atual do estado do cliente |
| `setCliente` | Atualiza os dados do cliente     |
| `pedido`     | Valor atual do pedido do cliente |
| `setPedido`  | Atualiza os dados do pedido      |
*/

import { createContext, useState } from "react";

export const PedidoContext = createContext();//Armazena os dados do pedido do cliente

export const PedidoProvider = ({ children }) => {
  const [cliente, setCliente] = useState({}); //guarda os dados do cliente (nome, CPF, endereço)
  const [pedido, setPedido] = useState({});//guarda os dados do pedido (sabor, tamanho, quantidade, borda)

  return (
    <PedidoContext.Provider value={{ cliente, setCliente, pedido, setPedido }}>
      {children}
    </PedidoContext.Provider>
  );
};
