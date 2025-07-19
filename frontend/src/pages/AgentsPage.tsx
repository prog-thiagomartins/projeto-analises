import { useEffect } from 'react'
import { Link } from 'react-router-dom'
import AgentForm from '../components/AgentForm'
import { listAgents } from '../services/api'
import { useStore } from '../store'

export default function AgentsPage() {
  const { agents, setAgents } = useStore()

  useEffect(() => {
    listAgents().then(data => {
      if (Array.isArray(data)) {
        setAgents(data)
      }
    })
  }, [setAgents])

  return (
    <div className="p-4 space-y-4">
      <h1 className="text-2xl font-bold">Agentes</h1>
      <ul className="space-y-2">
        {agents.map(a => (
          <li key={a.id} className="border p-2 rounded flex justify-between">
            <span>{a.name}</span>
            <Link className="text-blue-600" to={`/agentes/${a.id}`}>Abrir</Link>
          </li>
        ))}
      </ul>
      <div className="border-t pt-4">
        <h2 className="text-xl mb-2">Novo Agente</h2>
        <AgentForm />
      </div>
    </div>
  )
}
