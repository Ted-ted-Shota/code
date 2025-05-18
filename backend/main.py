import asyncio
from fastapi import FastAPI

app = FastAPI()

@app.on_event("startup")
async def startup_event():
    asyncio.create_task(initialize_plugins())

async def initialize_plugins():
    """Load heavy plugins in the background."""
    # TODO: replace with actual plugin initialization logic
    await asyncio.sleep(5)  # Simulate heavy work
    print("Plugins initialized")

@app.get("/")
async def read_root():
    return {"status": "ok"}

