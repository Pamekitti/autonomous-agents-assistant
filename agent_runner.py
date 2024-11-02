from typing import Dict, Any
import json
from openai import OpenAI
from models import Agent, Response
import inspect
from typing import get_type_hints

client = OpenAI()

def function_to_schema(func):
    """Convert a Python function to an OpenAI tool schema"""
    signature = inspect.signature(func)
    doc = inspect.getdoc(func) or ""
    type_hints = get_type_hints(func)
    
    parameters = {}
    required = []
    
    for name, param in signature.parameters.items():
        param_type = type_hints.get(name, str)
        param_schema = {"type": "string"}  # Default to string
        
        if param_type == int:
            param_schema = {"type": "integer"}
        elif param_type == float:
            param_schema = {"type": "number"}
        elif param_type == bool:
            param_schema = {"type": "boolean"}
            
        if param.default == param.empty:
            required.append(name)
            
        parameters[name] = param_schema
    
    return {
        "type": "function",
        "function": {
            "name": func.__name__,
            "description": doc,
            "parameters": {
                "type": "object",
                "properties": parameters,
                "required": required
            }
        }
    }

def run_full_turn(agent: Agent, messages: list) -> Response:
    current_agent = agent
    num_init_messages = len(messages)
    messages = messages.copy()

    while True:
        # Convert tools to schemas and create reverse mapping
        tool_schemas = [function_to_schema(tool) for tool in current_agent.tools]
        tools = {tool.__name__: tool for tool in current_agent.tools}

        # Get OpenAI completion
        response = client.chat.completions.create(
            model=agent.model,
            messages=[{"role": "system", "content": current_agent.instructions}] + messages,
            tools=tool_schemas or None,
        )
        message = response.choices[0].message
        messages.append(message)

        if message.content:
            print(f"{current_agent.name}:", message.content)

        if not message.tool_calls:
            break

        # Handle tool calls
        for tool_call in message.tool_calls:
            result = execute_tool_call(tool_call, tools, current_agent.name)

            if isinstance(result, Agent):  # Handle agent transfer
                current_agent = result
                result = f"Transfered to {current_agent.name}. Adopt persona immediately."

            result_message = {
                "role": "tool",
                "tool_call_id": tool_call.id,
                "content": result,
            }
            messages.append(result_message)

    return Response(agent=current_agent, messages=messages[num_init_messages:])

def execute_tool_call(tool_call, tools: Dict, agent_name: str) -> Any:
    name = tool_call.function.name
    args = json.loads(tool_call.function.arguments)

    print(f"{agent_name}:", f"{name}({args})")

    return tools[name](**args) 