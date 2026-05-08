from fastapi import FastAPI
from app.api.agents.routes import router as agents_router
from app.api.teams.routes import router as team_router
from app.database import connect_to_mongo, close_mongo_connection
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# 🔥 CORS CONFIG
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(agents_router, prefix="/api/v1")
app.include_router(team_router, prefix="/api/v1")

@app.on_event("startup")
async def startup():
    await connect_to_mongo()

@app.on_event("shutdown")
async def shutdown():
    await close_mongo_connection()