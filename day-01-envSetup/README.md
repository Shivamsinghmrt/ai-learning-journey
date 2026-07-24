# Day 01 - AI Development Environment Setup

# Overview

Welcome to **Day 01** of my AI Engineering Learning Journey.

The objective of this module is to prepare a complete AI development environment from scratch using Python.

Before building AI applications such as ChatGPT clones, AI Agents, RAG pipelines, LangChain applications or MCP servers, we first need a proper development environment.

This module explains every step required to install Python, configure Visual Studio Code, create a virtual environment, install required packages, securely manage API Keys, connect to OpenAI and execute the first AI request.

The goal of this exercise is not just to "make the code work", but to understand **why every step is necessary**.

---

# Learning Objectives

After completing this module, I was able to:

- Install Python correctly
- Configure VS Code for Python development
- Create and activate a Virtual Environment
- Understand why virtual environments are important
- Install required Python packages using pip
- Configure API Keys securely using a .env file
- Understand the role of requirements.txt
- Connect to OpenAI using the official SDK
- Send my first prompt to an LLM
- Receive AI-generated responses
- Initialize a Git repository
- Push the project to GitHub

---

# Technologies Used

- Python 3.x
- Visual Studio Code
- Virtual Environment (venv)
- pip
- python-dotenv
- OpenAI Python SDK
- Git
- GitHub

---

# Project Structure

```
day-01-envSetup/

│── main.py
│── README.md
└── notes.md
```

---

# Prerequisites

Before running this project make sure you have installed:

- Python 3.11 or later
- Visual Studio Code
- Git

---

# Step 1 - Clone Repository

```bash
git clone <repository-url>
```

Open the project inside VS Code.

---

# Step 2 - Create Virtual Environment

```bash
python -m venv .venv
```

This creates an isolated Python environment.

The `.venv` folder contains its own:

- Python Interpreter
- pip
- Installed Packages

Every project should have its own virtual environment.

---

# Step 3 - Activate Virtual Environment

### Windows

```bash
.venv\Scripts\activate
```

### Mac/Linux

```bash
source .venv/bin/activate
```

When activated your terminal should look similar to

```
(.venv)
```

This indicates Python commands are now executed inside the virtual environment.

---

# Step 4 - Install Required Libraries

Install all dependencies

```bash
pip install openai python-dotenv tiktoken
```

or

```bash
pip install -r requirements.txt
```

---

# Step 5 - Create .env File

Create a file named

```
.env
```

Add your OpenAI API Key

```
OPENAI_API_KEY=your_api_key_here
```

Never hardcode API Keys inside Python files.

---

# Step 6 - Run the Project

Execute

```bash
python main.py
```

The application connects to OpenAI and sends a prompt.

Example prompt

```
Write a short poem about the beauty of nature.
```

The generated response is printed on the console.

---

# Understanding the Code

The application performs the following steps:

1. Imports required libraries.
2. Loads environment variables.
3. Reads the OpenAI API Key.
4. Creates an OpenAI client.
5. Sends a prompt.
6. Receives the AI response.
7. Prints the response.

---

# Files Used

## main.py

Contains the Python application that communicates with OpenAI.

## README.md

Project documentation.

## notes.md

Detailed learning notes explaining every concept.

---

# Output

Example

```
Morning sunlight paints the sky,
Birds awaken as clouds drift by...
```

(The exact output will vary because AI generates new text.)

---

# Common Commands

Create Environment

```bash
python -m venv .venv
```

Activate

```bash
.venv\Scripts\activate
```

Install Packages

```bash
pip install -r requirements.txt
```

Run

```bash
python main.py
```

Deactivate

```bash
deactivate
```

---

# Learning Outcome

This module established the complete AI development environment required for future modules.

The environment created here will be used throughout this learning journey for:

- Tokenization
- Embeddings
- Vector Databases
- Prompt Engineering
- RAG
- LangChain
- LangGraph
- MCP
- AI Agents

---

# Next Module

Day 02 - Tokenization

In the next module we explore how Large Language Models convert human language into Tokens before processing.

---

# Author

Shivam Singh

Senior Java Full Stack Developer

Learning Journey:
Java Full Stack → AI Engineer