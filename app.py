from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Dict, Any, Optional
import uvicorn

from models import Action, Observation, Reward, State
from env import EmailTriageEnv

app = FastAPI(title="Email Triage - Enterprise Email Management")
env = EmailTriageEnv()

class ResetRequest(BaseModel):
    task_id: str = "easy"

class StepResponse(BaseModel):
    observation: Observation
    reward: Reward
    done: bool
    info: Dict[str, Any]

@app.post("/reset", response_model=Observation)
async def reset(req: Optional[ResetRequest] = None):
    task_id = req.task_id if req else "easy"
    try:
        return env.reset(task_id=task_id)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.post("/step", response_model=StepResponse)
async def step(action: Action):
    obs, reward, done, info = env.step(action)
    return StepResponse(
        observation=obs,
        reward=reward,
        done=done,
        info=info
    )

@app.get("/state", response_model=State)
async def state():
    return env.state()

def main():
    """Entry point for the application"""
    uvicorn.run(app, host="0.0.0.0", port=8000)

if __name__ == "__main__":
    main()
