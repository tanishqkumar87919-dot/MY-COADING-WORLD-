import pandas as pd

def pivotTable(weather: pd.DataFrame) -> pd.DataFrame:
    return weather.pivot(
        index='month',
        columns='city',
        values='temperature'
    ).rename_axis(None, axis=1).sort_index()