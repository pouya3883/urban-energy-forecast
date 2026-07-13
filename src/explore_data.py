import pandas as pd

df = pd.read_csv("data/AEP_hourly.csv")

df["Datetime"] = pd.to_datetime(df["Datetime"])
df["Hour"] = df["Datetime"].dt.hour
