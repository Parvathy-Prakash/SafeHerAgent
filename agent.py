from google.adk.agents.llm_agent import Agent
import threading

# ---------------- MOCK FUNCTIONS ----------------
def call_emergency(numbers):
    for number in numbers:
        print(f"[SYSTEM]: Emergency call initiated to {number}")

def send_location_to_control(location):
    print(f"[SYSTEM]: Location sent to control room: {location}")

def get_real_time_location():
    return {"lat": "12.9716", "lng": "77.5946"}

def camera_on():
    print("[SYSTEM]: Camera activated!")

# ---------------- EMERGENCY KEYWORDS ----------------
EMERGENCY_KEYWORDS = ["help", "emergency", "danger", "followed", "attack"]

# ---------------- AGENT INSTANCE ----------------
root_agent = Agent(
    model="gemini-2.5-flash",
    name="SafeHer",
    description="Women safety assistant that detects danger and helps in emergencies.",
    instruction=(
        "You are SafeHer. Detect danger, alert authorities, send location, "
        "and activate camera when emergency is detected."
    )
)

# ---------------- HELPER FUNCTION ----------------
def safeher_response(message: str) -> str:
    """
    This function wraps root_agent and adds emergency handling.
    """
    msg_lower = message.lower()
    if any(k in msg_lower for k in EMERGENCY_KEYWORDS):
        location = get_real_time_location()
        threading.Thread(target=send_location_to_control, args=(location,)).start()
        threading.Thread(target=call_emergency, args=(["112", "1091"],)).start()
        threading.Thread(target=camera_on).start()
        return "[SafeHer]: ⚠️ Emergency triggered! Authorities are on their way."
    
    # fallback to default agent behavior
    return root_agent.respond(message)
