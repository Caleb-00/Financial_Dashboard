import streamlit as st
from data import load_budget_data
import plotly.express as px
import plotly.graph_objects as go

fig = go.Figure(
    data=[go.Bar(y=[2, 1, 3])],
    layout_title_text="A Figure Displayed with fig.show()"
)
fig.show()
st.title("Budget Management Dashboard")

data=load_budget_data()
st.write("Departments")
st.write(data["departments"])
