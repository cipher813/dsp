# WARNING: If you close your browser, your work will be LOST!

# Q1: import numpy and pandas
import numpy as np
import pandas as pd

# Q2: Set options in pandas so it displays 30 `max_rows`
#                                 no limit on `max_columns`
#                                 precision is 3
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', 30)
pd.set_option('display.precision', 3)

# Q3: assign the versions of pandas and numpy to variables below
pd_version = pd.__version__
np_version = np.__version__

# Q4: Read in the csv file "olive.csv" with pandas.
#     The file exists in the workspace.
#     Assign it to variable `df`
df = pd.read_csv('olive.csv')

# The fields are:

# Unnamed: 0
# region
# area
# palmitic
# palmitoleic
# stearic
# oleic
# linoleic
# linolenic
# arachidic
# eicosenoic



# Q5: How many rows and columns are there in `df`? Put your answer in a variable `df_shape`.
df_shape =  df.shape

# Q6: assign the first 2 rows of `df` to `df_first_2`
df_first_two = df.head(2)

# Q7: How many distinct data types are there in `df`?
df_data_types_count = 2   # this should be an integer

# Q8: In `df`, create a new column 'sub_region_raw', which will be a copy of the column 'Unnamed: 0'
df['sub_region_raw'] = df['Unnamed: 0']

# Q9: In `df`, rename 'Unnamed: 0' to 'sub_region_desc'
df = df.rename(columns={'Unnamed: 0': 'sub_region_desc'})

# Q10: In `df`, rename the column 'area' to: 'sub_region'
df = df.rename(columns={'area': 'sub_region'})

# Q11: In `df`, get the unique values of the field 'region'
region_unique = df['region'].unique()

# Q12: In `df`, how many unique values of the field 'sub_region' are there?
sub_region_unique_count = 9  # should be an integer

# Q13: Lets take a look at the field `sub_region_desc`:

# >>> df['sub_region_desc'].head(5)
# 0    1.North-Apulia
# 1    2.North-Apulia
# 2    3.North-Apulia
# 3    4.North-Apulia
# 4    5.North-Apulia

# Looks like 'sub_region_desc' has line numbers attached to the beginning of region name. Remove those and get the unique values in that field, assign it to `srd_unique`
df['sub_region_desc'].replace(regex=True,inplace=True,to_replace=r'[\d.]',value=r'')
srd_unique = len(df['sub_region_desc'].unique()
