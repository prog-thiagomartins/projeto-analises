"""Application entry point and router registration."""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .api.v1.agent_router import router as agent_router
from .api.v1.document_router import router as document_router

app = FastAPI(title="SheetMind API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(agent_router, prefix="/agents", tags=["agents"])
app.include_router(document_router, prefix="/documents", tags=["documents"])


@app.get("/")
def read_root():
    return {"message": "Welcome to SheetMind"}
