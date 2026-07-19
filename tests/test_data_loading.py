from src.data_loader import (
    load_unified,
    load_reference_codes,
)


def test_load_dataset():

    df = load_unified()

    assert len(df) > 0


def test_reference_codes():

    ref = load_reference_codes()

    assert len(ref) > 0