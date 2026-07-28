from data import load_budget_data


data = load_budget_data()

print(data["Departments"])
print(data["Budgets"])
print(data["Expenses"])