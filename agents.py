from models import Agent
from typing import Dict, Any
from tools.web_search import web_search
from tools.code_execution import execute_code
from tools.data_analysis import analyze_data

# Agent instructions
TRIAGE_INSTRUCTIONS = """You are the primary triage agent for an advanced AI assistant system.
Your role is to:
1. Direct web-related queries to the web search agent using transfer_to_web()
2. Send data analysis tasks to the analyst agent using transfer_to_analyst()
3. Route knowledge-heavy questions to the knowledge agent using transfer_to_knowledge()
4. Direct complex reasoning tasks to the deep thought agent using transfer_to_deep_thought()
Handle simple queries directly. Be concise but friendly."""

KNOWLEDGE_INSTRUCTIONS = """You are a comprehensive knowledge agent.
Your role is to:
1. Provide accurate, detailed information on topics
2. Use web_search when you need to verify or update information
3. Transfer to web search agent (transfer_to_web) for extensive web research
4. Acknowledge uncertainties and limitations in your knowledge
5. Break down complex topics into understandable parts"""

DEEP_THOUGHT_INSTRUCTIONS = """You are a problem-solving specialist.
Your role is to:
1. Break down complex problems methodically
2. Use execute_code for computational tasks
3. Use analyze_data for data-driven insights
4. Transfer to analyst (transfer_to_analyst) for deep data analysis
5. Explain your reasoning process clearly"""

WEB_SEARCH_INSTRUCTIONS = """You are a web search specialist.
Your role is to:
1. Use web_search to find current information
2. Verify information across multiple sources
3. Transfer to knowledge agent (transfer_to_knowledge) for deep understanding
4. Always cite sources
5. Synthesize information clearly"""

ANALYST_INSTRUCTIONS = """You are a data analysis specialist.
Your role is to:
1. Use analyze_data for statistical analysis
2. Use execute_code for data processing
3. Create clear data visualizations
4. Provide data-driven recommendations
5. Explain technical concepts in simple terms"""

# Transfer functions
def transfer_to_web() -> Agent:
    """Transfer control to the web search specialist"""
    return web_search_agent

def transfer_to_analyst() -> Agent:
    """Transfer control to the data analysis specialist"""
    return analyst_agent

def transfer_to_knowledge() -> Agent:
    """Transfer control to the knowledge specialist"""
    return knowledge_agent

def transfer_to_deep_thought() -> Agent:
    """Transfer control to the deep thinking specialist"""
    return deep_thought_agent

# Update agent definitions with specific transfer functions
triage_agent = Agent(
    name="Triage Agent",
    model="gpt-4o-mini",
    instructions=TRIAGE_INSTRUCTIONS,
    tools=[transfer_to_web, transfer_to_analyst, 
           transfer_to_knowledge, transfer_to_deep_thought]
)

knowledge_agent = Agent(
    name="Knowledge Agent",
    model="gpt-4o",
    instructions=KNOWLEDGE_INSTRUCTIONS,
    tools=[web_search, transfer_to_web]  # Can transfer to web for additional searches
)

deep_thought_agent = Agent(
    name="Deep Thought Agent",
    model="gpt-4o",
    instructions=DEEP_THOUGHT_INSTRUCTIONS,
    tools=[execute_code, analyze_data, transfer_to_analyst]  # Can transfer to analyst
)

web_search_agent = Agent(
    name="Web Search Agent",
    model="gpt-4o-mini",
    instructions=WEB_SEARCH_INSTRUCTIONS,
    tools=[web_search, transfer_to_knowledge]  # Can transfer to knowledge for interpretation
)

analyst_agent = Agent(
    name="Analyst Agent",
    model="gpt-4o",
    instructions=ANALYST_INSTRUCTIONS,
    tools=[analyze_data, execute_code]  # No transfers needed for analyst
) 