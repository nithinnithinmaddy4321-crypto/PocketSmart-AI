# PocketSmart AI: Your Smart Budget & Recommendation Assistant

PocketSmart is a simple FastAPI web application that analyzes a user's monthly income and expenses and provides practical budgeting recommendations.

## Features

- Monthly income input
- Savings goal
- Housing, food, transport, utilities, entertainment and other expense tracking
- Total expense calculation
- Remaining monthly balance
- Expense ratio
- Largest expense category
- Smart rule-based recommendations
- Responsive web interface
- Health endpoint

## Requirements

Python 3.10 or newer is recommended.

## Run on Windows

Open the project folder in VS Code, then run:

```powershell
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python -m uvicorn app.main:app --reload
```

Open:

```text
http://127.0.0.1:8000
```

## Notes

This project is intentionally self-contained and does not require an API key or external AI service to run. The recommendation engine is in `app/budget_service.py`, so an external AI provider can be integrated later if required.

This application provides general budgeting information and is not professional financial advice.
