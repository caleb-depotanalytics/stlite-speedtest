import time

begin_render_load_time = time.time()

import time
from pathlib import Path

import numpy as np
import pandas as pd
import streamlit as st


def append_csv(filename, num_iterations, time_to_complete):
    if Path(filename).exists():
        test_df = pd.read_csv(filename, index_col=0)
    else:
        test_df = pd.DataFrame(columns=["num_iterations", "time_to_complete"])
    test_df = pd.concat(
        [
            test_df,
            pd.DataFrame.from_dict(
                {
                    "num_iterations": num_iterations,
                    "time_to_complete": time_to_complete,
                },
                orient="index",
            ).T,
        ],
        ignore_index=True,
    )
    test_df.to_csv(filename)


def pyodide_compute_test(num_iterations):
    """do a mathematical stress test with numpy"""
    # setup a timer
    start_time = time.time()

    # do 10000 calculations with numpy
    for i in range(num_iterations):
        np.random.randn(100, 100)
    end_time = time.time()
    # add a row to test_df
    append_csv("pyodide_test.csv", num_iterations, end_time - start_time)
    return


def pure_python_compute_test(num_iterations):
    """do a mathematical stress test in pure python"""

    start_time = time.time()
    for i in range(num_iterations):
        arbitrary_list = [x * 2 for x in range(100)]
    end_time = time.time()
    # add a row to test_df
    append_csv("pure_python_test.csv", num_iterations, end_time - start_time)
    return


if __name__ == "__main__":
    st.write("Speed test app")
    # do a mathematical stress test with numpy and pandas

    # create a dataframe
    df = pd.DataFrame(np.random.randn(200, 3), columns=["a", "b", "c"])

    # create a line chart
    chart_data = pd.DataFrame(np.random.randn(20, 3), columns=["a", "b", "c"])
    st.line_chart(chart_data)

    # create a map around Tenerife
    map_data = pd.DataFrame(
        np.random.randn(1000, 2) / [20, 20] + [28.2916, -16.6291],
        columns=["lat", "lon"],
    )

    st.map(map_data)

    end_render_load_time = time.time()
    st.write(
        f"Rendering a basic GUI in: {end_render_load_time - begin_render_load_time}"
    )

    num_iterations = st.slider(
        "Number of numpy rand computations to do", 1000, 100000, step=1000
    )
    # add a button to run the computational test and get return value
    st.button(
        "Run pyodide library compute test",
        on_click=pyodide_compute_test,
        args=(num_iterations,),
    )
    # dynamically display the global variable test_return_str, so that it updates when the variable is updated
    st.write(
        pd.read_csv("pyodide_test.csv", index_col=0)
        if Path("pyodide_test.csv").exists()
        else None
    )

    st.button(
        "Run pure python compute test",
        on_click=pure_python_compute_test,
        args=(num_iterations,),
    )
    st.write(
        pd.read_csv("pure_python_test.csv", index_col=0)
        if Path("pure_python_test.csv").exists()
        else None
    )
