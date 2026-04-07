from typing import Tuple, Dict, Any, Optional
from models import Action, Observation, Reward, State, Email
from data import TASKS, POLICY_SNIPPETS
from graders import grade_action

class EmailTriageEnv:
    def __init__(self):
        self.current_task: Optional[str] = None
        self.emails: list = []
        self.current_step = 0
        self.total_emails = 0
        self.score = 0.0

    def reset(self, task_id: str = "easy") -> Observation:
        if task_id not in TASKS:
            raise ValueError(f"Unknown task {task_id}")
            
        self.current_task = task_id
        self.emails = list(TASKS[task_id])
        self.total_emails = len(self.emails)
        self.current_step = 0
        self.score = 0.0
        
        return self._get_obs()

    def step(self, action: Action) -> Tuple[Observation, Reward, bool, Dict[str, Any]]:
        if self.current_step >= self.total_emails:
            return self._get_obs(), Reward(score=0.0), True, {"error": "Episode already done."}

        current_item = self.emails[self.current_step]
        truth = current_item["truth"]
        
        step_score = grade_action(action, truth)
        self.score += step_score
        
        self.current_step += 1
        done = self.current_step >= self.total_emails
        
        final_score = self.score / self.total_emails if self.total_emails > 0 else 0.0
        
        # Reward partial progress
        reward = Reward(score=step_score / self.total_emails)
        
        return self._get_obs(), reward, done, {"step_score": step_score, "cumulative_score": final_score}

    def state(self) -> State:
        return State(
            emails_processed=self.current_step,
            emails_total=self.total_emails,
            current_task=self.current_task or "none"
        )

    def _get_obs(self) -> Observation:
        if self.current_step < self.total_emails:
            current_email = self.emails[self.current_step]["email"]
            inbox_count = self.total_emails - self.current_step - 1
        else:
            current_email = None
            inbox_count = 0
            
        return Observation(
            current_email=current_email,
            inbox_count=inbox_count,
            policy_snippets=POLICY_SNIPPETS
        )
