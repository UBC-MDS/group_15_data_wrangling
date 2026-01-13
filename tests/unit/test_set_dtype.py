from group_15_data_wrangling.set_dtypes import set_dtype
import pytest
import pandas as pd

@pytest.fixture
def data() -> pd.DataFrame:
    """Fixture to load test data DataFrame from csv file."""
    
    file_path = 'data_sample.csv'
    try:
        df = pd.read_csv(file_path)
        return df
    except FileNotFoundError:
        pytest.fail(f"Test data file not found at: {file_path}")


def test_input_type():
    """Test for TypeError when function input is wrong type"""
    with pytest.raises(TypeError):
        set_dtype([123])  # type: ignore

def test_column_names():
    """Test for ValueError when function input is pd.DataFrame with wrong column names"""
    wrong_names = pd.DataFrame({"col1": [1,2,3], "col2": [4,5,6]})
    with pytest.raises(ValueError):
        set_dtype(wrong_names) 

def test_int8_columns(data):
    """Test that dtype is int8 for: age, education.num, hours.per.week"""
    transformed_data = set_dtype(data)
    for col in ["age", "education.num", "hours.per.week"]:
        expected = "int8"
        actual = transformed_data[col].dtype
        assert expected == actual, f"Expected {expected} dtype but got {actual} dtype for {col} column"
    