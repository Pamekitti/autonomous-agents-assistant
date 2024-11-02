from agent_runner import run_full_turn
from agents import triage_agent
from typing import List, Dict
import logging

def setup_logging():
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s'
    )

def main():
    setup_logging()
    agent = triage_agent
    messages: List[Dict[str, str]] = []
    
    logging.info("Starting personal assistant system")
    print("Welcome to Personal Assistant! (Type 'quit' to exit, 'reset' to start over)")
    
    while True:
        # try:
            user_input = input("User: ").strip()
            if user_input.lower() == 'quit':
                logging.info("User requested to quit")
                break
            elif user_input.lower() == 'reset':
                messages = []
                logging.info("Conversation reset")
                print("Conversation history cleared. Starting fresh!")
                continue
            
            if not user_input:
                print("Please enter a valid input.")
                continue
                
            messages.append({"role": "user", "content": user_input})
            
            response = run_full_turn(agent, messages)
            agent = response.agent
            messages.extend(response.messages)
            
        # except KeyboardInterrupt:
        #     print("\nGoodbye!")
        #     break
        # except Exception as e:
        #     logging.error(f"Error occurred: {str(e)}")
        #     print("An error occurred. Please try again.")

if __name__ == "__main__":
    main() 