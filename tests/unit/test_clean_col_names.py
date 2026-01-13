"""
Docstring for tests.unit.test_clean_col_names
"""

import pandas as pd
from group_15_data_wrangling.clean_col_name import clean_col_name

# df: test dataframe, out: dataframe preocessed by function
df = pd.read_csv("data_sample.csv")
out = clean_col_name(df)

# make sure the structure keeps the same after applying the function
assert out.shape[1] == df.shape[1]

# change column name "fnlwgt" to "final_weight"
assert "final_weight" in out.columns
assert "fnlwgt" not in out.columns

# change "." to "_"
assert all("." not in c for c in out.columns)
assert "capital_gain" in out.columns
assert "capital_loss" in out.columns
assert "hours_per_week" in out.columns

# columns not need to be changed stay the same
assert "age" in out.columns
assert "sex" in out.columns
assert "workclass" in out.columns

# test dataframe should not be changed
assert "fnlwgt" in df.columns
assert "education.num" in df.columns

# wrong input
with 
