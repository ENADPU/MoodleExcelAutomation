# 📡 Sistema de Monitoramento de Inscrições e Atualização de Planilhas

Este projeto consiste em um sistema que automatiza o monitoramento de inscrições de estudantes em cursos em uma plataforma Moodle e a atualização de dados em planilhas Excel armazenadas no SharePoint. Utilizando o Flask para receber webhooks do Moodle e o Power Automate para atualizar os dados nas planilhas, o sistema garante que todas as inscrições sejam processadas e documentadas de maneira eficiente.

## 🛠️ Funcionalidades

- 🔔 **Monitoramento de Inscrições:** Recebe notificações de inscrição e atualização de status diretamente do Moodle via webhook.
- 📝 **Formatação de Dados:** Formata automaticamente os dados recebidos (CPF, nome, vínculo, etc.) antes de serem enviados para o Power Automate.
- 📑 **Atualização de Planilhas:** Integração com o Power Automate para preencher e atualizar planilhas Excel no SharePoint com os dados formatados.
- 📊 **Documentação Completa:** Documentação detalhada sobre como instalar, configurar e usar o sistema.

## 🚀 Como Iniciar

### 📚 Tecnologias Utilizadas
- [Flask](https://flask.palletsprojects.com/)
- [Power Automate](https://flow.microsoft.com/)
- [Moodle Web Services](https://docs.moodle.org/dev/Web_services)
- [SharePoint](https://www.microsoft.com/en-us/microsoft-365/sharepoint/collaboration)

### 📦 Pré-requisitos

- 🐍 **Python 3.8+** - [Download Python](https://www.python.org/downloads/)
- 📋 **Conta no Heroku (opcional)** - Para deploy na nuvem.
- 📊 **Power Automate** - Configurado para integração com SharePoint e Excel.

### 🖥️ Instalação

1. Clone o repositório:
   ```bash
   git clone https://github.com/seu-usuario/seu-repositorio.git
   ```
2. Acesse o diretório do projeto:
   ```bash
   cd seu-repositorio
   ```
3. Crie e ative o ambiente virtual:
   ```bash
   python -m venv venv
   source venv/bin/activate # Linux/Mac
   venv\Scripts\activate # Windows
   ```
4. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

### ⚙️ Configuraçãoo

1. Crie um arquivo .env na raiz do projeto com as seguintes variáveis de ambiente:
```bash
MOODLE_API_URL=https://seu-moodle.com/webservice/rest/server.php
MOODLE_API_TOKEN=seu-token-de-acesso
POWER_AUTOMATE_URL=https://seu-fluxo-de-automacao.com
PORT=5000
DEBUG=True
```

2. Certifique-se de que as URLs e tokens de acesso estão corretos e correspondem ao seu ambiente.

### 📊 Fluxo de Trabalho

1. **Inscrição do estudante:** Quando a inscrição de um estudante é aceita em um curso, o Moodle envia um webhook para o servidor Flask.
2. **Processamento do Webhook:** O Flask recebe o webhook, formata os dados e envia para o Power Automate.
3. **Atualização da Planilha:** O Power Automate atualiza as planilhas Excel no SharePoint com os dados formatados.

### 🧪 Testes

- Execute testes unitários e de integração para garantir que tudo está funcionando conforme o esperado:
```bash
pytest tests/
```

### 🌐 Deploy

#### Heroku
1. Faça login no Heroku:
```bash
heroku login
```

2. Crie uma nova aplicação:
```bash
heroku create nome-da-sua-aplicacao
```

3. Faça o deploy do código:
```bash
git push heroku main
```

### Outros
- Consulte a documentação da plataforma de nuvem de sua escolha (AWS, Google Cloud, Azure, etc.) para instruções de deploy.

### 🤝 Contribuições
1. Faça um fork do projeto.
2. Crie uma nova branch com suas alterações:
```bash
git checkout -b feature/nova-funcionalidade
```
3. Faça commit das suas alterações:
```bash
git commit -m 'Adiciona nova funcionalidade'
```
4. Faça push para a branch criada:
```bash
git push origin feature/nova-funcionalidade
```
5. Abra um pull request.

### 📝 Licença
Este projeto está licenciado sob a Licença MIT - consulte o arquivo [LICENSE](LICENSE) para mais detalhes.

### 🧑‍💻 Autor
- **Gustavo Barbosa:** - [LinkedIn](https://www.linkedin.com/in/barbosa885/)
