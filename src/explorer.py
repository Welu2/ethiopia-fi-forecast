import pandas as pd


def dataset_summary(df):

    print("=" * 50)

    print(df.info())

    print("=" * 50)

    print(df.head())

    print("=" * 50)

    print(df.describe(include="all"))


def record_counts(df):

    for col in [
        "record_type",
        "pillar",
        "source_type",
        "confidence",
    ]:

        if col in df.columns:

            print("\n", col)

            print(df[col].value_counts(dropna=False))


def temporal_range(df):

    if "observation_date" in df.columns:

        dates = pd.to_datetime(df["observation_date"])

        print("Start:", dates.min())

        print("End:", dates.max())


def indicator_coverage(df):

    cols = ["indicator_code", "indicator"]

    available = [c for c in cols if c in df.columns]

    print(df.groupby(available).size())


def events(df):

    events = df[df["record_type"] == "event"]

    cols = [
        "record_id",
        "category",
        "indicator",
        "observation_date",
        "source_name",
        "confidence"
    ]

    cols = [c for c in cols if c in events.columns]

    print(events[cols])