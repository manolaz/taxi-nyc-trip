import pandas as pd
import pyarrow as pa
import pyarrow.parquet as pq
# from fastparquet import write

df = pd.read_csv('dataset/green_tripdata_2013-09.csv')
# using Pyarrow
table = pa.Table.from_pandas(df)
pq.write_table(table, 'dataset/green_tripdata_2013-09.parquet')

# alternative solution using FastParquet
# write('dataset/green_tripdata_2013-09.parq', df)
