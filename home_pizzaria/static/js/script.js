// Espera o documento carregar
document.addEventListener("DOMContentLoaded", () => {
  const formContato = document.getElementById('form-contato');

  formContato.addEventListener('submit', (e) => {
    e.preventDefault(); // Impede o envio padrão

    // Pega o valor do email
    const email = formContato.querySelector('input[type="email"]').value.trim();

    if(email) {
      alert(`Obrigado pelo contato! Em breve responderemos o email: ${email}`);
      formContato.reset();
    } else {
      alert("Por favor, insira um email válido.");
    }
  });
});


