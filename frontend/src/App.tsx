import { BrowserRouter as Router, Routes, Route, Navigate, Link } from 'react-router-dom'
import AgentsPage from './pages/AgentsPage'
import AgentDetailPage from './pages/AgentDetailPage'

export default function App() {
  return (
    <Router>
      <nav className="p-4 bg-blue-600 text-white mb-4">
        <Link to="/agentes" className="font-bold">SheetMind</Link>
      </nav>
      <Routes>
        <Route path="/" element={<Navigate to="/agentes" replace />} />
        <Route path="/agentes" element={<AgentsPage />} />
        <Route path="/agentes/:id" element={<AgentDetailPage />} />
      </Routes>
    </Router>
  )
}
