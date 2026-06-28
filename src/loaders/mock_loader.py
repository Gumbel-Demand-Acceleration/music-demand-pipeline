import pandas as pd

from src.schema import CANONICAL_COLUMNS
from src.validation.validate_schema import validate_schema
from src.validation.validate_demand import validate_demand


def load_mock_demand(path: str) -> pd.DataFrame:
    df = pd.read_csv(path)

    validate_schema(df)

    df = df[CANONICAL_COLUMNS].copy()
    df["week"] = pd.to_datetime(df["week"])
    df["demand"] = pd.to_numeric(df["demand"], errors="coerce")

    if df["demand"].isna().any():
        raise ValueError("Demand column contains invalid numeric values.")

    validate_demand(df)

    return df