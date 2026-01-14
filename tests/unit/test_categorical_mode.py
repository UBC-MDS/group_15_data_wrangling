import pandas as pd
import pytest

from group_15_data_wrangling.categorical_mode import cat_mode_impute

def test_cat_mode_impute_type_error():
    with pytest.raises(TypeError, match="pandas DataFrame"):
        cat_mode_impute(["not", "a", "df"])

def test_cat_mode_impute_value_error():
    df = pd.DataFrame({"a": ["x", "y", "z"]})
    with pytest.raises(ValueError, match="sign.*not found"):
        cat_mode_impute(df, columns=["a"], sign="?")

def test_cat_mode_impute_key_error():
    df = pd.DataFrame({"a": ["x", "?", "y"]})
    with pytest.raises(KeyError, match="not found"):
        cat_mode_impute(df, columns=["does_not_exist"])
