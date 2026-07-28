import pandas as pd

def load_budget_data():
    departments=pd.read_excel('data/departments.xlsx',sheet_name='Departments')

    budgets=pd.read_excel('data/budgets.xlsx',sheet_name='Budget')

    expenses=pd.read_excel('data/expenses.xlsx',sheet_name='Expenses')

    return{
        "departments":departments,
        "budgets":budgets,
        "expenses":expenses
    }