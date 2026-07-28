from data import load_budget_data

data = load_budget_data()

print("Budgets columns:")
print(data["budgets"].columns)

print("\nExpenses columns:")
print(data["expenses"].columns)