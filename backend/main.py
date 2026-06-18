from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers import project_plan, documents

app = FastAPI(
    title="PreSalesAI API",
    description="Système d'automatisation des plans de projet",
    version="1.0.0"
)

# Configuration CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Inclure les routers
app.include_router(project_plan.router, prefix="/api/project", tags=["Project Plan"])
app.include_router(documents.router, prefix="/api/documents", tags=["Documents"])

@app.get("/")
async def root():
    return {"status": "ok", "service": "PreSalesAI"}

@app.get("/health")
async def health():
    return {"status": "healthy"}