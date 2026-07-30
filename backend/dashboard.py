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
departments = data["departments"]

budgets=budgets.merge(departments, on="Department_ID")
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
# Department Budget Chart
# -----------------------------

department_budget = (
    budgets
    .groupby("Department_name")["allocated"]
    .sum()
    .reset_index()
)


department_chart = px.bar(
    department_budget,
    y="Department_name",
    x="allocated",
    orientation="h",
    title="Budget by Department"
)


st.plotly_chart(
    department_chart,
    use_container_width=True
)