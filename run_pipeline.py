from src.loaders.mock_loader import load_mock_demand
from src.transforms.build_weekly_vectors import build_weekly_vectors
from configs.config import RAW_PATH, OUTPUT_PATH, HORIZON_WEEKS


def main():
    demand = load_mock_demand(RAW_PATH)
    vectors = build_weekly_vectors(demand, horizon_weeks=HORIZON_WEEKS)

    vectors.to_parquet(OUTPUT_PATH, index=False)

    print("Pipeline finished.")
    print(f"Input rows: {len(demand)}")
    print(f"Output rows: {len(vectors)}")
    print(f"Saved to: {OUTPUT_PATH}")
    print(vectors[["song_id", "country", "demand_vector"]])


if __name__ == "__main__":
    main()