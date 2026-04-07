from pydantic import BaseModel, Field
from typing import List, Optional, Literal

class Action(BaseModel):
    action_type: Literal["archive", "forward", "reply"] = Field(..., description="The action to take on the current email.")
    target_email: Optional[str] = Field(None, description="The email address to forward to (required if action_type is forward).")
    draft_body: Optional[str] = Field(None, description="The body of the reply (required if action_type is reply).")

class Email(BaseModel):
    id: str
    sender: str
    subject: str
    body: str

class Observation(BaseModel):
    current_email: Optional[Email] = Field(None, description="The current email to process. Null if inbox is empty.")
    inbox_count: int = Field(..., description="Number of emails remaining in the inbox after this one.")
    policy_snippets: str = Field(..., description="Company policies the agent should refer to.")

class Reward(BaseModel):
    score: float = Field(..., description="Score between 0.0 and 1.0 representing task success.")

class State(BaseModel):
    emails_processed: int
    emails_total: int
    current_task: str
