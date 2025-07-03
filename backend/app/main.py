from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .uploads.routes import router as upload_router
from .agents.routes import router as agent_router
from .interactions.routes import router as interaction_router

app = FastAPI(title="SheetMind API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(upload_router, prefix="/upload", tags=["uploads"])
app.include_router(agent_router, prefix="/agents", tags=["agents"])
app.include_router(interaction_router, prefix="/agents", tags=["interactions"])

@app.get("/")
def read_root():
    return {"message": "Welcome to SheetMind"}

