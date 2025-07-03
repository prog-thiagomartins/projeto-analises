import { useState } from 'react'
import { useParams } from 'react-router-dom'
import { useStore } from '../store'

function Chat() {
  const { id } = useParams()
  const agent = useStore(s => s.agents.find(a => a.id === id))
  const [question, setQuestion] = useState('')
  const [answer, setAnswer] = useState('')

  const ask = async () => {
    const res = await fetch(`/agents/${id}/ask`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ question })
    })
    const data = await res.json()
    setAnswer(data.answer)
  }

  if (!agent) return <div className="p-4">Agente não encontrado.</div>

  return (
    <div className="p-4 space-y-4">
      <h1 className="text-xl">Chat com {agent.name}</h1>
      <textarea className="border p-2 w-full" value={question} onChange={e => setQuestion(e.target.value)} />
      <button className="bg-blue-600 text-white px-4 py-2" onClick={ask}>Perguntar</button>
      {answer && <div className="border p-2">{answer}</div>}
    </div>
  )
}

export default Chat
