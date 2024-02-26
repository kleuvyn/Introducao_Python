function menuShow() {
  let menuMobile = document.querySelector('.mobile-menu');
  if (menuMobile.classList.contains('open')) {
    menuMobile.classList.remove('open');
    document.querySelector('.icon').src="https://img.icons8.com/?size=256&id=quuyJoZCkYni&format=png";
  } else {
    menuMobile.classList.add('open');
    document.querySelector('.icon').src="https://img.icons8.com/?size=256&id=K7OXfoF0zHXw&format=pngg";
  }
}

const switchModal = () => {
  const modal = document.querySelector('.modal')
  const actualStyle = modal.style.display
  if(actualStyle == 'block') {
    modal.style.display = 'none'
  } else {
    modal.style.display = 'block'
  }
}

const btnConfirmar = document.getElementById('confirmarBtn');
btnConfirmar.addEventListener('click', function() {
  const valores = obterValoresFormulario();
  const corpoEmail = construirCorpoEmail(valores);
  const assunto = 'Nova mensagem de contato';

  const mailtoLink = `mailto:b.kleuvyn@gmail.com?subject=${encodeURIComponent(
    assunto
  )}&body=${encodeURIComponent(corpoEmail)}`;

  window.location.href = mailtoLink;

  switchModal(); 
});

window.onclick = function(event) {
  const modal = document.querySelector('.modal')
  if (event.target == modal) {
    switchModal();
  }
}

function obterValoresFormulario() {
  const nome = document.getElementById('texto').value;
  const telefone = document.getElementById('telefone').value;
  const email = document.getElementById('email').value;
  const hora = document.getElementById('hora').value;
  const primeiroContatoSim = document.getElementById('sim').checked;
  const primeiroContatoNao = document.getElementById('nao').checked;
  const mensagem = document.getElementById('mensagem').value;

  return {
    nome,
    telefone,
    email,
    hora,
    primeiroContatoSim,
    primeiroContatoNao,
    mensagem,
  };
}

function construirCorpoEmail(valores) {
  return `
    Nome: ${valores.nome}
    Telefone: ${valores.telefone}
    E-mail: ${valores.email}
    Horário para entrar em contato: ${valores.hora}
    Primeiro Contato: ${valores.primeiroContatoSim ? 'Sim' : 'Não'}
    Mensagem: ${valores.mensagem}
  `;
}