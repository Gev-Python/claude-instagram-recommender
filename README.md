# Date Series Finder

AI CLI application built with Python and Claude API.

The application analyzes Instagram profile-like data, identifies interests, recommends a TV series for a date night, and checks where it is available for streaming.

---

## Features

- Claude API integration
- CLI interface
- AI-powered TV series recommendation
- Mock Instagram profile scanner
- Streaming service lookup
- Modular architecture
- JSON-based Claude response

---

## Tech Stack

- Python 3.11
- Claude API / Anthropic SDK
- python-dotenv

---

## How It Works

1. User enters an Instagram username.
2. The app reads mock Instagram profile data.
3. Claude analyzes bio, posts, interests and lifestyle.
4. Claude returns a structured JSON recommendation.
5. Python checks streaming availability on Netflix, HBO or Prime.
6. The final recommendation is printed in the console.

---

## Project Structure

```text
main.py
agent.py
claude_client.py
prompts.py
tools.py
mock_data.py
architecture.md
requirements.txt
.env.example