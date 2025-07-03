import { useState } from 'react'
import { askAgent } from '../services/api'

interface Props {
  agentId: string
}

export default function ChatBox({ agentId }: Props) {
  const [question, setQuestion] = useState('')
  const [messages, setMessages] = useState<{ q: string; a: string }[]>([])

  const send = async () => {
    if (!question) return
    const res = await askAgent(agentId, question)
    setMessages([...messages, { q: question, a: res.answer }])
    setQuestion('')
  }

  return (
    <div className="space-y-2">
      <div className="space-y-2">
        {messages.map((m, i) => (
          <div key={i} className="border p-2 rounded">
            <p className="font-semibold">Q: {m.q}</p>
            <p>A: {m.a}</p>
          </div>
        ))}
      </div>
      <textarea
        className="border p-2 w-full"
        value={question}
        onChange={e => setQuestion(e.target.value)}
      />
      <button className="bg-blue-600 text-white px-4 py-2" onClick={send}>
        Enviar
      </button>
    </div>
  )
}
