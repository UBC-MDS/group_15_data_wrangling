import pytest
import pandas as pd
from group_15_data_wrangling.clean_col_names import clean_col_name

def test_clean_col_name():
    # df: original test dataframe, out: dataframe after using the function
    df = pd.read_csv("tests/unit/data_sample.csv")
    out = clean_col_name(df)
    orig_cols = df.columns.tolist()

    # the structure keeps the same after applying the function
    assert out.shape[1] == df.shape[1]

    # change column name "fnlwgt" to "final_weight"
    assert "final_weight" in out.columns
    assert "fnlwgt" not in out.columns

    # change "." to "_"
    assert all("." not in c for c in out.columns)
    assert "capital_gain" in out.columns
    assert "capital_loss" in out.columns
    assert "hours_per_week" in out.columns

    # columns not need to be changed should stay the same
    assert "age" in out.columns
    assert "sex" in out.columns
    assert "workclass" in out.columns

    # test dataframe should not be changed
    assert df.columns.tolist() == orig_cols

# wrong input
def test_clean_col_name_wrong_input():
    wrong_input = ["not", "dataframe"]
    with pytest.raises(TypeError, match="must be a dataframe"):
        clean_col_name(wrong_input) # pyright: ignore[reportArgumentType]

# missing column name
def test_clean_col_name_missing():
    df = pd.DataFrame({"age": [1, 2]})
    with pytest.raises(ValueError, match="not found in dataframe"):
        clean_col_name(df)
