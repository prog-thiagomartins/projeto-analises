#!/bin/bash
# Setup script for SheetMind project
# This script will prepare backend and frontend dependencies
set -e

# Backend setup
if [ ! -d "backend/.venv" ]; then
  python3 -m venv backend/.venv
fi
source backend/.venv/bin/activate
pip install --upgrade pip
pip install -r backend/requirements.txt

deactivate

# Frontend setup
cd frontend
npm install
cd ..

echo "Setup complete."

