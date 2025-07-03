import { create } from 'zustand'

interface Agent {
  id: string
  name: string
  description: string
}

interface Store {
  agents: Agent[]
  setAgents: (agents: Agent[]) => void
}

export const useStore = create<Store>((set) => ({
  agents: [],
  setAgents: (agents) => set({ agents })
}))
