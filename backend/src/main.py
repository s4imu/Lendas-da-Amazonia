import uvicorn
from fastapi import FastAPI
import auth.routes
import user.routes

app = FastAPI(title="Lendas das Amazônia", description="Backend do projeto Lendas da Amazônia", version="0.0.1",)

app.include_router(auth.routes.router, tags=["auth"])
app.include_router(user.routes.router, tags=["user"])

if __name__ == "__main__":
    uvicorn.run("main:app", port=5000, log_level="info", reload=True) # Desenvolvimento Apenas

