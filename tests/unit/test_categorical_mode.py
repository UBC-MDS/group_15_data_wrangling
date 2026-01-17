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

def test_cat_mode_impute_replaces_sign_with_mode_and_returns_copy():
    df = pd.DataFrame({"a": ["x", "?", "x", "y"]})

    out = cat_mode_impute(df, columns=["a"], sign="?")

    # core behavior
    assert out.loc[1, "a"] == "x"
    assert (out["a"] == "?").sum() == 0

    # original unchanged (function returns a copy)
    assert out is not df
    assert df.loc[1, "a"] == "?"

def test_cat_mode_impute_tie_break_is_lexicographic():
    df = pd.DataFrame({"a": ["b", "a", "?", "b", "a", "?"]})
    out = cat_mode_impute(df, columns=["a"], sign="?")
    assert out.loc[2, "a"] == "a"
    assert out.loc[5, "a"] == "a"
