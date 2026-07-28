import pandas as pd


def load_budget_data():

    file_path = "../data/Budget2026.xlsx"

    departments = pd.read_excel(
        file_path,
        sheet_name="Departments"
    )

    budgets = pd.read_excel(
        file_path,
        sheet_name="Budgets"
    )

    expenses = pd.read_excel(
        file_path,
        sheet_name="Expenses"
    )

    return {
        "departments": departments,
        "budgets": budgets,
        "expenses": expenses
    }