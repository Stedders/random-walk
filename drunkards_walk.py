import random
from datetime import date, timedelta, datetime

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


# df = iterative_random_walk(
#     company_count=5,
#     start=date(2000, 1, 1),
#     end=date(2000, 1, 3),
#     interval=timedelta(minutes=1),
#     initial_value=100,
#     rand_seed=12345,
# )
# print(df)
