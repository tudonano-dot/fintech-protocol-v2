from google import genai
from google.genai import types
import json
import os
import time

# ==============================================================================
# 1. CONFIGURATION (V2 ENGINE)
# ==============================================================================
# PASTE YOUR KEY HERE
API_KEY = "YOUR_GEMINI_API_KEY"
MODEL_ID = "gemini-3-flash-preview" # The Modern Engine

client = genai.Client(api_key=API_KEY)

# ==============================================================================
# 2. THE REFACTORING KERNEL (IMPROVED LOGIC)
# ==============================================================================
REFACTOR_INSTRUCTION = """
<role>
You are the GEMINI 3 MIGRATION ENGINE.
Rewrite "Legacy Prompts" (GPT-4/Claude) into "Gemini 3 Native Specifications".
</role>

<rules>
1. **PHYSICS SHIFT (CRITICAL):**
   - Legacy prompts often ask for "Low Temp" or "Robotic" tone.
   - GEMINI 3 REQUIREMENT: **Force Temperature 1.0**.
   - INSTRUCTION: You must output a config block setting `temperature: 1.0`.
   - REASONING: "Gemini 3 degrades at low temperatures. High entropy required for reasoning."

2. **STRUCTURE ENFORCEMENT:**
   - Convert text into XML Tags: <role>, <constraints>, <task>.
   - Use Positive Constraints ("Focus on X") instead of Negative ("Don't do Y").

3. **THINKING PROTOCOL:**
   - Add a mandatory instruction: "Before answering, plan the logic step-by-step."
</rules>

<output_format>
JSON ONLY:
{
  "legacy_issues": ["List of errors (e.g., 'Low Temp detected')"],
  "migrated_prompt": "The full, ready-to-use Gemini 3 System Prompt (Markdown)",
  "config_suggestion": {"temperature": 1.0, "topP": 0.95}
}
</output_format>
"""

# ==============================================================================
# 3. THE MIGRATION FUNCTION
# ==============================================================================
def migrate_prompt(legacy_text):
    print(f"\n--- 🏗️ INGESTING LEGACY PROMPT ({len(legacy_text)} chars) ---")

    try:
        response = client.models.generate_content(
            model=MODEL_ID,
            contents=f"LEGACY PROMPT TO REFACTOR:\n{legacy_text}",
            config=types.GenerateContentConfig(
                system_instruction=REFACTOR_INSTRUCTION,
                response_mime_type="application/json",
                temperature=0.0
            )
        )

        data = json.loads(response.text)

        print("\n[ANALYSIS COMPLETE]")
        print(f"❌ ISSUES DETECTED: {data['legacy_issues']}")
        
        print("\n[MIGRATED CONFIG]")
        print(json.dumps(data['config_suggestion'], indent=2))

        print("\n[PREVIEW OF OPTIMIZED PROMPT]")
        print(data['migrated_prompt'][:200] + "...\n(Full prompt saved to file)")

        # Save to file (The Deliverable)
        filename = "gemini_3_optimized.md"
        with open(filename, "w") as f:
            f.write(data['migrated_prompt'])

        print(f"\n>> ✅ SUCCESS. Artifact saved to '{filename}'")
        
        # Print content for User Verification
        print("\n--- 📄 FULL FILE CONTENT ---")
        print(data['migrated_prompt'])

    except Exception as e:
        print(f"❌ CRITICAL FAILURE: {e}")

# ==============================================================================
# 4. EXECUTION
# ==============================================================================
if __name__ == "__main__":
    print(f"*** ACTIVATING MIGRATION SERVICE ({MODEL_ID}) ***")
    
    # DEFAULT TEST PAYLOAD (The "Bad" Prompt)
    default_payload = """
    SYSTEM: You are a financial analyst bot.
    INSTRUCTIONS:
    1. Analyze the attached bank statement.
    2. Be very strict and robotic.
    3. OUTPUT FORMAT: Just give me the numbers.
    SETTINGS: Use Temperature 0.1 because I need accuracy.
    CONSTRAINTS: Do not talk to the user. Do not explain your reasoning.
    """
    
    migrate_prompt(default_payload)
