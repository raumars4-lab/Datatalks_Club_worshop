# This script is going to download a table or data from web side, transform and clear the data with pandas and load this data to a databases.
# I am executing this script in local, the comand sys.argv is not useful, for this reason I am going to thake the month data using the actual value
import sys
from datetime import datetime

# si pasas argumento, lo usa; si no, usa el mes actual
month = int(sys.argv[1]) if len(sys.argv) > 1 else datetime.now().month

print("arguments", sys.argv)
print(f"Actual_month: {month}")
print(f"output_day_{month}.parquet")

## The next step is going to use pandas. Fist of all is necesary to isntall pandas pyarrow because in this course is going to use parquet data
# Normaly when I write a script, I put all the libraries and modules at the top of the script, but in this case I am going to put it here because I want to explain the reason of this library.
import pandas as pd
# Pandas is a library that allows us to manipulate data in a very easy way, it is very useful for data analysis and data cleaning. In this case, I am going to use it to create a dataframe and save it as a parquet file.
df = pd.DataFrame({"day": [1, 2], "number_passengers": [3, 4]})
# To agregate any data in this dataframe, is necessary to add a new column with the month value, this is going to be useful for the next step when we are going to load this data to a database.
df["month"] = month
print(df.head())
# To write this dataframe to parquet is going to use this sentence
# First of all, we need to install the library pyarrow, this library is going to be used by pandas to write the dataframe to parquet format. 
# But we are going to use a virtual envirorment, in this case, we not need to install this dependence inside the local machine:
## To create a virtual envriorment, is necesary to write this sentence: uv init --python 3.13
## To execute the virual enviorment, is going to write this sentence: uv run python -V
df.to_parquet(f"output_day_{month}.parquet")

# Next step is create the docker image
