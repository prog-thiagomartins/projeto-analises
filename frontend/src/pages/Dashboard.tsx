import { useEffect, useState } from 'react'
import { Link } from 'react-router-dom'
import { useStore } from '../store'

interface AgentInput {
  name: string
  description: string
  goals: string
}

function Dashboard() {
  const { agents, setAgents } = useStore()
  const [form, setForm] = useState<AgentInput>({ name: '', description: '', goals: '' })

  useEffect(() => {
    fetch('/agents').then(r => r.json()).then(setAgents)
  }, [setAgents])

  const createAgent = async () => {
    const res = await fetch('/agents', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ ...form, goals: form.goals.split(',') })
    })
    const data = await res.json()
    setAgents([...agents, data])
  }

  return (
    <div className="p-4">
      <h1 className="text-2xl mb-4">Agentes</h1>
      <ul className="mb-4 space-y-2">
        {agents.map(a => (
          <li key={a.id} className="border p-2 rounded">
            <Link className="text-blue-600" to={`/chat/${a.id}`}>{a.name}</Link>
          </li>
        ))}
      </ul>
      <div className="space-y-2">
        <input className="border p-2 w-full" placeholder="Nome" value={form.name} onChange={e => setForm({ ...form, name: e.target.value })} />
        <input className="border p-2 w-full" placeholder="Descrição" value={form.description} onChange={e => setForm({ ...form, description: e.target.value })} />
        <input className="border p-2 w-full" placeholder="Objetivos separados por vírgula" value={form.goals} onChange={e => setForm({ ...form, goals: e.target.value })} />
        <button className="bg-blue-600 text-white px-4 py-2" onClick={createAgent}>Criar Agente</button>
      </div>
    </div>
  )
}

export default Dashboard
