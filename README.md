# Onsetto Engineering Challenge

## Overview

This repository contains my solution for the Onsetto Engineering Challenge.

### Part 1
Playwright browser automation that:

- Logs into the application
- Completes MFA
- Updates banking details
- Updates payment method
- Verifies saved information

### Part 2

Python API client that:

- Authenticates
- Completes MFA
- Updates banking information
- Updates payment method
- Prints confirmation responses

---

## Project Structure

playwright/
python-client/

---

## Installation

### Playwright

cd playwright

npm install

npx playwright install

npm test

### Python

cd python-client

python3 -m venv venv

source venv/bin/activate

pip install -r requirements.txt

python main.py

---

## Environment Variables

See .env.example

---

## Design Decisions

- Page Object Model
- Environment-based configuration
- Centralized API client
- Error handling
- Type-safe structure