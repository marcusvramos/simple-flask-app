# Flask OCI Application

Aplicação Flask com deploy automatizado para Oracle Cloud Infrastructure (OCI) usando GitHub Actions.

## 🚀 Características

- **Aplicação Flask** rodando na porta 8080
- **Proxy Reverso** com Nginx
- **CI/CD** com GitHub Actions
- **Backup automático** antes de cada deploy
- **Notificações** via Discord/Slack
- **Health checks** automáticos

## 📋 Pré-requisitos

- Instância OCI configurada
- Python 3.11+
- Chave SSH configurada

## 🔧 Configuração

### Secrets do GitHub

Configure os seguintes secrets no repositório:

- `SSH_PRIVATE_KEY`: Chave privada SSH para acessar a instância
- `DISCORD_WEBHOOK`: URL do webhook do Discord (opcional)
- `SLACK_WEBHOOK`: URL do webhook do Slack (opcional)

### Informações da Instância

- **IP**: 137.131.166.12
- **Compartimento**: VMs (subcompartimento de VM)
- **Shape**: VM.Standard.E2.1.Micro (Free Tier)
- **NSG**: Mesmo grupo de segurança da vm-web

## 🚦 Endpoints

- `/` - Página inicial
- `/api/health` - Health check
- `/api/info` - Informações do sistema
- `/api/status` - Status da aplicação

## 📦 Deploy

O deploy é feito automaticamente ao fazer push para a branch `main` ou `master`.

### Processo de Deploy:

1. **Testes** - Executa testes automatizados
2. **Backup** - Cria backup da versão anterior
3. **Deploy** - Copia arquivos e reinicia serviços
4. **Verificação** - Valida health check
5. **Notificação** - Envia status para Discord/Slack

### Deploy Manual

```bash
# Conectar na instância
ssh ubuntu@137.131.166.12

# Verificar status
sudo systemctl status flask-app

# Ver logs
sudo journalctl -u flask-app -f
```

## 🔄 Backup

Os backups são criados automaticamente em `/home/ubuntu/backups/` antes de cada deploy.

Mantém apenas os últimos 5 backups para economizar espaço.

## 🛠️ Desenvolvimento Local

```bash
# Instalar dependências
pip install -r requirements.txt

# Executar aplicação
python app.py

# Acessar em http://localhost:8080
```

## 📊 Monitoramento

- Health check: `http://137.131.166.12/api/health`
- Logs: `sudo journalctl -u flask-app -f`
- Status Nginx: `sudo systemctl status nginx`

## 🔐 Segurança

- Aplicação roda com usuário não-root
- Nginx como proxy reverso
- Network Security Group configurado
- Backups automáticos