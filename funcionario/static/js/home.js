function mostrarDetalhe(elemento) {
  document.getElementById('detalheNome').textContent = elemento.dataset.nome;
  document.getElementById('detalheCPF').textContent = elemento.dataset.cpf;
  document.getElementById('detalheEndereco').textContent = elemento.dataset.endereco;
  document.getElementById('detalheQuantidade').textContent = elemento.dataset.quantidade;
  document.getElementById('detalheBorda').textContent = elemento.dataset.borda;
  document.getElementById('detalheTamanho').textContent = elemento.dataset.tamanho;
  document.getElementById('detalheSabores').textContent = elemento.dataset.sabores;

  document.getElementById('detalhePedido').style.display = 'flex';
  document.getElementById('mainContent').style.display = 'none';
  document.querySelector('.sidebar').style.display = 'none';
}

function fecharDetalhe() {
  document.getElementById('detalhePedido').style.display = 'none';
  document.getElementById('mainContent').style.display = 'flex';
  document.querySelector('.sidebar').style.display = 'flex';
}
