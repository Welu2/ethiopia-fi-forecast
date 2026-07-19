import pandas as pd
from pathlib import Path

PROCESSED = Path("data/processed")


def add_records(df, additions):

    enriched = pd.concat(
        [df, additions],
        ignore_index=True
    )

    enriched.to_csv(
        PROCESSED / "ethiopia_fi_enriched.csv",
        index=False
    )

    return enriched