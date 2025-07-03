import { useEffect, useState } from 'react'
import { useParams } from 'react-router-dom'
import FileUpload from '../components/FileUpload'
import ChatBox from '../components/ChatBox'
import { getAgent } from '../services/api'
import { Agent } from '../store'

export default function AgentDetailPage() {
  const { id } = useParams()
  const [agent, setAgent] = useState<Agent | null>(null)
  const [files, setFiles] = useState<string[]>([])

  useEffect(() => {
    if (id) getAgent(id).then((data) => { setAgent(data); setFiles(data.context_files || []) })
  }, [id])

  if (!agent) return <div className="p-4">Carregando...</div>

  return (
    <div className="p-4 space-y-4">
      <h1 className="text-xl font-bold">{agent.name}</h1>
      <p>{agent.description}</p>
      <p className="italic">Objetivo: {agent.objective}</p>

      <div className="space-y-2">
        <h2 className="font-semibold">Arquivos de Contexto</h2>
        <ul className="list-disc ml-5">
          {files.map((f, i) => <li key={i}>{f}</li>)}
        </ul>
        <FileUpload agentId={agent.id} onUploaded={(names) => setFiles([...files, ...names])} />
      </div>

      <div className="space-y-2 border-t pt-4">
        <h2 className="font-semibold">Chat</h2>
        <ChatBox agentId={agent.id} />
      </div>
    </div>
  )
}
