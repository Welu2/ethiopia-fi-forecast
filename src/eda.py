"""
EDA utilities for Ethiopia Financial Inclusion Forecasting Project

Task 2
"""

from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd

FIGURES_DIR = Path("reports/figures")
FIGURES_DIR.mkdir(parents=True, exist_ok=True)


# ---------------------------------------------------------
# Helper Functions
# ---------------------------------------------------------

def _save_plot(filename):
    plt.tight_layout()
    plt.savefig(FIGURES_DIR / filename, dpi=300)
    plt.show()


def observations(df):
    if "record_type" not in df.columns:
        return df
    return df[df["record_type"] == "observation"].copy()


def events(df):
    if "record_type" not in df.columns:
        return df
    return df[df["record_type"] == "event"].copy()


# ---------------------------------------------------------
# Dataset Overview
# ---------------------------------------------------------

def dataset_summary(df):
    print("=" * 60)
    print("Dataset Shape")
    print(df.shape)

    print("\nColumns")
    print(df.columns.tolist())

    print("\nData Types")
    print(df.dtypes)

    print("\nMissing Values")
    print(df.isna().sum())

    print("\nDuplicate Rows")
    print(df.duplicated().sum())


def plot_record_types(df):

    if "record_type" not in df.columns:
        return

    counts = df["record_type"].value_counts()

    plt.figure(figsize=(6,4))
    counts.plot(kind="bar")

    plt.title("Records by Type")
    plt.ylabel("Count")

    _save_plot("record_types.png")


def plot_pillars(df):

    if "pillar" not in df.columns:
        return

    counts = df["pillar"].fillna("Missing").value_counts()

    plt.figure(figsize=(6,4))
    counts.plot(kind="bar")

    plt.title("Records by Pillar")

    _save_plot("pillars.png")


def plot_source_types(df):

    if "source_type" not in df.columns:
        return

    counts = df["source_type"].fillna("Missing").value_counts()

    plt.figure(figsize=(6,4))
    counts.plot(kind="bar")

    plt.title("Source Types")

    _save_plot("source_types.png")


def plot_confidence(df):

    if "confidence" not in df.columns:
        return

    counts = df["confidence"].fillna("Missing").value_counts()

    plt.figure(figsize=(6,4))
    counts.plot(kind="bar")

    plt.title("Confidence Distribution")

    _save_plot("confidence_distribution.png")


# ---------------------------------------------------------
# Temporal Coverage
# ---------------------------------------------------------

def temporal_coverage(df):

    obs = observations(df)

    if "observation_date" not in obs.columns:
        return

    obs = obs.copy()

    obs["year"] = pd.to_datetime(
        obs["observation_date"]
    ).dt.year

    coverage = (
        obs.groupby(["indicator", "year"])
        .size()
        .unstack(fill_value=0)
    )

    plt.figure(figsize=(12,8))

    plt.imshow(coverage.values)

    plt.colorbar(label="Records")

    plt.xticks(
        range(len(coverage.columns)),
        coverage.columns,
        rotation=45
    )

    plt.yticks(
        range(len(coverage.index)),
        coverage.index
    )

    plt.title("Temporal Coverage")

    _save_plot("temporal_coverage.png")


# ---------------------------------------------------------
# Indicator Coverage
# ---------------------------------------------------------

def indicator_coverage(df):

    obs = observations(df)

    coverage = (
        obs.groupby("indicator")
        .size()
        .sort_values(ascending=False)
    )

    print(coverage)

    plt.figure(figsize=(10,6))

    coverage.plot(kind="bar")

    plt.title("Indicator Coverage")

    _save_plot("indicator_coverage.png")


# ---------------------------------------------------------
# Account Ownership
# ---------------------------------------------------------

def account_ownership(df):

    obs = observations(df)

    mask = (
        obs["indicator"]
        .str.contains(
            "account",
            case=False,
            na=False
        )
    )

    data = obs[mask].copy()

    if len(data) == 0:
        print("No account ownership records found.")
        return

    data["year"] = pd.to_datetime(
        data["observation_date"]
    ).dt.year

    yearly = (
        data.groupby("year")["value_numeric"]
        .mean()
    )

    plt.figure(figsize=(8,5))

    plt.plot(
        yearly.index,
        yearly.values,
        marker="o"
    )

    plt.title("Account Ownership Trend")

    plt.ylabel("Percent")

    plt.grid(True)

    _save_plot("account_ownership.png")

    growth = yearly.diff()

    print("\nGrowth (Percentage Points)")

    print(growth)


# ---------------------------------------------------------
# Gender Gap
# ---------------------------------------------------------

def gender_gap(df):

    obs = observations(df)

    if "gender" not in obs.columns:
        return

    data = obs.dropna(subset=["gender"])

    if len(data) == 0:
        return

    data["year"] = pd.to_datetime(
        data["observation_date"]
    ).dt.year

    pivot = data.pivot_table(
        index="year",
        columns="gender",
        values="value_numeric",
        aggfunc="mean"
    )

    plt.figure(figsize=(8,5))

    for col in pivot.columns:

        plt.plot(
            pivot.index,
            pivot[col],
            marker="o",
            label=col
        )

    plt.legend()

    plt.title("Gender Gap")

    plt.grid(True)

    _save_plot("gender_gap.png")


# ---------------------------------------------------------
# Mobile Money
# ---------------------------------------------------------

def mobile_money(df):

    obs = observations(df)

    mask = (
        obs["indicator"]
        .str.contains(
            "mobile",
            case=False,
            na=False
        )
    )

    data = obs[mask].copy()

    if len(data) == 0:
        return

    data["year"] = pd.to_datetime(
        data["observation_date"]
    ).dt.year

    yearly = (
        data.groupby("year")["value_numeric"]
        .mean()
    )

    plt.figure(figsize=(8,5))

    plt.plot(
        yearly.index,
        yearly.values,
        marker="o"
    )

    plt.title("Mobile Money Trend")

    plt.grid(True)

    _save_plot("mobile_money.png")


# ---------------------------------------------------------
# Infrastructure
# ---------------------------------------------------------

def infrastructure(df):

    obs = observations(df)

    keywords = [
        "internet",
        "mobile",
        "4g",
        "atm"
    ]

    mask = obs["indicator"].str.contains(
        "|".join(keywords),
        case=False,
        na=False
    )

    data = obs[mask]

    print(data[
        [
            "indicator",
            "value_numeric",
            "observation_date"
        ]
    ])


# ---------------------------------------------------------
# Event Timeline
# ---------------------------------------------------------

def event_timeline(df):

    ev = events(df)

    if len(ev) == 0:
        return

    ev["date"] = pd.to_datetime(
        ev["observation_date"]
    )

    ev = ev.sort_values("date")

    plt.figure(figsize=(12,2))

    plt.scatter(
        ev["date"],
        [1]*len(ev)
    )

    for _, row in ev.iterrows():

        label = row["category"]

        plt.text(
            row["date"],
            1.02,
            label,
            rotation=45,
            fontsize=8
        )

    plt.yticks([])

    plt.title("Financial Inclusion Events")

    _save_plot("event_timeline.png")


# ---------------------------------------------------------
# Correlation
# ---------------------------------------------------------

def correlation_matrix(df):

    obs = observations(df)

    pivot = obs.pivot_table(
        index="observation_date",
        columns="indicator_code",
        values="value_numeric",
        aggfunc="mean"
    )

    corr = pivot.corr()

    plt.figure(figsize=(10,8))

    plt.imshow(corr)

    plt.colorbar()

    plt.xticks(
        range(len(corr.columns)),
        corr.columns,
        rotation=90,
        fontsize=7
    )

    plt.yticks(
        range(len(corr.columns)),
        corr.columns,
        fontsize=7
    )

    plt.title("Correlation Matrix")

    _save_plot("correlation_matrix.png")

    return corr


# ---------------------------------------------------------
# Data Quality
# ---------------------------------------------------------

def data_quality_report(df):

    report = pd.DataFrame({
        "missing": df.isna().sum(),
        "dtype": df.dtypes
    })

    print(report)

    return report


# ---------------------------------------------------------
# Run Everything
# ---------------------------------------------------------

def run_all(df):

    dataset_summary(df)

    plot_record_types(df)

    plot_pillars(df)

    plot_source_types(df)

    plot_confidence(df)

    temporal_coverage(df)

    indicator_coverage(df)

    account_ownership(df)

    gender_gap(df)

    mobile_money(df)

    infrastructure(df)

    event_timeline(df)

    correlation_matrix(df)

    data_quality_report(df)