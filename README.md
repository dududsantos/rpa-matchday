# rpa-matchday ⚽

Robô simples em Python que, todo dia, busca os jogos de futebol do dia (via [football-data.org](https://www.football-data.org/)), filtra pelos seus times e competições favoritos e envia um resumo formatado direto pro WhatsApp (via [CallMeBot](https://www.callmebot.com/blog/free-api-whatsapp-messages/)).

Exemplo de mensagem recebida:

```
Oi Dudu, esses são os Jogos de hoje ⚽:

⚽ *Flamengo x Mirassol*
🕐 19:30 | 🏆 Campeonato Brasileiro Série A
```

## Como funciona

1. `client.py` consulta a API do football-data.org pedindo os jogos da data atual.
2. `filter.py` filtra os jogos, mantendo apenas os que envolvem uma competição favorita ou um time favorito.
3. `formatter.py` monta a mensagem final, convertendo os horários (UTC) para o horário de Brasília.
4. `notifier.py` envia a mensagem pro WhatsApp via CallMeBot.
5. Se não houver jogos filtrados no dia, nenhuma mensagem é enviada.

## Estrutura do projeto

```
rpa-matchday/
├── src/
│   ├── main.py        # ponto de entrada — orquestra todo o fluxo
│   ├── client.py       # consome a API de futebol
│   ├── filter.py       # filtra jogos por time/competição favoritos
│   ├── formatter.py    # formata a mensagem final
│   ├── notifier.py     # envia a mensagem via WhatsApp (CallMeBot)
│   └── settings.py     # variáveis de configuração e listas de favoritos
├── requirements.txt
├── .env.example
└── README.md
```

## Pré-requisitos

- Python 3.9+ (o projeto usa `zoneinfo`, disponível a partir do Python 3.9)
- Uma chave de API gratuita do [football-data.org](https://www.football-data.org/client/register)
- Um número de WhatsApp registrado no [CallMeBot](https://www.callmebot.com/blog/free-api-whatsapp-messages/) (o processo de ativação é gratuito e leva poucos minutos)

## Instalação

```bash
git clone https://github.com/dududsantos/rpa-matchday.git
cd rpa-matchday

python -m venv .venv
.venv\Scripts\Activate.ps1   # Windows (PowerShell)
# source .venv/bin/activate  # Linux/macOS

pip install -r requirements.txt
```

## Configuração

Copie o arquivo de exemplo e preencha com suas credenciais:

```bash
cp .env.example .env
```

| Variável | Descrição |
|---|---|
| `API_URL` | URL base da API do football-data.org (padrão já definido, geralmente não precisa alterar) |
| `API_KEY` | Sua chave de API do football-data.org |
| `CALLMEBOT_API_KEY` | Chave de API gerada pelo CallMeBot ao ativar seu número |
| `WHATSAPP_PHONE` | Número de WhatsApp (com DDI) que vai receber as notificações |

Os times e competições favoritos ficam definidos diretamente em [`src/settings.py`](src/settings.py), nas listas `FAV_COMPETITIONS` e `FAV_TEAMS` (usando os IDs da API do football-data.org). Edite essas listas para personalizar.

## Uso

Rode sempre a partir da raiz do projeto, como módulo:

```bash
python -m src.main
```

Para rodar automaticamente todo dia, agende a execução desse comando no Task Scheduler (Windows) ou no cron (Linux/macOS).

## Tecnologias

- [requests](https://pypi.org/project/requests/) — chamadas HTTP
- [python-dotenv](https://pypi.org/project/python-dotenv/) — carregamento de variáveis de ambiente
- [tzdata](https://pypi.org/project/tzdata/) — banco de dados de fusos horários (necessário no Windows)

## Licença

Projeto pessoal, sem licença definida. Sinta-se à vontade para usar como referência.
