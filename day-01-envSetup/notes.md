# Day 01 - AI Development Environment Setup

---

# Introduction

This is the first module of my AI Engineering Learning Journey.

Before building AI applications like ChatGPT, AI Agents, Retrieval-Augmented Generation (RAG), LangChain applications, or Model Context Protocol (MCP) servers, we first need to prepare a proper development environment.

Unlike Java, where we usually start by creating a Maven or Gradle project, AI development starts by setting up Python, creating an isolated environment, installing the required libraries, configuring API keys, and verifying that we can communicate with an LLM.

This module focuses on understanding **why** each setup step is required rather than simply following commands.

---

# Why Python for AI?

Although AI models can be accessed from many programming languages, Python has become the standard language for AI development.

Reasons include:

- Simple and readable syntax
- Massive AI ecosystem
- Official support from almost every AI framework
- Extensive community support
- Large collection of AI libraries

Popular AI libraries include:

- OpenAI SDK
- LangChain
- LangGraph
- LlamaIndex
- TensorFlow
- PyTorch
- Hugging Face Transformers
- FastAPI

As a Java developer, I will continue using Java professionally, but Python is essential for AI engineering.

---

# Installing Python

Python provides:

- Python Interpreter
- pip (Package Manager)
- Standard Library

Verify installation:

```bash
python --version
```

Verify pip:

```bash
pip --version
```

If these commands work successfully, Python has been installed correctly.

---

# Visual Studio Code

VS Code is one of the most popular editors for Python and AI development.

Required extensions include:

- Python
- Pylance

These extensions provide:

- IntelliSense
- Auto-completion
- Debugging
- Syntax highlighting

---

# What is pip?

pip is Python's package manager.

Java analogy:

```
Java
↓

Maven / Gradle

↓

Downloads Dependencies
```

Python

```
Python

↓

pip

↓

Downloads Packages
```

Example

```bash
pip install openai
```

downloads the official OpenAI SDK.

Similarly,

```bash
pip install python-dotenv
```

downloads the dotenv library.

---

# What is a Virtual Environment?

A Virtual Environment (venv) creates an isolated Python environment for a project.

Without a virtual environment, every Python project would share the same installed libraries, which could lead to version conflicts.

Example:

Project A requires:

```
openai==1.30
```

Project B requires:

```
openai==2.0
```

Without isolation, these projects could interfere with each other.

A virtual environment solves this by maintaining separate dependencies for each project.

---

# Creating a Virtual Environment

Command:

```bash
python -m venv .venv
```

This creates a folder named:

```
.venv
```

Inside this folder Python creates:

- Separate Interpreter
- Separate pip
- Installed Packages
- Activation Scripts

Every AI project should have its own virtual environment.

---

# Activating Virtual Environment

Windows

```bash
.venv\Scripts\activate
```

Mac/Linux

```bash
source .venv/bin/activate
```

Successful activation changes the terminal to

```
(.venv)
```

This means every package installed using pip is now installed only inside this project.

---

# Installing Dependencies

Instead of manually downloading packages, Python uses pip.

Command:

```bash
pip install openai python-dotenv tiktoken
```

This installs:

OpenAI SDK

Allows Python applications to communicate with OpenAI.

python-dotenv

Loads values from a .env file.

tiktoken

Used to understand how LLMs tokenize text.

---

# requirements.txt

Instead of asking everyone to install packages manually, Python projects usually contain

```
requirements.txt
```

Example

```
openai
python-dotenv
tiktoken
```

Another developer can simply run

```bash
pip install -r requirements.txt
```

to install all required dependencies.

Java analogy:

Similar to

```
pom.xml

or

build.gradle
```

---

# Why .env File?

Applications often require secrets such as:

- API Keys
- Database Passwords
- Access Tokens

These should never be hardcoded.

Incorrect

```python
api_key = "sk-xxxxxxxx"
```

Correct

```
.env

↓

Environment Variable

↓

Python
```

Example

```
OPENAI_API_KEY=your_api_key_here
```

This keeps secrets outside the source code and prevents accidental exposure.

---

# Understanding load_dotenv()

```python
load_dotenv()
```

This function reads the `.env` file and loads all variables into the application's environment.

Without calling this function, `os.getenv()` would not be able to read the API key stored in `.env`.

---

# Understanding os.getenv()

```python
os.getenv("OPENAI_API_KEY")
```

This retrieves the value of the `OPENAI_API_KEY` environment variable.

Instead of exposing the API key directly in code, the application reads it securely at runtime.

---

# Understanding the OpenAI Client

```python
client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)
```

This creates an OpenAI client.

The client is responsible for communicating with OpenAI servers over HTTPS.

Java analogy:

Similar to creating:

- RestTemplate
- WebClient
- HttpClient

before making REST API calls.

---

# Sending the First AI Request

```python
response = client.responses.create(
    model="gpt-4.1-mini",
    input="Write a short poem about the beauty of nature."
)
```

This sends a request to the OpenAI API.

Internally, the SDK:

1. Creates an HTTPS request.
2. Adds the API key.
3. Sends the prompt.
4. Waits for the model's response.
5. Returns the generated output.

---

# Printing the Response

```python
print(response.output_text)
```

Displays the generated AI response on the console.

Since LLMs generate text dynamically, the response may differ each time.

---

# Git Setup

Version control is essential for software development.

Commands used:

Initialize repository

```bash
git init
```

Check status

```bash
git status
```

Stage changes

```bash
git add .
```

Commit

```bash
git commit -m "Day 1 - Environment Setup"
```

Push

```bash
git push
```

---

# Problems Faced During Setup

## Git Not Recognized

### Problem

```
git is not recognized as an internal or external command
```

### Cause

Git was installed but the terminal had not picked up the updated PATH.

### Solution

- Verify Git installation.
- Restart the terminal (or VS Code) so the updated PATH is loaded.
- Run:

```bash
git --version
```

to confirm Git is available.

---

## PowerShell Script Execution Error

### Problem

PowerShell blocked activation of the virtual environment because script execution was disabled.

### Solution

Run:

```powershell
Set-ExecutionPolicy -Scope CurrentUser RemoteSigned
```

Then activate the environment again:

```powershell
.venv\Scripts\activate
```

---

## Virtual Environment Permission Error

A common issue is trying to recreate `.venv` while it is already active.

### Example

```bash
python -m venv .venv
```

while the prompt already shows:

```
(.venv)
```

### Solution

Either:

- Use the existing virtual environment, or
- Run `deactivate` before recreating it.

---

## Why Use GitHub?

GitHub provides:

- Source code backup
- Version history
- Collaboration
- Portfolio for recruiters
- Documentation hosting

It also allows tracking the learning journey over time.

---

# Java Developer Perspective

As a Java developer, several Python concepts map naturally to tools I already know:

| Python | Java Equivalent |
|---------|-----------------|
| pip | Maven / Gradle |
| requirements.txt | pom.xml / build.gradle |
| .env | application.properties (for configuration, though secrets should be handled securely) |
| Virtual Environment | Project-specific dependency isolation |
| OpenAI Client | RestTemplate / WebClient |
| Git | Git |

Understanding these similarities made the transition to Python much easier.

---

# Key Learnings

- Python is the primary language for AI development.
- Every project should use a virtual environment.
- `pip` manages Python packages.
- `requirements.txt` ensures reproducible environments.
- Secrets should be stored in `.env`.
- `load_dotenv()` loads environment variables.
- `os.getenv()` reads them safely.
- The OpenAI SDK simplifies communication with LLMs.
- Git is essential for version control and collaboration.

---

# Interview Questions

### What is pip?

Python's package manager used to install and manage third-party libraries.

---

### Why do we use a virtual environment?

To isolate project dependencies and avoid version conflicts.

---

### What is requirements.txt?

A file listing all project dependencies so others can recreate the same environment.

---

### Why should API keys never be hardcoded?

Hardcoding secrets risks exposing them in source code or public repositories. Using environment variables keeps credentials separate from the codebase.

---

### What does load_dotenv() do?

It loads variables from a `.env` file into the application's environment so they can be accessed with `os.getenv()`.

---

### What is the role of the OpenAI client?

It manages authenticated communication with the OpenAI API and sends requests to language models.

---

# Summary

Day 1 focused on building a solid foundation for AI development.

Instead of only installing software, I learned:

- how Python projects are structured,
- how dependencies are managed,
- how secrets are handled securely,
- how to communicate with an LLM,
- and how to version the project with Git.

This environment will be reused throughout the remaining modules of my AI Engineering learning journey.

---

# Next Module

**Day 02 – Tokenization**

Now that the development environment is ready, the next step is to understand how Large Language Models convert human language into tokens before processing it.