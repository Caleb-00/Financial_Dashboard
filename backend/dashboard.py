import streamlit as st
from data import load_budget_data
import plotly.express as px
import plotly.graph_objects as go


# -----------------------------
# Page Configuration
# -----------------------------

st.set_page_config(
    page_title="Budget Management Dashboard",
    layout="wide"
)


# -----------------------------
# Load Data
# -----------------------------

data = load_budget_data()

budgets = data["budgets"]
expenses = data["expenses"]


# -----------------------------
# Calculate Metrics
# -----------------------------

total_budget = budgets["allocated"].sum()

total_expenses = expenses["amount"].sum()

remaining_budget = total_budget - total_expenses

utilization = (total_expenses / total_budget) * 100


# -----------------------------
# Dashboard Title
# -----------------------------

st.title("Budget Management Dashboard")

st.write(
    "Executive overview of organizational spending and budget utilization."
)


# -----------------------------
# KPI Cards
# -----------------------------

col1, col2, col3, col4 = st.columns(4)


col1.metric(
    label="Total Budget",
    value=f"${total_budget:,.0f}"
)


col2.metric(
    label="Total Expenses",
    value=f"${total_expenses:,.0f}"
)


col3.metric(
    label="Remaining Budget",
    value=f"${remaining_budget:,.0f}"
)


col4.metric(
    label="Budget Used",
    value=f"{utilization:.1f}%"
)


st.divider()


# -----------------------------
# Budget Overview Chart
# -----------------------------

comparison = {
    "Category": [
        "Budget",
        "Expenses",
        "Remaining"
    ],
    "Amount": [
        total_budget,
        total_expenses,
        remaining_budget
    ]
}


fig = px.bar(
    comparison,
    x="Category",
    y="Amount",
    title="Budget Overview",
    text="Amount"
)


fig.update_traces(
    texttemplate="$%{text:,.0f}",
    textposition="outside"
)


fig.update_layout(
    yaxis_title="Amount ($)",
    xaxis_title="",
    showlegend=False,
    height=500
)


st.plotly_chart(
    fig,
    use_container_width=True
)


# -----------------------------
# Department Spending Chart
# -----------------------------

department_spending = (
    expenses
    .groupby("Department_ID")["amount"]
    .sum()
    .reset_index()
)


department_chart = px.bar(
    department_spending,
    x="Department_ID",
    y="amount",
    title="Spending by Department"
)


st.plotly_chart(
    department_chart,
    use_container_width=True
)