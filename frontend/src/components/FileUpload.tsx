import { useRef } from 'react'
import { uploadContext } from '../services/api'

interface Props {
  agentId: string
  onUploaded?: (names: string[]) => void
}

export default function FileUpload({ agentId, onUploaded }: Props) {
  const inputRef = useRef<HTMLInputElement>(null)

  const handleUpload = async () => {
    const files = Array.from(inputRef.current?.files || [])
    if (!files.length) return
    const docs = await uploadContext(agentId, files)
    if (onUploaded) onUploaded(docs.map((d: any) => d.name))
    if (inputRef.current) inputRef.current.value = ''
  }

  return (
    <div className="space-y-2">
      <input ref={inputRef} type="file" multiple className="border p-2" />
      <button className="bg-green-600 text-white px-4 py-2" onClick={handleUpload}>
        Enviar Arquivos
      </button>
    </div>
  )
}
