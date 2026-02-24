from fastapi import FastAPI, WebSocket
from fastapi.middleware.cors import CORSMiddleware
from websocket_manager import manager
from ai_service import generate_insight
from advanced_analytics import AnalyticsEngine
import pandas as pd

app = FastAPI(title="VisioSphere Backend")

engine = AnalyticsEngine()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def health():
    return {"status": "VisioSphere Backend Running"}

@app.post("/ai-insight")
async def ai_insight(data: dict):
    prompt = data.get("prompt")
    response = generate_insight(prompt)
    return {"response": response}

@app.post("/analytics/clustering")
async def clustering(data: dict):
    df = pd.DataFrame(data["values"])
    labels = engine.clustering(df)
    return {"clusters": labels}

@app.post("/analytics/predict")
async def prediction(data: dict):
    X = pd.DataFrame(data["X"])
    y = pd.Series(data["y"])
    predictions = engine.prediction(X, y)
    return {"predictions": predictions}

@app.websocket("/ws/{client_id}")
async def websocket_endpoint(websocket: WebSocket, client_id: str):
    await manager.connect(websocket, client_id)
    try:
        while True:
            data = await websocket.receive_text()
            await manager.broadcast(data)
    except:
        manager.disconnect(client_id)
