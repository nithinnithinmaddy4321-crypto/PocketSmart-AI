from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from .budget_service import build_budget_plan

app = FastAPI(title="PocketSmart AI: Your Smart Budget & Recommendation Assistant")
templates = Jinja2Templates(directory="app/templates")


@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={}
    )


@app.post("/analyze", response_class=HTMLResponse)
def analyze(
    request: Request,
    name: str = Form(...),
    income: float = Form(...),
    housing: float = Form(...),
    food: float = Form(...),
    transport: float = Form(...),
    utilities: float = Form(...),
    entertainment: float = Form(...),
    other: float = Form(...),
    savings_goal: float = Form(...),
):
    data = {
        "name": name.strip(),
        "income": income,
        "housing": housing,
        "food": food,
        "transport": transport,
        "utilities": utilities,
        "entertainment": entertainment,
        "other": other,
        "savings_goal": savings_goal,
    }

    result = build_budget_plan(data)

    return templates.TemplateResponse(
        request=request,
        name="result.html",
        context={"data": data, "result": result}
    )


@app.get("/health")
def health():
    return {
        "status": "ok",
        "project": "PocketSmart AI Smart Budget & Recommendation Assistant"
    }
