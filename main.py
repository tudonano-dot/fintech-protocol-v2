from google import genai
from google.genai import types
import json
import time
import os

# --- CONFIGURATION ---
# NOTE: In production, use os.environ["GEMINI_API_KEY"]
# For this demo, the user must insert their key.
API_KEY = "YOUR_GEMINI_API_KEY_HERE" 
MODEL_ID = "gemini-3-flash-preview"

client = genai.Client(api_key=API_KEY)

# --- THE CONSTITUTIONAL ROUTER ---
DISPATCHER_SYSTEM_PROMPT = """
You are the FinFlux Global Dispatcher.
Your goal: ZERO LATENCY routing of financial queries.

PROTOCOL:
1. SECURITY SCAN: If keywords ["fraud", "stolen", "hacked", "unauthorized"] -> ROUTE: "HUMAN" (URGENCY: HIGH).
2. AUTHENTICATION: If keywords ["reset", "password", "login", "2fa"] -> ROUTE: "FLASH" (URGENCY: LOW).
3. TRANSACTIONAL: If keywords ["pending", "status", "transfer", "declined"] -> ROUTE: "PRO" (URGENCY: MED).

OUTPUT STRICT JSON:
{"reasoning": "Brief logic trace", "route_to": "FLASH/PRO/HUMAN", "urgency": "LOW/MED/HIGH"}
"""

def deploy_dispatcher(query):
    print(f"\n📨 INCOMING STREAM: '{query}'")
    start_time = time.perf_counter()
    
    try:
        response = client.models.generate_content(
            model=MODEL_ID,
            contents=query,
            config=types.GenerateContentConfig(
                system_instruction=DISPATCHER_SYSTEM_PROMPT,
                response_mime_type="application/json",
                temperature=0.1
            )
        )
        
        latency_ms = (time.perf_counter() - start_time) * 1000
        data = json.loads(response.text)
        
        print(f"⚡ LATENCY: {latency_ms:.1f}ms (Gemini 3 Flash)")
        print(f"🧠 LOGIC: {data['reasoning']}")
        print(f"🎯 TARGET: {data['route_to']}")
        
    except Exception as e:
        print(f"❌ KERNEL PANIC: {e}")

if __name__ == "__main__":
    print(f"--- 🟢 SYSTEMS ONLINE: CONNECTED TO {MODEL_ID} ---")
    deploy_dispatcher("I forgot my password again.")
    deploy_dispatcher("My transfer #9922 is pending for 3 days.")
    deploy_dispatcher("ALERT! UNKNOWN DEVICE LOGGED IN AND DRAINED FUNDS!")
