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

### Enviar arquivos de contexto para um agente

```http
POST /agents/{agent_id}/context
Content-Type: multipart/form-data
files: [planilha.xlsx, relatorio.pdf]
```

### Estrutura de agente com documentos associados

```json
{
  "id": "123",
  "name": "Finance Bot",
  "description": "Auxilia na análise de planilhas",
  "objective": "Responder dúvidas financeiras",
  "context_files": ["planilha.xlsx", "relatorio.pdf"],
  "context_docs": ["doc1", "doc2"]
}
```

### Pergunta considerando o contexto

```http
POST /agents/{agent_id}/ask
{
  "question": "Liste os totais presentes na planilha"
}
```
