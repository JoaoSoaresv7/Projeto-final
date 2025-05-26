import { useContext } from "react";
import { PedidoContext } from "../context/PedidoContext";
import pizza from "../assets/pizza.jpg";

const Carrinho = () => {
  const { cliente, pedido } = useContext(PedidoContext);

  const total = 45 * pedido.quantidade + (pedido.borda ? 5 : 0);

  return (
    <div className="carrinho-container">
      <h2>Resumo do Pedido</h2>

      <img src={pizza} alt="pizza" width={100} />

      <p>
        <strong>
          {pedido.quantidade}x {pedido.sabor}
        </strong>
      </p>
      <p>
        Tamanho: <strong>{pedido.tamanho}</strong>
      </p>
      {pedido.borda && (
        <p>
          Adicional: <strong>Borda recheada</strong>
        </p>
      )}

      <div className="carrinho-resumo">
        <h3>Entrega:</h3>
        <p>
          <strong>Endereço:</strong> {cliente.endereco}
        </p>
        <p>
          <strong>Tempo estimado:</strong> 22-28 minutos
        </p>
        <p>
          <strong>Total:</strong> R$ {total},00
        </p>
      </div>

      <button className="primary-button" style={{ marginTop: "1.5rem" }}>
        Fazer Pedido
      </button>
    </div>
  );
};

export default Carrinho;
