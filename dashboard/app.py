import streamlit as st
import pandas as pd
import plotly.express as px
from pathlib import Path


# -------------------
# Page Configuration
# -------------------

st.set_page_config(
    page_title="Ethiopia Financial Inclusion Dashboard",
    layout="wide"
)


# -------------------
# Load Data
# -------------------

@st.cache_data
def load_data():

    # Project root directory
    BASE_DIR = Path(__file__).resolve().parent.parent

    data_path = (
        BASE_DIR
        / "data"
        / "raw"
        / "ethiopia_fi_unified_data_enriched.xlsx"
    )

    forecast_path = (
        BASE_DIR
        / "data"
        / "task4_forecast_table.csv"
    )

    data = pd.read_excel(
        data_path,
        sheet_name="ethiopia_fi_unified_data"
    )

    forecast = pd.read_csv(
        forecast_path
    )

    return data, forecast


data, forecast = load_data()


# -------------------
# Sidebar Navigation
# -------------------

st.sidebar.title(
    "Navigation"
)

page = st.sidebar.radio(
    "Select Page",
    [
        "Overview",
        "Trends",
        "Forecasts",
        "Inclusion Projections"
    ]
)


# -------------------
# Overview Page
# -------------------

if page == "Overview":

    st.title(
        "Ethiopia Financial Inclusion Dashboard"
    )

    col1, col2, col3 = st.columns(3)


    account = data[
        data["indicator_code"] == "ACC_OWNERSHIP"
    ].copy()


    if len(account) > 0:

        account = account.sort_values(
            "observation_date"
        )

        latest_account = (
            account.iloc[-1]["value_numeric"]
        )

    else:
        latest_account = 0


    col1.metric(
        "Account Ownership",
        f"{latest_account:.1f}%"
    )


    col2.metric(
        "Indicators",
        data["indicator_code"].nunique()
    )


    col3.metric(
        "Data Records",
        len(data)
    )


    st.subheader(
        "Top Indicators"
    )


    indicator_counts = (
        data["indicator_code"]
        .value_counts()
        .head(10)
    )


    fig = px.bar(
        indicator_counts,
        title="Indicator Coverage"
    )


    st.plotly_chart(
        fig,
        use_container_width=True
    )


# -------------------
# Trends Page
# -------------------

elif page == "Trends":

    st.title(
        "Financial Inclusion Trends"
    )


    indicators = (
        data["indicator_code"]
        .dropna()
        .unique()
    )


    indicator = st.selectbox(
        "Select Indicator",
        indicators
    )


    df = data[
        data["indicator_code"] == indicator
    ].copy()


    df["date"] = pd.to_datetime(
        df["observation_date"]
    )


    df = df.sort_values(
        "date"
    )


    fig = px.line(
        df,
        x="date",
        y="value_numeric",
        markers=True,
        title=indicator
    )


    st.plotly_chart(
        fig,
        use_container_width=True
    )


    st.download_button(
        label="Download Indicator Data",
        data=df.to_csv(index=False),
        file_name="indicator_data.csv",
        mime="text/csv"
    )


# -------------------
# Forecast Page
# -------------------

elif page == "Forecasts":

    st.title(
        "Financial Inclusion Forecasts 2025-2027"
    )


    scenario = st.selectbox(
        "Select Scenario",
        [
            "baseline",
            "optimistic",
            "pessimistic"
        ]
    )


    fig = px.line(
        forecast,
        x="year",
        y=scenario,
        markers=True,
        title=f"{scenario.title()} Forecast"
    )


    st.plotly_chart(
        fig,
        use_container_width=True
    )


    st.subheader(
        "Forecast Results"
    )


    st.dataframe(
        forecast
    )


    st.download_button(
        label="Download Forecast",
        data=forecast.to_csv(index=False),
        file_name="forecast_results.csv",
        mime="text/csv"
    )


# -------------------
# Inclusion Projection Page
# -------------------

elif page == "Inclusion Projections":

    st.title(
        "Progress Toward 60% Financial Inclusion Target"
    )


    scenario = st.selectbox(
        "Scenario",
        [
            "pessimistic",
            "baseline",
            "optimistic"
        ]
    )


    projected_value = (
        forecast[scenario]
        .iloc[-1]
    )


    target = 60


    progress = min(
        projected_value / target,
        1
    )


    st.progress(
        progress
    )


    st.write(
        f"""
        Projected Account Ownership (2027):

        **{projected_value:.1f}%**

        Target:

        **{target}%**
        """
    )


    fig = px.bar(
        forecast,
        x="year",
        y=[
            "pessimistic",
            "baseline",
            "optimistic"
        ],
        title="Scenario Comparison"
    )


    st.plotly_chart(
        fig,
        use_container_width=True
    )


    st.subheader(
        "Key Insights"
    )

    st.write(
        """
        - Digital finance expansion is expected to support inclusion growth.
        - Mobile money adoption is a major driver of future access.
        - Forecast uncertainty remains high because historical observations are limited.
        """
    )
