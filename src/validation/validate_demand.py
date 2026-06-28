import pandas as pd


def validate_demand(df: pd.DataFrame) -> None:
    if (df["demand"] < 0).any():
        raise ValueError("Negative demand detected.")

    if df["week"].isna().any():
        raise ValueError("Missing week values.")

    if df.duplicated(subset=["song_id", "country", "week"]).any():
        raise ValueError("Duplicate song-country-week rows detected.")

