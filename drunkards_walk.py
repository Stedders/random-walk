import random
from datetime import date, timedelta, datetime, time

import pandas as pd
import polars as pl


def iterative_random_walk(
    company_count: int,
    timeseries_start: date,
    timeseries_end: date,
    interval: timedelta,
    open_time: time,
    close_time: time,
) -> pd.DataFrame:
    data = {f"company {x}": [100] for x in range(company_count)}
    timestamp = datetime.combine(timeseries_start, datetime.min.time())
    timestamps = [timestamp]
    while timestamp.date() <= timeseries_end:
        timestamp += interval
        print(f"Processing {timestamp}")
        if timestamp.time() < open_time or timestamp.time() > close_time:
            continue

        for company in data:
            data[company].append(data[company][-1] + random.random())
        timestamps.append(timestamp)
    data["timestamp"] = timestamps
    return pl.DataFrame(data).to_pandas()


def pandas_vectorised_random_walk() -> pd.DataFrame:
    return pd.DataFrame()


def polars_vectorised_random_walk() -> pd.DataFrame:
    return pl.DataFrame().to_pandas()
