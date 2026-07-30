
#This is the file used to read the data from the excel file 
import pandas as pd


def load_budget_data():

    file_path = "data/Budget2026.xlsx"
#----------------------------------------
#reading each page of excel file then returning it to the API
#----------------------------------------
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