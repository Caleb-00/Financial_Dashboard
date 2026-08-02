import streamlit as st
from data import load_budget_data
import plotly.express as px
import plotly.graph_objects as go
import plotly.io as pio
pio.templates.default = "plotly"

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
    "This dashboard provides an overview of the budget allocation, expenses, and remaining budget for the organization."
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

department_chart.update_layout(
    xaxis_title="Allocated Budget",
    yaxis_title="Department",
    
)
#this is the original way to display the bar chart before formatting

#st.plotly_chart(
    #department_chart,
   # use_container_width=True
#)

# -----------------------------
# Department Budget Pie Chart
# -----------------------------

department_pie_chart = px.pie(
    department_budget,
    values="allocated",
    names="Department_name",
    title="Budget by Department Pie Chart"
)

#this is the original way to display the pie chart before formatting

#st.plotly_chart(
    #department_pie_chart,
    #use_container_width=True
#)


# -----------------------------
# Department Expense Chart
# -----------------------------

department_expenses = (
    expenses
    .merge(departments, on="Department_ID")
    .groupby("Department_name")["amount"]
    .sum()
    .reset_index()
)


expense_chart = px.bar(
    department_expenses,
    x="Department_name",
    y="amount",
    title="Expenses by Department",
)

expense_chart.update_layout(
    xaxis_title="Department",
    yaxis_title="Expenses",
    xaxis_tickangle=-45
)

#this is the original way to display the chart before formatting
#st.plotly_chart(
    #expense_chart,
    #use_container_width=True
#)


# -----------------------------
# Top Row: Budget Bar + Pie Chart
# -----------------------------

left_col, right_col = st.columns([2, 1])  # Bar chart gets more space

with left_col:
    st.plotly_chart(
        department_chart,
        use_container_width=True
    )

with right_col:
    st.plotly_chart(
        department_pie_chart,
        use_container_width=True
    )

# -----------------------------
# Bottom Row: Expense Chart
# -----------------------------

st.plotly_chart(
    expense_chart,
    use_container_width=True
)