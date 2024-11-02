from pydantic import BaseModel
from typing import Optional, List, Any
from dotenv import load_dotenv

load_dotenv()

class Agent(BaseModel):
    name: str = "Agent"
    model: str = "gpt-4o-mini"
    instructions: str = "You are a helpful Agent"
    tools: List[Any] = []

class Response(BaseModel):
    agent: Optional[Agent]
    messages: list 