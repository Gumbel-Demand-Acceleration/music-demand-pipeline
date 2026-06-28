import pandas as pd
from src.schema import CANONICAL_COLUMNS


def validate_schema(df: pd.DataFrame) -> None:
    missing = set(CANONICAL_COLUMNS) - set(df.columns)

    if missing:
        raise ValueError(f"Missing required columns: {missing}")
    