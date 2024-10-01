import pandas as pd
from fastapi import FastAPI
from sodapy import Socrata

app = FastAPI()


def serialize(row):
    return {
        "make": row["make"][0],
        "electric_range": {
            "mean": row["electric_range"]["mean"],
            "count": row["electric_range"]["count"],
        },
    }


@app.get("/electric-ranges")
def electric_ranges(model_year: int):
    client = Socrata("data.wa.gov", None)

    # TODO: add limits and pagination
    results = client.get("f6w7-q2d2", model_year=model_year, limit=1000)

    results_df = pd.DataFrame.from_records(results)

    # TODO: test for errors here with mocked data (floats, alpha, nulls); add try/except
    results_df["electric_range"] = pd.to_numeric(results_df["electric_range"])
    grouped_df = (
        results_df.groupby("make")
        .agg({"electric_range": ["mean", "count"]})
        .reset_index()
    )
    response_data = grouped_df.apply(serialize, axis=1).tolist()

    return {"results": response_data}
