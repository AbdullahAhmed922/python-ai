# 🤖 AI-Driven Python Learning Journey

Welcome to the **AI-Driven Python Learning Journey**! This repository documents a structured, practical progression from Python fundamentals to building **Applied AI & Agentic Workflows**.

The primary objective is to move from foundational programming and scripting toward building reliable, production-ready AI systems, hybrid rule/LLM pipelines, and autonomous workflows designed for real-world business operations.

---

## 📂 Repository Structure

### 💻 Code (`code/`)

#### 📦 Module 2: LLM Integration, Memory, Personas & Batch Production
- **[`code/project_m2_content_studio.py`](code/project_m2_content_studio.py)**: **Module 2 Capstone** — *AI Content Studio*. A multi-purpose operational AI tool for Sweet Crumbs Bakery that automates batch menu descriptions with cloud cost estimation, streams social media posts with Roman Urdu cultural translations, provides instant 0-token dictionary price lookups, and conducts customer chat using a bounded sliding-window memory and strictly grounded business facts (powered by `ollama:gemma3:4b`).
- **[`code/lesson_2_4_batch_writer.py`](code/lesson_2_4_batch_writer.py)**: **Batch Copywriter** — Automated batch generation of appetizing pastry descriptions with token accumulation, execution timing, and skipping unavailable items.
- **[`code/lesson_2_3_persona_bot.py`](code/lesson_2_3_persona_bot.py)**: **Persona Bot** — Dynamic persona-switching assistant (`friendly`, `formal`, `sales`) grounded in real bakery business facts.
- **[`code/lesson_2_2_chat_memory.py`](code/lesson_2_2_chat_memory.py)**: **Conversational Memory** — Multi-turn chat assistant with sliding-window memory management to prevent unbounded context growth.
- **[`code/lesson_2_1_first_ai_call.py`](code/lesson_2_1_first_ai_call.py)**: **First AI Call & Profiling** — LLM invocation for topic explanations with automated token count and latency tracking.

#### 📦 Module 1: Foundations & Interactive Business Automations
- **[`code/project_m1_front_desk.py`](code/project_m1_front_desk.py)**: **Module 1 Capstone (Part 2)** — *Sweet Crumbs Bakery AI Front Desk Assistant*. An automated business front desk assistant featuring FAQ resolution, an interactive `/quote` pricing and discount engine, privacy-preserving AI model routing (local Ollama Llama 3.2 vs. cloud), token & cost calculation, and end-of-session reporting.
- **[`code/project_m1_prompt_kit.py`](code/project_m1_prompt_kit.py)**: **Module 1 Capstone (Part 1)** — *Business Prompt Kit*. Generates customized AI prompt templates for Marketing, Customer Support, and Growth tailored to client business data.
- **[`code/lesson_08_mini_chatbot.py`](code/lesson_08_mini_chatbot.py)**: **TechFix Laptop Care Bot** — Interactive FAQ bot with a complaint-first intent hierarchy, human agent handover, and chat metrics summary.
- **[`code/lesson_07_conditions.py`](code/lesson_07_conditions.py)**: **Smart Model Router** — Routes user tasks between local (Ollama) and cloud models based on task complexity, token estimation, and data privacy constraints.
- **[`code/lesson_06_strings_prompts.py`](code/lesson_06_strings_prompts.py)**: **String Hygiene & Prompt Sanitization** — String cleaning (`.strip()`, `.lower()`, `.title()`, `.capitalize()`, `.startswith()`) for robust input handling.
- **[`code/lesson_05_variables.py`](code/lesson_05_variables.py)**: **State & Context Management** — Managing state and prompt contexts with typed Python variables.
- **[`code/lesson_04_print_input.py`](code/lesson_04_print_input.py)**: **Dynamic Prompt Generator** — Interactive consultation prompts using `input()` and formatted console output.
- **[`code/lesson_02_toolkit.py`](code/lesson_02_toolkit.py)**: **Toolchain Verification** — Python environment, `uv`, Ollama, and IDE setup diagnostics.
- **[`code/lesson_01_intro.py`](code/lesson_01_intro.py)**: **Personal Vision & Roadmap** — Learning strategy for Applied AI & Agentic Workflow Engineering.

---

### 📄 Documentation & Results (`docs/`)

Comprehensive records of system designs, experiment logs, test runs, and evaluations:

- **Module 2 Documentation**:
  - **[`docs/project-m2-cp1-design.md`](docs/project-m2-cp1-design.md)**: Architectural design, model temperature allocation, facts mapping, and test matrix for the Sweet Crumbs AI Content Studio.
  - **[`docs/project-m2-cp1-results.md`](docs/project-m2-cp1-results.md)**: Factual QA validation, hallucination checks, tone analysis, and Roman Urdu translation evaluations.
  - **[`docs/my-answers-module-2.md`](docs/my-answers-module-2.md)**: Conceptual checkpoint answers and quick-check verification for Lessons 2.1 to 2.4.
- **Module 1 Documentation**:
  - **[`docs/project-m1-part2-design.md`](docs/project-m1-part2-design.md)**: Architectural specification, intent hierarchy, pricing engine formulas, and verification test cases for the Sweet Crumbs Front Desk.
  - **[`docs/project-m1-part2-results.md`](docs/project-m1-part2-results.md)**: Real-world local LLM test runs analyzing grounded vs. hallucinated responses for out-of-scope customer inquiries.
  - **[`docs/project-m1-results.md`](docs/project-m1-results.md)**: Output evaluation and testing logs for the Business Prompt Kit.
  - **[`docs/my-answers-module-1.md`](docs/my-answers-module-1.md)**: Conceptual checkpoint answers for Module 1.
  - **[`docs/prompt-test.md`](docs/prompt-test.md)**: Prompt engineering experiments and structured output testing.
  - **[`docs/ollama-first-chat.md`](docs/ollama-first-chat.md)**: Local LLM setup and inference verification via Ollama.
- **Visual Proofs & Artifacts**:
  - **[`docs/project-m2-cp1-run.png`](docs/project-m2-cp1-run.png)**: Terminal session showing batch menu generation, streaming posts, Roman Urdu translations, and grounded chat.
  - **[`docs/project-m1-part2-run.png`](docs/project-m1-part2-run.png)**: Complete interactive run of the Sweet Crumbs AI Front Desk Assistant.
  - **[`docs/project-m1-run.png`](docs/project-m1-run.png)**: Terminal output of the Module 1 Part 1 prompt generation kit.
  - **[`docs/setup-check.png`](docs/setup-check.png)**: AI development environment and local toolchain diagnostics.

---

### 📓 Notebooks (`notebooks/`)

Interactive Jupyter Notebooks for experimentation, data analysis, and prototyping with `ipykernel`.

---

## 🥐 Featured Project: Sweet Crumbs Bakery — AI Ecosystem
*Source: [`code/project_m1_front_desk.py`](code/project_m1_front_desk.py) | [`code/project_m2_content_studio.py`](code/project_m2_content_studio.py)*

The Sweet Crumbs Bakery automation represents an end-to-end operational AI ecosystem, evolving from a customer-facing front-desk bot into a full-fledged **AI Content Studio**.

```
                        ┌─────────────────────────────────────────┐
                        │       Sweet Crumbs AI Ecosystem         │
                        └───────────────────┬─────────────────────┘
                                            │
               ┌────────────────────────────┴───────────────────────────┐
               ▼                                                        ▼
  ┌─────────────────────────┐                             ┌─────────────────────────┐
  │ Module 1: Front Desk    │                             │ Module 2: Content Studio│
  ├─────────────────────────┤                             ├─────────────────────────┤
  │ • Complaint-first routing│                             │ • Batch menu copywriter │
  │ • Interactive /quote    │                             │ • Multi-tone social post│
  │ • PII privacy router    │                             │ • Roman Urdu translator │
  │ • Rule + local AI blend │                             │ • 0-token price lookup  │
  └─────────────────────────┘                             │ • Sliding-window memory │
                                                          └─────────────────────────┘
```

### 1. AI Content Studio (Module 2)
A multi-purpose marketing and operational tool designed for bakery staff and online engagement:

- **Batch Menu Descriptions (`/menu`)**:
  - Generates mouth-watering descriptions for all available bakery items using a creative LLM configuration.
  - Skips zero-priced items (`mango tart: 0 PKR`) before calling the model to save tokens and avoid advertising unavailable products.
  - Calculates estimated cloud API costs ($\$0.015$ per 1K tokens) alongside local zero-cost token metrics.
- **Streamed Social Media Generator (`/post <tone>`)**:
  - Streams posts word-by-word with support for distinct brand tones:
    - `fun`: Playful, energetic, short punchy sentences.
    - `premium`: Elegant, calm, artisanal focus on morning-fresh baking.
    - `urgent`: Limited-batch alerts encouraging same-day orders.
  - Defensive fallback handles unrecognized tones (e.g., `/post pirate`) seamlessly.
- **Roman Urdu Cultural Localization (Bonus)**:
  - Automatically translates English marketing posts into natural, localized Pakistani Roman Urdu using a low-temperature model.
  - Strictly preserves original PKR pricing, bakery hours, and city details without distortion.
- **Zero-Token Price Lookups (`/price <item>`)**:
  - Deterministic Python dictionary lookup (`facts["prices"].get(...)`).
  - Completely bypasses the LLM for instant, 100% accurate, zero-token cost pricing answers.
- **Grounded Conversational Chat with Memory**:
  - Answers customer inquiries strictly from injected bakery facts (hours, DHA delivery, custom order advance notices).
  - Employs a sliding context window (`max_messages=6`) preserving the initial system prompt to prevent context drift and unbounded token inflation.
- **Comprehensive Session Analytics**:
  - Tracks individual counts for chat responses, menu descriptions, social posts, price queries, total tokens accumulated, and total model execution time.

### 2. AI Front Desk Assistant (Module 1)
A customer-facing front-desk automation system combining deterministic speed with intelligent fallback:
- **Complaint-First Intent Hierarchy**: Catches urgent issues and triggers immediate manager escalation.
- **Interactive `/quote` Calculator**: Computes bulk orders, tiered discounts, and delivery fee rules with input validation.
- **Privacy-Preserving Routing**: Detects sensitive PII (Phone/CNIC) and routes requests exclusively to local Ollama models for 100% data confidentiality.

### 📋 Architectural Model & Intent Matrix

| Component | Operation | Model / Tool | Temperature | Purpose |
| :--- | :--- | :--- | :--- | :--- |
| **Customer Chat** | In-context Grounding | `precise_llm` (`gemma3:4b`) | `0.2` | Strictly factual responses; eliminates hallucinations |
| **Menu Generator** | Creative Copywriting | `creative_llm` (`gemma3:4b`) | `0.8` | Varied, appetizing descriptions for pastries |
| **Social Posts** | Tone-tuned Streaming | `creative_llm` (`gemma3:4b`) | `0.8` | Stylistic flair tailored to brand voice |
| **Urdu Translation**| Semantic Mapping | `precise_llm` (`gemma3:4b`) | `0.2` | Accurate cultural localization retaining exact PKR/hours |
| **Price Check** | Deterministic Lookup | Python Dictionary | N/A (0 Tokens) | Instant execution, 100% pricing accuracy |
| **Privacy Check** | PII Detection & Route | Ollama (`llama3.2`) | `0.2` | 0-cost local inference protecting private customer data |

---

## 💻 TechFix Laptop Care — Interactive Helper Bot
*Source: [`code/lesson_08_mini_chatbot.py`](code/lesson_08_mini_chatbot.py)*

A rule-based and intent-prioritized support system built for a computer hardware repair shop in Hafeez Center, Lahore:

| Priority | Intent | Matching Keywords | Response Action |
| :---: | :--- | :--- | :--- |
| **1** | **Complaint (Top Priority)** | `late`, `complaint`, `bad`, `broken` | Immediate apology and manager escalation callback |
| **2** | **Human Handover** | `agent`, `human` | Instant transfer to on-duty technician and graceful exit |
| **3** | **Greeting** | `hi`, `hello`, `salam` | Personalized welcome message |
| **4** | **Timings** | `timing`, `time`, `open`, `hours` | Operating schedule (11:00 AM – 9:00 PM, Mon–Sat) |
| **5** | **Fees & Pricing** | `fee`, `price`, `cost`, `charges` | Diagnostic and maintenance pricing starting at 1,500 PKR |
| **6** | **Location** | `location`, `address`, `where` | Shop address (2nd Floor, Hafeez Center, Gulberg III, Lahore) |
| **7** | **Appointment** | `appointment`, `book`, `repair`, `upgrade` | Booking intake workflow requesting laptop model |
| **8** | **AI Fallback** | *(Any unmatched query)* | Structures a 2-line prompt for LLM completion |

---

## 🛠️ AI Dev Toolkit

- **Language**: Python 3.14+
- **Environment & Dependency Manager**: [`uv`](https://astral.sh/uv) (high-performance Python packaging)
- **Orchestration Framework**: LangChain (`langchain`, `langchain-ollama`, `init_chat_model`)
- **Local LLM Engine**: [Ollama](https://ollama.ai) (defaulting to `gemma3:4b` for Content Studio; `qwen2.5:3b` and `llama3.2` for foundational modules)
- **Development Tooling**: Antigravity IDE, Claude Code, Jupyter Notebooks (`ipykernel`)
- **Primary OS**: Windows 11 / PowerShell

---

## 🚀 Getting Started

### 1. Clone & Setup Environment

Ensure [`uv`](https://astral.sh/uv) and [Ollama](https://ollama.ai) are installed on your machine:

```powershell
# Clone the repository
git clone https://github.com/AbdullahAhmed922/python-ai.git
cd python-ai

# Synchronize virtual environment with uv
uv sync

# Pull the primary local models used in the modules
ollama pull gemma3:4b
ollama pull qwen2.5:3b
ollama pull llama3.2
```

### 2. Running the Projects

#### 🥐 Sweet Crumbs AI Content Studio (Module 2 Capstone)
```powershell
uv run python code/project_m2_content_studio.py
```
**Interactive Commands:**
- `/menu` — Generate batch descriptions for all in-stock bakery items with token metrics and cloud cost estimates.
- `/post fun` | `/post premium` | `/post urgent` — Stream an Instagram caption in the selected style, followed by a Roman Urdu version.
- `/price <item>` — Perform instant, 0-token price lookups (e.g. `/price chocolate cake`, `/price mango tart`).
- `/reset` — Clear conversation history while retaining system rules.
- `bye` — Terminate session and display comprehensive usage statistics.

#### 🏪 Sweet Crumbs AI Front Desk Assistant (Module 1 Capstone Part 2)
```powershell
uv run python code/project_m1_front_desk.py
```
*Try asking for store hours, entering `/quote` for order calculations, submitting a query containing phone numbers to observe privacy routing, or typing `bye` for session metrics.*

#### 📝 Business Prompt Kit (Module 1 Capstone Part 1)
```powershell
uv run python code/project_m1_prompt_kit.py
```

#### 💻 TechFix Laptop Care Chatbot
```powershell
uv run python code/lesson_08_mini_chatbot.py
```

#### 🧪 Modular AI Lessons (Module 2)
```powershell
# Lesson 2.1: First AI Call with token & duration tracking
uv run python code/lesson_2_1_first_ai_call.py

# Lesson 2.2: Chat memory with sliding window context management
uv run python code/lesson_2_2_chat_memory.py

# Lesson 2.3: Persona-switching bot with factual grounding
uv run python code/lesson_2_3_persona_bot.py

# Lesson 2.4: Batch product writer with cost accumulation
uv run python code/lesson_2_4_batch_writer.py
```

---

## 📌 Engineering Principles & Key Learnings

1. **Deterministic-First, AI-Second Architecture**:
   Never spend model tokens on tasks solved by a hash table. Using Python dictionaries for pricing guarantees zero latency, $0 token cost, and 100% accuracy.
2. **Temperature Separation**:
   Customer support requires low entropy ($\text{temperature}=0.2$) to enforce factual grounding. Creative marketing copy demands higher variance ($\text{temperature}=0.8$) to deliver fresh, engaging prose.
3. **Context Window Stewardship**:
   Chat histories cannot grow indefinitely. Bounded sliding-window architectures (`messages = [system] + history[-N:]`) maintain predictable token consumption and latency.
4. **Privacy & Zero-Cost Edge Inference**:
   Sensitivities like phone numbers, CNICs, or proprietary customer data are routed to local Ollama models (`llama3.2`, `gemma3:4b`), providing air-gapped data privacy with zero API expenses.
5. **Hallucination Prevention via Fact Injection**:
   Strict system prompt boundaries instructing the assistant to answer *only* from supplied business facts prevent the model from inventing non-existent items or policies.

---

## 👤 Author

- **Abdullah Ahmed**
- *Aspiring Applied AI & Agentic Workflow Engineer*
- 📍 Lahore, Pakistan
- 📧 [abd1962964@gmail.com](mailto:abd1962964@gmail.com)
