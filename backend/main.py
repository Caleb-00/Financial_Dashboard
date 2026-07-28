from fastapi import FastAPI
from data import load_budget_data
app = FastAPI(
    title="Budget Management API"
)

@app.get("/")
def home():
    return {
        "message":"Budget Management API running"
    }
@app.get("/departments")
def departments():

    data = load_budget_data()

    return data["departments"].to_dict(
        orient="records"
    )


@app.get("/expenses")
def expenses():

    data = load_budget_data()

    return data["expenses"].to_dict(
        orient="records"
    )

@app.get("/budgets")
def budgets():
    data = load_budget_data()

    return data["budgets"].to_dict(
        orient="records"
    )