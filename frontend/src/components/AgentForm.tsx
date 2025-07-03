import { useState } from 'react'
import { createAgent, AgentCreate } from '../services/api'
import { useNavigate } from 'react-router-dom'

interface Props {
  onCreated?: (id: string) => void
}

export default function AgentForm({ onCreated }: Props) {
  const [form, setForm] = useState<AgentCreate>({ name: '', description: '', objective: '' })
  const navigate = useNavigate()

  const submit = async () => {
    const agent = await createAgent(form)
    if (onCreated) onCreated(agent.id)
    else navigate(`/agentes/${agent.id}`)
  }

  return (
    <div className="space-y-2">
      <input
        className="border p-2 w-full"
        placeholder="Nome"
        value={form.name}
        onChange={e => setForm({ ...form, name: e.target.value })}
      />
      <input
        className="border p-2 w-full"
        placeholder="Descrição"
        value={form.description}
        onChange={e => setForm({ ...form, description: e.target.value })}
      />
      <input
        className="border p-2 w-full"
        placeholder="Objetivo"
        value={form.objective}
        onChange={e => setForm({ ...form, objective: e.target.value })}
      />
      <button className="bg-blue-600 text-white px-4 py-2" onClick={submit}>
        Criar Agente
      </button>
    </div>
  )
}
