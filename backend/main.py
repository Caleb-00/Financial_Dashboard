from fastapi import FastAPI
from data import load_budget_data
app = FastAPI(
    title="Budget Management API"
)


#setting up the paths for the API

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

#This path uses sum of expenses and budget to then return information about the budget and expenses to the API
@app.get("/summary")
def summary():
    data =load_budget_data()

    budgets=data["budgets"]
    expenses=data["expenses"]

    total_budget=budgets["allocated"].sum()
    total_expenses=expenses["amount"].sum()

    return {
        "total_budget": int(total_budget),
        "total_expenses": int(total_expenses),
        "remaining_budget": int(total_budget - total_expenses)
    }