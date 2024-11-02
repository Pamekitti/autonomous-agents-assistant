from agent_runner import run_full_turn
from agents import triage_agent

def main():
    agent = triage_agent
    messages = []

    print("Welcome to ACME Customer Service! (Type 'quit' to exit)")
    
    while True:
        user_input = input("User: ")
        if user_input.lower() == 'quit':
            break
            
        messages.append({"role": "user", "content": user_input})

        response = run_full_turn(agent, messages)
        agent = response.agent
        messages.extend(response.messages)

if __name__ == "__main__":
    main() 