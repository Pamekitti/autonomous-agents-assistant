from pydantic import BaseModel
from typing import Optional, List, Any, Dict
from dotenv import load_dotenv
import os

load_dotenv()

class Agent(BaseModel):
    name: str
    model: str
    instructions: str
    tools: List[Any]
    memory: Dict[str, Any] = {}  # For maintaining context
    
    class Config:
        arbitrary_types_allowed = True

class ChatMessage(BaseModel):
    role: str
    content: str
    name: Optional[str] = None
    
class ChatCompletionResponse(BaseModel):
    id: str
    object: str
    created: int
    model: str
    choices: List[Dict[str, Any]]
    usage: Dict[str, int]

    def get_message_content(self) -> str:
        """Extract the message content from the first choice"""
        return self.choices[0]["message"]["content"]

class Response(BaseModel):
    agent: Optional[Agent]
    messages: List[Dict[str, str]]  # Each message must have 'role' and 'content' keys, optionally 'name'
    context: Dict[str, Any] = {}  # For passing context between agents