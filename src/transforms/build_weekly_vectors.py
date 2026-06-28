import pandas as pd


def build_weekly_vectors(df: pd.DataFrame, horizon_weeks: int = 26) -> pd.DataFrame:
    rows = []
    group_cols = ["song_id", "song_name", "artist_name", "country", "source"]

    for keys, group in df.groupby(group_cols):
        group = group.sort_values("week")
        start_week = group["week"].min()
        full_weeks = pd.date_range(start=start_week, periods=horizon_weeks, freq="7D")

        aligned = (
            group.set_index("week")
            .reindex(full_weeks)
            .rename_axis("week")
            .reset_index()
        )

        aligned["demand"] = aligned["demand"].fillna(0)

        rows.append(
            {
                "song_id": keys[0],
                "song_name": keys[1],
                "artist_name": keys[2],
                "country": keys[3],
                "source": keys[4],
                "start_week": start_week,
                "horizon_weeks": horizon_weeks,
                "demand_vector": aligned["demand"].tolist(),
            }
        )

    return pd.DataFrame(rows)
