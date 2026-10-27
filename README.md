# 🤖 AI-Driven Python Learning Journey

Welcome to the **AI-Driven Python Learning Journey**! This repository documents a structured, practical progression from Python fundamentals to building **Applied AI & Agentic Workflows**.

The primary objective is to move from fundamental scripting to building production-ready AI systems, intelligent RAG pipelines, and autonomous agents that automate complex business operations.

---

## 📂 Repository Structure

### 💻 Code (`code/`)
The learning path combines foundational programming exercises, modular experiments, and capstone projects:

- **`lesson_01_intro.py`**: Personal vision & AI roadmap (Applied AI & Agentic Workflow Engineering).
- **`lesson_02_toolkit.py`**: AI Dev Toolkit verification (Python, uv, Ollama, Claude Code).
- **`lesson_04_print_input.py`**: Dynamic consultation prompt generator utilizing `input()` and `print()`.
- **`lesson_05_variables.py`**: State & prompt context management using Python variables.
- **`lesson_06_strings_prompts.py`**: String cleaning (`.strip()`, `.lower()`, `.title()`, `.capitalize()`, `.startswith()`) for robust prompt hygiene.
- **`lesson_07_conditions.py`**: **Smart Model Router** — Routes user tasks between local (Ollama) and cloud models based on task type, token estimation, and privacy constraints.
- **`lesson_08_mini_chatbot.py`**: **TechFix Laptop Care Bot** — Interactive FAQ bot with a complaint-first intent hierarchy, human agent handover, and chat metrics summary.
- **`project_m1_prompt_kit.py`**: **Module 1 Capstone (Part 1)** — *Business Prompt Kit* that generates custom AI prompt templates for Marketing, Customer Support, and Growth tailored to client business data.
- **`project_m1_front_desk.py`**: **Module 1 Capstone (Part 2)** — *Sweet Crumbs Bakery AI Front Desk Assistant*. An automated business front desk assistant featuring FAQ resolution, an interactive `/quote` pricing and discount engine, privacy-preserving AI model routing (local Ollama Llama 3.2 vs. cloud), token & cost calculation, and end-of-session reporting.

---

### 📄 Documentation & Results (`docs/`)
Comprehensive documentation of design specs, experiment logs, and local LLM evaluations:

- **`project-m1-part2-design.md`**: Architectural design, intents mapping, pricing business rules, and 10 verification test cases for the Sweet Crumbs Front Desk.
- **`project-m1-part2-results.md`**: Real-world Ollama (`llama3.2`) test runs analyzing grounded vs. hallucinated responses for unanswered customer questions.
- **`project-m1-results.md`**: Testing and output evaluation for the Module 1 Part 1 Business Prompt Kit with local Ollama LLMs.
- **`prompt-test.md`**: Prompt engineering experiments and structured output testing.
- **`ollama-first-chat.md`**: Initial setup and verification of local LLM inference with Ollama.
- **`my-answers-module-1.md`**: Module 1 conceptual checkpoint answers.
- **Visual Proofs & Artifacts**:
  - `setup-check.png`: AI dev environment and toolchain verification.
  - `project-m1-run.png`: Terminal output from Module 1 Part 1 prompt generation.
  - `project-m1-part2-run.png`: Full interactive session run of the Sweet Crumbs AI Front Desk Assistant.

---

### 📓 Notebooks (`notebooks/`)
Interactive Jupyter Notebooks for experimentation, data analysis, and prototyping with `ipykernel`.

---

## 🥐 Featured Project: Sweet Crumbs Bakery — AI Front Desk Assistant
*Source: [`code/project_m1_front_desk.py`](code/project_m1_front_desk.py) | Design Specs: [`docs/project-m1-part2-design.md`](docs/project-m1-part2-design.md)*

A customer-facing front-desk automation system designed for **Sweet Crumbs Bakery** in Gulberg, Lahore. It combines deterministic rule-based speed with intelligent AI fallback routing.

### 🌟 Key Capabilities
1. **Complaint-First Intent Hierarchy**: Prioritizes unhappy customers (`refund`, `complaint`, `late`) and human handover (`human`, `agent`) before generic FAQ matching.
2. **Interactive `/quote` Pricing Engine**:
   - Menu: Cupcake (250 PKR), Brownie (300 PKR), Chocolate Cake (1,500 PKR).
   - **Bulk Discount**: 10% discount automatically applied for quantities $\ge 10$.
   - **Free Delivery Rule**: Free delivery on discounted orders $\ge 3,000$ PKR; otherwise 200 PKR standard delivery.
   - **Defensive Input Handling**: Employs `.isdigit()` validation to prevent runtime `ValueError` crashes when non-numeric quantities are entered.
3. **Privacy-Preserving AI Fallback & Router**:
   - **PII Guardrail**: Messages containing private data (`phone`, `cnic`, `address`) are routed strictly to local `llama3.2 (local, private)` at **0 PKR cost**, ensuring customer data remains secure.
   - **Cloud Fallback**: General product inquiries are routed to a cloud model with real-time token estimation (`round(len(chars) / 4)`) and cost tracking (0.10 PKR per 1,000 tokens).
   - **Prompt Guardrail**: Truncates queries to 150 characters to prevent prompt bloat and uncontrolled API costs.
4. **Session Analytics & Audit Reporting**:
   - Generates a full summary on exit (`bye`): total messages, rules answered, unanswered fallbacks, manager complaint alerts, quotes generated, total quoted revenue, and cumulative AI inference cost.

### 📋 Sweet Crumbs Intent Matrix

| Intent | Keywords | Response / Action |
| :--- | :--- | :--- |
| **Complaint (Priority 1)** | `refund`, `complaint`, `late` | Apologetic response + 1-hour manager escalation callback |
| **Human Handover** | `human`, `agent` | Connects to human agent and terminates chat |
| **Greeting** | Exact `hi`, `hello`, `salam`, `hey` (or `.startswith()`) | Personalized welcome with menu and quote hints |
| **Operating Hours** | `hour`, `open`, `close`, `timing` | Open 9:00 AM – 10:00 PM, 7 days a week |
| **Location** | `location`, `where`, `branch`, `shop` | Main Boulevard, Gulberg, Lahore |
| **Delivery Policy** | `deliver`, `shipping`, `fee`, `charges` | Standard fee (200 PKR), Free on orders $\ge 3,000$ PKR |
| **Menu & Prices** | `menu`, `price`, `items`, `cost` | Current items with direct prompt to use `/quote` |
| **Quote Calculator** | `/quote` command | Multi-step interactive pricing, discount & delivery calculation |
| **Smart AI Fallback** | Any unmatched query | Privacy check $\rightarrow$ Local Ollama or Cloud routing + 2-line prompt generation |

---

## 💻 TechFix Laptop Care — Interactive Helper Bot
*Source: [`code/lesson_08_mini_chatbot.py`](code/lesson_08_mini_chatbot.py)*

A specialized support bot built for a local computer shop in Hafeez Center, Lahore, focusing on rapid intent resolution:

| # | Intent | Keywords | Bot Reply |
|---|---|---|---|
| 1 | **Complaint (Top Priority)** | `late`, `complaint`, `bad`, `broken` | Apologizes and schedules immediate manager call |
| 2 | **Human Agent** | `agent`, `human` | Instantly transfers to human and ends chat |
| 3 | **Greeting** | `hi`, `hello`, `salam` | Warm personalized welcome |
| 4 | **Timings** | `timing`, `time`, `open`, `hours` | 11:00 AM to 9:00 PM, Monday – Saturday |
| 5 | **Fees** | `fee`, `price`, `cost`, `charges` | Diagnostic and cleaning starting at 1,500 PKR |
| 6 | **Location** | `location`, `address`, `where` | 2nd Floor, Hafeez Center, Gulberg III, Lahore |
| 7 | **Appointment** | `appointment`, `book`, `repair`, `upgrade` | Requests laptop model to reserve slot |
| 8 | **Fallback** | *(Unmatched)* | Constructs structured prompt for AI answering |

---

## 🛠️ AI Dev Toolkit

- **Language**: Python 3.14+
- **Environment & Dependency Manager**: [`uv`](https://astral.sh/uv) (fast Python package management)
- **Local LLM Engine**: [Ollama](https://ollama.ai) (`llama3.2`)
- **Development Tooling**: Claude Code, Antigravity IDE, Jupyter Notebooks (`ipykernel`)
- **Primary OS**: Windows 11 / PowerShell

---

## 🚀 Getting Started

### 1. Clone & Setup Environment
Ensure `uv` is installed, then set up the virtual environment:
```bash
# Clone the repository
git clone https://github.com/AbdullahAhmed922/python-ai.git
cd python-ai

# Synchronize virtual environment with uv
uv sync
```

### 2. Running the Projects

**Run the Sweet Crumbs AI Front Desk Assistant (Module 1 Checkpoint 2):**
```bash
uv run python code/project_m1_front_desk.py
```
*Try asking about hours, typing `/quote` for 12 cupcakes, testing private queries (`"change my phone number"`), or typing `bye` to view the session analytics!*

**Run the Business Prompt Kit (Module 1 Part 1):**
```bash
uv run python code/project_m1_prompt_kit.py
```

**Run the TechFix Bot:**
```bash
uv run python code/lesson_08_mini_chatbot.py
```

---

## 📌 Vision & Purpose

This repository marks the progression toward mastering **Applied AI & Agentic Systems**:
- 🐍 **Production Python**: Writing clean, defensive, modular Python.
- 🛡️ **Privacy & Guardrails**: Designing systems that protect user PII and route requests to zero-cost local LLMs.
- 🧠 **Context & Prompt Architecture**: Engineering reliable, hallucination-resistant prompts for business workflows.
- 🤖 **Autonomous Agents & RAG**: Expanding rule-based front desks into fully autonomous agents integrated with vector databases and tool calling.

---

## 👤 Author

- **Abdullah Ahmed**
- *Aspiring Applied AI & Agentic Workflow Engineer*
- 📍 Lahore, Pakistan
