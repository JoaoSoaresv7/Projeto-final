import { useState, useContext } from "react";
import { useNavigate } from "react-router-dom";
import { PedidoContext } from "../context/PedidoContext";
import pizza from "../assets/pizza.jpg";

const EscolherPizza = () => {
  const [tamanho, setTamanho] = useState("M");
  const [quantidade, setQuantidade] = useState(1);
  const [borda, setBorda] = useState(false);
  const { setPedido } = useContext(PedidoContext);
  const navigate = useNavigate();

  const handlePedido = () => {
    setPedido({
      sabor: "Calabresa",
      tamanho,
      quantidade,
      borda,
    });
    navigate("/carrinho");
  };

  return (
    <div className="pizza-page">
      <img src={pizza} className="pizza-image" alt="Pizza" />
      <h3>Pizza Calabresa - R$45,00</h3>

      <div className="tamanho-btns">
        {["P", "M", "G"].map((t) => (
          <button
            key={t}
            className={t === tamanho ? "ativo" : ""}
            onClick={() => setTamanho(t)}
          >
            {t}
          </button>
        ))}
      </div>

      <label>
        <input
          type="checkbox"
          checked={borda}
          onChange={(e) => setBorda(e.target.checked)}
        />
        Borda recheada
      </label>

      <div style={{ margin: "1rem 0" }}>
        <button onClick={() => setQuantidade(Math.max(1, quantidade - 1))}>
          −
        </button>
        <span style={{ margin: "0 1rem" }}>{quantidade}</span>
        <button onClick={() => setQuantidade(quantidade + 1)}>+</button>
      </div>

      <button className="primary-button" onClick={handlePedido}>
        Adicionar ao Carrinho
      </button>
    </div>
  );
};

export default EscolherPizza;
