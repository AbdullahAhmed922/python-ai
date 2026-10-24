# 🤖 AI-Driven Python Learning Journey

Welcome to the **AI-Driven Python Learning Journey**! This repository is more than just a practice space; it is a documented progression of learning Python specifically to build **Applied AI & Agentic Workflows**.

The goal of this project is to move from Python fundamentals to building intelligent RAG pipelines and autonomous agents that automate complex business operations.

---

## 📂 Repository Structure

### 💻 Code (`code/`)
The core of the learning path, divided into lessons and a milestone project:
- **`lesson_01_intro.py`**: Introduction to Python and personal AI vision.
- **`lesson_02_toolkit.py`**: AI Dev Toolkit configuration (Python, uv, Ollama, Claude Code).
- **`lesson_04_print_input.py`**: Practical application of `input()` and `print()` to create a dynamic AI consultation prompt.
- **`lesson_05_variables.py`**: Working with Python variables to store AI context.
- **`lesson_06_strings_prompts.py`**: Advanced string manipulation for structured prompting.
- **`lesson_07_conditions.py`**: Using conditional logic to create adaptive AI responses.
- **`lesson_08_mini_chatbot.py`**: Building a basic interactive chatbot loop.
- **`project_m1_prompt_kit.py`**: **Module 1 Capstone Project** — A professional Business Prompt Kit that generates tailored AI prompts for Marketing, Customer Service, and Growth based on client data.

### 📄 Documentation (`docs/`)
Detailed records of experiments and results:
- `ollama-first-chat.md`: Documentation of the first interaction with local LLMs.
- `project-m1-results.md`: Results and analysis of the Module 1 project.
- `prompt-test.md`: Testing and refining the prompt engineering logic.
- Visual proofs of setup and project runs.

### 📓 Notebooks (`notebooks/`)
Interactive Jupyter Notebooks for rapid experimentation and data exploration.

---

## 🤖 TechFix Bot — Intent Design Table

The chatbot in `code/lesson_08_mini_chatbot.py` is built for **TechFix Laptop Care**, a local laptop repair shop in Hafeez Center, Lahore. Below is the design table that maps every intent the bot recognises.

| # | Intent | User Wants | Keywords | Bot Reply |
|---|--------|-----------|----------|-----------|
| 1 | **Greeting** | Say hello | `hi`, `hello`, `salam` | `Walaikum Assalam, {name}! How can I help you with your laptop today?` |
| 2 | **Timings** | Know shop hours | `timing`, `time`, `open`, `hours` | `We are open 11 am to 9 pm, Monday to Saturday.` |
| 3 | **Fees** | Know the cost | `fee`, `price`, `cost`, `charges` | `Basic diagnostic and cleaning fee is 1,500 PKR.` |
| 4 | **Location** | Find the shop | `location`, `address`, `where` | `We are on the 2nd Floor, Hafeez Center, Gulberg III, Lahore.` |
| 5 | **Appointment** | Book a repair | `appointment`, `book`, `repair`, `upgrade` | `Sure, {name}! Share your laptop model and we will book a repair slot for you.` |
| 6 | **Complaint** | Report a problem | `late`, `complaint`, `bad`, `broken` | `Sorry about that, {name}. Our shop manager will call you today.` |
| 7 | **Human Agent** | Talk to a person | `agent`, `human` | `Connecting you to a human...` *(ends chat)* |
| 8 | **Fallback** | Anything else | *(no match)* | Echoes the question inside a future-AI prompt template |

> **Design note:** Complaints are checked *before* FAQ intents so a frustrated user who mentions a keyword like "fee" inside a complaint is not given a generic FAQ answer.

---

## 🛠️ AI Dev Toolkit

This project is built using a modern AI engineering stack:
- **Language**: Python 3.13+
- **Package Manager**: `uv` (for ultra-fast dependency management)
- **LLM Orchestration**: Ollama (Local LLM execution)
- **AI Assistant**: Claude Code (CLI-based agentic coding)
- **Editor**: VS Code

---

## 🚀 Getting Started

### Setting Up the Environment
Using `uv` for a seamless setup:
```bash
# Install uv if you haven't already
curl -LsSf https://astral.sh/uv/install.sh | sh

# Sync the environment
uv sync
```

### Running the Projects
```bash
# Run the Module 1 Project
python code/project_m1_prompt_kit.py
```

---

## 📌 Vision & Purpose

This repository documents the transition from a learner to an **Applied AI & Agentic Workflow Engineer**. 

**Focus Areas:**
- 🐍 **Python Mastery**: Writing clean, scalable code.
- 🧠 **Prompt Engineering**: Creating structured, dynamic prompts for business automation.
- 🤖 **Agentic Workflows**: Learning how to connect LLMs to tools and data.
- 💼 **Business Value**: Solving real-world problems like manual customer support through AI.

---

## 👤 Author

- **Abdullah Ahmed**
- *Aspiring Applied AI & Agentic Workflow Engineer*
