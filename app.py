"""
Email Triage Server - FastAPI Application
Handles email triage tasks with OpenEnv Interface
"""

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Dict, Any, Optional
import uvicorn
import sys
import os

# Add parent directory to path for imports
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from models import Action, Observation, Reward, State
from env import EmailTriageEnv

# Initialize FastAPI app
app = FastAPI(
    title="Email Triage - Enterprise Email Management",
    description="Email triage and routing system using OpenEnv",
    version="1.0.0"
)

# Initialize environment
env = EmailTriageEnv()

# Request/Response Models
class ResetRequest(BaseModel):
    """Reset request body"""
    task_id: str = "easy"

class StepResponse(BaseModel):
    """Step response body"""
    observation: Observation
    reward: Reward
    done: bool
    info: Dict[str, Any]

# API Routes
@app.post("/reset", response_model=Observation, tags=["operations"])
async def reset(req: Optional[ResetRequest] = None):
    """
    Reset the environment and start a new episode
    
    Args:
        req: ResetRequest with optional task_id ("easy", "medium", "hard")
        
    Returns:
        Observation: Initial observation for the episode
    """
    task_id = req.task_id if req else "easy"
    try:
        return env.reset(task_id=task_id)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.post("/step", response_model=StepResponse, tags=["operations"])
async def step(action: Action):
    """
    Execute an action in the environment
    
    Args:
        action: Action to take (archive, forward, or reply)
        
    Returns:
        StepResponse: Observation, reward, done flag, and info
    """
    obs, reward, done, info = env.step(action)
    return StepResponse(
        observation=obs,
        reward=reward,
        done=done,
        info=info
    )

@app.get("/state", response_model=State, tags=["operations"])
async def state():
    """
    Get current environment state
    
    Returns:
        State: Current state including emails processed, total, and task
    """
    return env.state()

@app.get("/health", tags=["health"])
async def health():
    """Health check endpoint"""
    return {"status": "healthy", "service": "email-triage-server"}

def main():
    """Entry point for the application"""
    uvicorn.run(
        app,
        host="0.0.0.0",
        port=8000,
        log_level="info",
        access_log=True
    )

if __name__ == "__main__":
    main()
