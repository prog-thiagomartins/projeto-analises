import { create } from 'zustand'

export interface Agent {
  id: string
  name: string
  description: string
  objective: string
  context_files: string[]
}

interface Store {
  agents: Agent[]
  setAgents: (agents: Agent[]) => void
}

export const useStore = create<Store>((set) => ({
  agents: [],
  setAgents: (agents) => set({ agents })
}))
