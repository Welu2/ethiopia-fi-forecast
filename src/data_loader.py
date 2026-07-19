from pathlib import Path
import pandas as pd


PROJECT_ROOT = Path(__file__).resolve().parent.parent


RAW_DIR = PROJECT_ROOT / "data" / "raw"


def load_unified():
    return pd.read_excel(RAW_DIR / "ethiopia_fi_unified_data_enriched.xlsx",sheet_name=1)


def load_reference_codes():
    return pd.read_excel(RAW_DIR / "reference_codes.xlsx")


def load_impact_links():
    """
    Loads the 'impact' sheet from the enriched Excel file.
    """
    path = RAW_DIR / "ethiopia_fi_unified_data_enriched.xlsx"

    if path.exists():
        # Changed from read_csv to read_excel
        return pd.read_excel(path, sheet_name="Impact_sheet")

    return None
