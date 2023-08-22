import random
from datetime import date, timedelta, datetime

import pandas as pd
import polars as pl


def iterative_random_walk(
        company_count: int,
        start: date,
        end: date,
        interval: timedelta,
) -> pl.DataFrame:
    data = {f"company {x}": [100] for x in range(company_count)}
    timestamp = datetime.combine(start, datetime.min.time())
    timestamps = [timestamp]
    while timestamp.date() < end:
        timestamp += interval
        for company in data:
            data[company].append(data[company][-1] + random.random())
        timestamps.append(timestamp)
    data["timestamp"] = timestamps
    return pl.DataFrame(data)


def pandas_vectorised_random_walk() -> pd.DataFrame:
    return pd.DataFrame()


def polars_vectorised_random_walk() -> pl.DataFrame:
    return pl.DataFrame()

