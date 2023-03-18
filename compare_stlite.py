import math

import pandas as pd
import plotly.express as px
import streamlit as st
from matplotlib import pyplot as plt

if __name__ == "__main__":
    # read in the test data
    dt_pyodide_test_df = pd.read_csv("desktop_pyodide_test.csv", index_col=0)
    dt_pure_python_test_df = pd.read_csv("desktop_pure_python_test.csv", index_col=0)

    st_pyodide_test_df = pd.read_csv("streamlit_pyodide_test.csv", index_col=0)
    st_pure_python_test_df = pd.read_csv("streamlit_pure_python_test.csv", index_col=0)

    # create a line chart
    st.line_chart(dt_pyodide_test_df["time_to_complete"])
    st.line_chart(st_pyodide_test_df["time_to_complete"])
    # st.line_chart(y=st_pyodide_test_df['time_to_complete'].values, x=dt_pyodide_test_df['num_iterations'].values)
    # define plotly figure and define the range of the axes
    fig = px.line(
        dt_pyodide_test_df,
        x="num_iterations",
        y="time_to_complete",
        title="Desktop/Streamlit - Pyodide Libraries (Exec Secs)",
    )
    st.plotly_chart(fig)

    # define plotly figure and define the range of the axes
    fig = px.line(
        dt_pure_python_test_df,
        x="num_iterations",
        y="time_to_complete",
        title="Desktop/Streamlit - Pure Python (Exec Secs)",
    )
    st.plotly_chart(fig)

    # define plotly figure and define the range of the axes
    mixed_df = pd.DataFrame()
    mixed_df["num_iterations"] = dt_pure_python_test_df["num_iterations"]
    mixed_df["time_to_complete"] = (
        dt_pure_python_test_df["time_to_complete"]
        / st_pure_python_test_df["time_to_complete"]
    )
    fig = px.line(
        mixed_df,
        x="num_iterations",
        y="time_to_complete",
        title="Desktop/Streamlit - Pure Python",
    )
    st.plotly_chart(fig)

    # define plotly figure and define the range of the axes
    mixed_df = pd.DataFrame()
    mixed_df["num_iterations"] = dt_pyodide_test_df["num_iterations"]
    mixed_df["time_to_complete"] = (
        dt_pyodide_test_df["time_to_complete"] / st_pyodide_test_df["time_to_complete"]
    )
    fig = px.line(
        mixed_df,
        x="num_iterations",
        y="time_to_complete",
        title="Desktop/Streamlit - Pyodide Libraries",
    )
    st.plotly_chart(fig)
    # st.line_chart(dt_pure_python_test_df['time_to_complete']/st_pure_python_test_df['time_to_complete'])
