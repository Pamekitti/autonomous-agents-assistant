# Autonomous Agents Assistant

A multi-agent system that uses specialized AI agents to handle different types of tasks through smart routing and handoffs.

## Overview

This system has different AI agents working together:
- **Triage Agent**: Routes requests to the right specialist
- **Knowledge Agent**: Handles information and explanations
- **Deep Thought Agent**: Tackles complex problems
- **Web Search Agent**: Does web research
- **Analyst Agent**: Handles data analysis

## Setup

1. Clone the repository:
```bash
git clone https://github.com/yourusername/autonomous-agents-assistant.git
cd autonomous-agents-assistant
```

2. Install requirements:
```bash
pip install -r requirements.txt
```

3. Set up environment variables in `.env`:
```bash
# OpenAI Configuration
OPENAI_API_KEY=your_openai_api_key
LOG_LEVEL=INFO

# Memory Management
MEMORY_CLEANUP_INTERVAL=3600
MAX_SHORT_TERM_MEMORIES=1000
AGENT_TIMEOUT=300

# API Keys and Configuration
DUCKDUCKGO_API_KEY=your_api_key_here
MAX_CODE_EXECUTION_TIME=30
MAX_SEARCH_RESULTS=3
ENABLE_CODE_EXECUTION=true
ENABLE_WEB_SEARCH=true
```

## Usage

Run the assistant:
```bash
python main.py
```

## Project Structure
```
├── main.py           # Entry point
├── models.py         # Data models
├── agents.py         # Agent definitions
├── agent_runner.py   # Agent execution logic
└── tools/           # Agent tools
    ├── web_search.py
    ├── code_execution.py
    └── data_analysis.py
```
