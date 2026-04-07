from models import Action
from typing import Dict, Any

def grade_action(action: Action, truth: Dict[str, Any]) -> float:
    # 0.0 or 1.0 scoring
    if action.action_type != truth["action_type"]:
        return 0.0
    
    if truth["action_type"] == "forward":
        if action.target_email == truth.get("target_email"):
            return 1.0
        return 0.0
        
    if truth["action_type"] == "reply":
        keyword = truth.get("keyword")
        if keyword and action.draft_body and keyword in action.draft_body:
            return 1.0
        return 0.0
        
    if truth["action_type"] == "archive":
        return 1.0

    return 0.0
