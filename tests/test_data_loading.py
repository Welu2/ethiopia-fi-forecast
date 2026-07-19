from unittest.mock import patch
import pandas as pd
from src.data_loader import (
    load_unified,
    load_reference_codes,
)


@patch("pandas.read_excel")
def test_load_dataset(mock_read_excel):
    # Create mock data so the test doesn't look for a physical file
    mock_df = pd.DataFrame({
        "record_type": ["event"],
        "title": ["Test Event"],
    })
    mock_read_excel.return_value = mock_df

    df = load_unified()

    # Verify pandas read engine was triggered and data exists
    mock_read_excel.assert_called_once()
    assert len(df) > 0


@patch("pandas.read_excel")
def test_reference_codes(mock_read_excel):
    # Mock reference codes
    mock_df = pd.DataFrame({
        "code": ["A", "B"],
        "meaning": ["Alpha", "Beta"],
    })
    mock_read_excel.return_value = mock_df

    ref = load_reference_codes()

    mock_read_excel.assert_called_once()
    assert len(ref) > 0