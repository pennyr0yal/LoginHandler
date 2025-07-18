# Automação de Login com Selenium e requests

Este script realiza o login automático (via `Selenium` ou `requests`) no site de testes, simula o preenchimento dos campos de usuário e senha, envia os dados e retorna uma mensagem com o resultado do login.

---

## Funcionalidades

- Aceita entrada de usuário e senha manualmente ou utiliza dados de teste pré-definidos.
- Permite que o usuário selecione entre login via Selenium ou requests.
  - No modo `Selenium`, detecta e atualiza automaticamente o **chromedriver** compatível com sua versão do Chrome. Acessa o navegador e executa o login de forma visível ou em segundo plano (headless).
  - No modo `Requests`, realiza a requisição POST diretamente para o servidor, sem abrir o navegador. O desempenho desse modo é melhor e mais rápido do que com Selenium.
- Exibe mensagens de sucesso ou falha com base no alerta retornado pela página.

## Como usar

1. Execute o arquivo .bat na pasta principal. O programa instalará o venv e as bibliotecas necessárias.
2. Uma janela irá ser exibida para que o usuário escolha entre fazer o login via Selenium ou via requests.
3. Digite os dados de acesso quando solicitado.
   - Para usar os dados de teste, digite `1` em ambos os campos.
4. Selenium:
   - O navegador será aberto e o login será executado.
5. Requests:
   - A requisição será enviada ao site para efetuar o login.
6. Você verá no terminal uma das mensagens:
   - ✅ Login bem sucedido!
   - ❌ Login falhou, tente novamente.
   - ⚠️ Classe de alerta inesperada.

## Observações

- O script atualiza automaticamente o chromedriver.exe na pasta C:/WebDrivers se detectar uma versão incompatível com o navegador.
- A verificação de versão ou download do driver pode falhar em ambientes com restrições de rede.
- O script pode ser adaptado para automatizar o login em outros sites, bastando alterar os seletores XPATH e a URL.

# Autora
Desenvolvido por Natalia Junghans

📧 natbjunghans@gmail.com
