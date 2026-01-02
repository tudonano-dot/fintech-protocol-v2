# 🛡️ Constitutional Dispatcher (Gemini 3 Architecture)

**Status:** Production Prototype  
**Engine:** Google Gemini 3 Flash Preview (Temp 0.1)  
**Latency:** ~1.9s (Cloud/Python) / Target: <400ms (Edge)

### ⚡ The Problem
High-volume Fintech platforms face a "Triage Bottleneck." Human agents are overwhelmed by password resets, causing them to miss critical fraud alerts.

### 🧠 The Solution
A **Constitutional Routing Agent** that sits between the User and the Support Team. It uses a "Zero-Tolerance" safety layer to detect fraud semantics before routing.

### 🏗️ Architecture
- **Layer 1 (Ingest):** Raw User Query.
- **Layer 2 (Safety):** Regex + Semantic Fraud Detection (Constitutional Guardrails).
- **Layer 3 (Route):** - `Agent_Flash` (Low Cost) -> FAQs
  - `Agent_Pro` (High Reasoning) -> Transaction Analysis
  - `Agent_Human` (High Priority) -> Fraud/Risk Escalation

### 🧪 Performance Logs (Simulation)
> **Input:** "ALERT! UNKNOWN DEVICE LOGGED IN AND DRAINED FUNDS!"
> **Logic:** Detected keywords indicating unauthorized access and potential fraud.
> **Route:** HUMAN [High Urgency]

### 🚀 Usage
This protocol is designed for integration into Intercom/Zendesk APIs or custom Python backends.
