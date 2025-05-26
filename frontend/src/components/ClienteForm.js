/*
Entenda:
useState(form)	Armazena dados do formulário localmente
useContext	Permite salvar os dados no contexto global (PedidoContext)
handleSubmit()	Salva os dados e redireciona para a próxima página
useNavigate()	Muda de rota sem recarregar a página
Formulário	Coleta nome, CPF e endereço
*/

import { useState, useContext } from "react";
import { useNavigate } from "react-router-dom";
import { PedidoContext } from "../context/PedidoContext";

const ClienteForm = () => {
  const [form, setForm] = useState({ nome: "", cpf: "", endereco: "" });
  const { setCliente } = useContext(PedidoContext);
  const navigate = useNavigate();

  const handleSubmit = (e) => {
    e.preventDefault(); // Impede o recarregamento da página
    setCliente(form);  // Salva os dados no contexto global
    navigate("/pedido"); // Leva o usuário para a página de seleção da pizza
  };

  return (
    <form onSubmit={handleSubmit} className="cliente-form">
      <h2>Seus Dados</h2>
      <input
        name="nome"
        placeholder="Nome"
        onChange={(e) => setForm({ ...form, nome: e.target.value })}
        required
      />
      <input
        name="cpf"
        placeholder="CPF"
        onChange={(e) => setForm({ ...form, cpf: e.target.value })}
        required
      />
      <input
        name="endereco"
        placeholder="Endereço"
        onChange={(e) => setForm({ ...form, endereco: e.target.value })}
        required
      />
      <button type="submit" className="primary-button">
        Continuar
      </button>
    </form>
  );
};

export default ClienteForm;
