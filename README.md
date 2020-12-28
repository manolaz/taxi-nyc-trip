# taxi-nyc-trip

There Python scripts doing simple data conversion

## Python requirements

(Pyarrow)[https://arrow.apache.org/docs/python/parquet.html]

- Install with Anaconda is recommended [https://arrow.apache.org/docs/python/install.html]

(Pandas)[https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.to_parquet.html]

## Task 1

- Load the GreenTrip CSV data and convet to Parquet
- Running with command

```bash
 python csv2parquet.py
```

Output result stored at:
=> dataset/green_tripdata_2013-09.parquet

## Task 2

- Load the GreenTrip data from Parquet
- Running with command

```bash
 python hot_encoding.py
```

### GPS Coordinate idea pseudo code

we can divide the JFK Airport to N x M zones

- ZONE CODE could be Hashing by LONGITUDE and Latitude of PICKUP of Dropoff localtion

Example:
ZONE A1 if

- LONG between [-73.9524 ... -73.9526]
- LAT between [40.8107 ... 40.8108]

Output result stored at:
=> dataset/augmented_green_tripdata_2013-09.parquet
