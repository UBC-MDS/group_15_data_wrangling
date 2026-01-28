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

def test_cat_mode_impute_columns_type_error():
    df = pd.DataFrame({"a": ["x", "?", "x"]})

    with pytest.raises(TypeError, match="columns.*list of strings"):
        cat_mode_impute(df, columns="a", sign="?")  # not a list

    with pytest.raises(TypeError, match="columns.*list of strings"):
        cat_mode_impute(df, columns=[1, 2], sign="?")  # not list[str]


def test_cat_mode_impute_columns_none_auto_detects_and_imputes():
    df = pd.DataFrame({"a": ["x", "?", "x"], "b": ["y", "y", "y"]})

    out = cat_mode_impute(df, columns=None, sign="?")

    assert out["a"].tolist() == ["x", "x", "x"]
    assert out["b"].tolist() == ["y", "y", "y"]


def test_cat_mode_impute_all_missing_in_target_column_raises():
    df = pd.DataFrame({"a": ["?", "?", "?"]})

    with pytest.raises(ValueError, match="cannot be imputed.*all values are missing"):
        cat_mode_impute(df, columns=["a"], sign="?")

def test_cat_mode_impute_columns_none_and_no_sign_raises_valueerror():
    df = pd.DataFrame({"a": ["x", "y", "z"], "b": ["m", "n", "p"]})

    with pytest.raises(ValueError, match="sign.*not found|targeted columns"):
        cat_mode_impute(df, columns=None, sign="?")
