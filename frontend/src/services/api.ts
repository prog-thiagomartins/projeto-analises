export interface AgentCreate {
  name: string;
  description: string;
  objective: string;
}

export interface Question {
  question: string;
}

const BASE_URL = '';

export async function listAgents() {
  const res = await fetch(`${BASE_URL}/agents`);
  return res.json();
}

export async function createAgent(data: AgentCreate) {
  const res = await fetch(`${BASE_URL}/agents`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(data),
  });
  return res.json();
}

export async function getAgent(id: string) {
  const res = await fetch(`${BASE_URL}/agents/${id}`);
  return res.json();
}

export async function uploadContext(id: string, files: File[]) {
  const form = new FormData();
  files.forEach(f => form.append('files', f));
  const res = await fetch(`${BASE_URL}/agents/${id}/context`, {
    method: 'POST',
    body: form,
  });
  return res.json();
}

export async function askAgent(id: string, question: string) {
  const res = await fetch(`${BASE_URL}/agents/${id}/ask`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ question }),
  });
  return res.json();
}
