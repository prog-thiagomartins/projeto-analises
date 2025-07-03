import { BrowserRouter as Router, Routes, Route, Link } from 'react-router-dom'
import Dashboard from './Dashboard'
import Chat from './Chat'

function App() {
  return (
    <Router>
      <nav className="p-4 bg-blue-600 text-white">
        <Link to="/">SheetMind</Link>
      </nav>
      <Routes>
        <Route path="/" element={<Dashboard />} />
        <Route path="/chat/:id" element={<Chat />} />
      </Routes>
    </Router>
  )
}

export default App
