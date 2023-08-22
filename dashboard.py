from datetime import date, timedelta

import polars as pl
import streamlit as st
import plotly.express as px

from drunkards_walk import iterative_random_walk

dashboard_name = "Drunkards Walk Dashboard"
st.set_page_config(
    page_title=dashboard_name,
    page_icon=":beer:",
    layout="wide",
    menu_items={
        "About": "Dashboard plotting a configurable, deterministic drunkards/random walk algorithm"
    },
)

st.title(dashboard_name)

with st.sidebar as sb:
    st.header("Configuration")

df = iterative_random_walk(
    company_count=5,
    start=date.today(),
    end=date.today() + timedelta(days=5),
    interval=timedelta(minutes=1),
)
st.plotly_chart(
    px.line(
        data_frame=df,
        x="timestamp",
        y=[col for col in df.columns if col != "timestamp:w" ""],
    ),
    use_container_width=True,
)
