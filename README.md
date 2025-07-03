# SheetMind

SheetMind é um SaaS para diagnóstico inteligente de planilhas e documentos financeiros. Esta versão inclui a base para utilização de agentes com CrewAI e estrutura inicial para integração com Docling.

## Instalação

### Back-end

```bash
cd backend
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

### Front-end

```bash
cd frontend
npm install
npm run dev
```

## Exemplos de uso da API

### Criar agente

```http
POST /agents
{
  "name": "Finance Bot",
  "description": "Auxilia na análise de planilhas",
  "objective": "Responder dúvidas financeiras",
  "context_files": ["demo.xlsx"]
}
```

### Perguntar ao agente

```http
POST /agents/{agent_id}/ask
{
  "question": "Qual o lucro deste mês?"
}
```

As respostas ainda são simuladas, mas a estrutura está pronta para evolução com CrewAI e Docling.
