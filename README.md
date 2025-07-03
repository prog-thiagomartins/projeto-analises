# SheetMind

SheetMind é uma aplicação SaaS que permite criar agentes inteligentes capazes de interpretar planilhas e documentos financeiros. Os arquivos enviados pelos usuários são processados pelo Docling e servem como contexto para agentes baseados em CrewAI responderem perguntas via chat.

## Tecnologias

- **FastAPI** – back‑end e APIs REST
- **CrewAI** – orquestração dos agentes de IA
- **Docling** – parsing e estruturação de arquivos
- **React + Vite** – front‑end SPA
- **TailwindCSS** – estilos

## Como executar localmente

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

### Script de preparação

Se preferir, utilize o script `setup.sh` na raiz do projeto para instalar todas
as dependências do back-end e do front-end de uma só vez:

```bash
./setup.sh
```

### Fluxo principal

1. **Upload** – o usuário seleciona arquivos relacionados ao agente.
2. **Processamento** – o back-end utiliza o Docling para ler os dados e associa o documento ao agente.
3. **Interação** – o usuário envia perguntas e o agente responde considerando o contexto dos arquivos enviados.

Para exemplos mais detalhados de requisições, consulte a documentação da API em `docs/ARQUITETURA.md`.
