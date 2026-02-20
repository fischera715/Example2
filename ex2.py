import streamlit as st
import plotly.express as px
import pandas as pd

st.title("Interactive Dashboard with Streamlit & Plotly")

df = px.data.gapminder()

year = st.slider(
    "Select Year:",
    int(df["year"].min()),
    int(df["year"].max()),
    int(df["year"].min())
)

filtered_df = df[df["year"] == year]

fig = px.scatter(
    filtered_df,
    x="gdpPercap",
    y="lifeExp",
    size="pop",
    color="continent",
    hover_name="country",
    log_x=True,
    size_max=60
)

st.plotly_chart(fig, use_container_width=True)
