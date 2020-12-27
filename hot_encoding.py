import pandas as pd
import pyarrow as pa
import pyarrow.parquet as pq

table = pq.read_table('dataset/green_tripdata_2013-09.parquet')
pq.write_table(table, 'dataset/augmented_green_tripdata_2013-09.parquet')
