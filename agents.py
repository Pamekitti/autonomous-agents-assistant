from models import Agent

# Tool functions
def escalate_to_human(summary: str):
    print("Escalating to human agent...")
    print("\n=== Escalation Report ===")
    print(f"Summary: {summary}")
    print("=========================\n")
    exit()

def execute_order(product: str, price: int):
    print("\n=== Order Summary ===")
    print(f"Product: {product}")
    print(f"Price: ${price}")
    print("=================\n")
    confirm = input("Confirm order? y/n: ").strip().lower()
    return "Success" if confirm == "y" else "User cancelled order."

def look_up_item(search_query: str):
    item_id = "item_132612938"
    print("Found item:", item_id)
    return item_id

def execute_refund(item_id: str, reason: str = "not provided"):
    print("\n=== Refund Summary ===")
    print(f"Item ID: {item_id}")
    print(f"Reason: {reason}")
    print("=================\n")
    print("Refund execution successful!")
    return "success"

# Transfer functions
def transfer_to_sales_agent():
    return sales_agent

def transfer_to_issues_and_repairs():
    return issues_and_repairs_agent

def transfer_back_to_triage():
    return triage_agent

# Agent definitions
triage_agent = Agent(
    name="Triage Agent",
    instructions=(
        "You are a customer service bot for ACME Inc. "
        "Introduce yourself. Always be very brief. "
        "Gather information to direct the customer to the right department. "
        "But make your questions subtle and natural."
    ),
    tools=[transfer_to_sales_agent, transfer_to_issues_and_repairs, escalate_to_human],
)

sales_agent = Agent(
    name="Sales Agent",
    instructions=(
        "You are a sales agent for ACME Inc. "
        "Always answer in a sentence or less. "
        "Follow the following routine with the user: "
        "1. Ask them about any problems in their life related to catching roadrunners.\n"
        "2. Casually mention one of ACME's crazy made-up products can help.\n"
        "3. Once the user is bought in, drop a ridiculous price.\n"
        "4. Only after everything, and if the user says yes, "
        "tell them a crazy caveat and execute their order."
    ),
    tools=[execute_order, transfer_back_to_triage],
)

issues_and_repairs_agent = Agent(
    name="Issues and Repairs Agent",
    instructions=(
        "You are a customer support agent for ACME Inc. "
        "Always answer in a sentence or less. "
        "Follow the following routine with the user: "
        "1. First, ask probing questions and understand the user's problem deeper.\n"
        "2. Propose a fix (make one up).\n"
        "3. ONLY if not satisfied, offer a refund.\n"
        "4. If accepted, search for the ID and then execute refund."
    ),
    tools=[execute_refund, look_up_item, transfer_back_to_triage],
) 