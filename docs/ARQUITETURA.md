# Arquitetura do SheetMind

Este documento descreve a organização dos módulos do back-end e o fluxo de dados utilizado para que os agentes consigam responder perguntas a partir de arquivos enviados pelos usuários.

## Módulos do back-end

- **api** – rotas FastAPI agrupadas por versão. Cada rota delega a lógica para os serviços.
- **services** – camada de regras de negócio. `AgentService` e `DocumentService` mantêm os dados em memória e coordenam o uso dos parsers.
- **models** – modelos Pydantic compartilhados entre rotas e serviços.
- **parsers** – implementação de leitores de arquivos (CSV, Excel e PDF) com retorno em estruturas do Docling.
- **agents** e **interactions** – exemplos de rotas simples sem a divisão por versão, mantidos por compatibilidade.

## Fluxo de dados

```text
Upload -> DocumentService.parse_file -> Docling structures -> association to Agent -> AgentService.ask_agent -> response
```

1. O usuário envia arquivos via `/agents/{id}/context`.
2. `AgentService` utiliza `DocumentService` para escolher o parser apropriado e gerar estruturas Docling.
3. O identificador dos documentos é salvo no agente para futuras consultas.
4. Ao receber uma pergunta (`/agents/{id}/ask`), o serviço recupera os documentos do agente e, caso CrewAI esteja instalado, inicia a execução do agente. Caso contrário, é retornada uma resposta simulada.

## Escalabilidade e modularidade

- A separação por serviços facilita a troca de implementações (por exemplo, armazenar documentos em banco de dados no futuro).
- Parsers seguem uma interface única (`BaseParser`), permitindo adicionar novos formatos de forma isolada.
- O front-end foi criado com Vite e organizado em páginas, componentes reutilizáveis e uma store global simples via Zustand.

## Organização do front-end

- `pages/` – páginas acessadas pelas rotas React Router.
- `components/` – componentes reutilizáveis como formulários, chat e upload.
- `services/` – funções de chamada à API.
- `store.ts` – estado global minimalista para lista de agentes.

Com essa base é possível evoluir o projeto adicionando autenticação, persistência em banco e agentes mais complexos sem grandes mudanças estruturais.
