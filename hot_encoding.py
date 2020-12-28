import pandas as pd
import pyarrow as pa
import pyarrow.parquet as pq
import datetime.datetime as datetime

# ***
# Create a derived dataset, from the one created above, using a SQL statement that selects all existing columns and adds these new columns:

# * One-Hot encoding for each hour of the day
# * One-Hot encoding for each day	of the week
# * Duration in seconds of the trip
# * An int encoding to indicate if the pickup or dropoff locations were at JFK airport. (Use a bounding box from the GPS coordinates to determine this). Provide pseudo code if out of time. This column is optional.
# ***


# table = pq.read_table('dataset/green_tripdata_2013-09.parquet')
df = pd.read_parquet('dataset/green_tripdata_2013-09.parquet')
for index, row in df.iterrows():
    pickup = datetime.timestamp(row["lpep_pickup_datetime"])
    dropoff = datetime.timestamp(row["Lpep_dropoff_datetime"])
    row['trip_duration'] = (dropoff - pickup).total_seconds()

table = pa.Table.from_pandas(df)
pq.write_table(table, 'dataset/augmented_green_tripdata_2013-09.parquet')
