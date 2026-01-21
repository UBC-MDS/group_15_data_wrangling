# Welcome to group_15_data_wrangling

|         |        |
|---------|--------|
| Package | [![Latest PyPI Version](https://img.shields.io/pypi/v/group_15_data_wrangling.svg)](https://pypi.org/project/group_15_data_wrangling/) [![Supported Python Versions](https://img.shields.io/pypi/pyversions/group_15_data_wrangling.svg)](https://pypi.org/project/group_15_data_wrangling/)  |
| Meta    | [![Code of Conduct](https://img.shields.io/badge/Contributor%20Covenant-v2.0%20adopted-ff69b4.svg)](CODE_OF_CONDUCT.md) |

## Package Summary

This package aim to simplify the data wrangling for the Adult Census Income dataset found here: <https://www.kaggle.com/datasets/uciml/adult-census-income>. This will make it easier for someone who want to work with the data to quickly get the dataset in a clean format where they can then start analysis right away.

### Functions

- `set_dtype()`
  - sets the data types for each column in the dataset to reduce memory requirements
- `cat_mode_impute()`
  - performs imputation of missing values
- `clean_col_name()`
  - replace "." with "-" and make some names more meaningful
- `encode_income_binary()`
  - encode the target feature, income, as binary

### How this package fits into python ecosystem

There is an existant package called `pyjanitor` that has many useful data cleaning routines. These are general purpose and very powerful. Our package is much more focused on cleaning the specific adult census income dataset. In general `pyjanitor` is a much more useful package, but to tidy our specific dataset our functions will probably do the job with less effort.

`pyjanitor`: <https://github.com/pyjanitor-devs/pyjanitor>

## Get started

You can install this package into your preferred Python environment using pip:

```bash
pip install --index-url https://test.pypi.org/simple/ --extra-index-url https://pypi.org/simple group_15_data_wrangling
```

To use group_15_data_wrangling in your code:

```python
>>> import group_15_data_wrangling
>>> group_15_data_wrangling(census_df)
```

### Documentation

[Documentation can be found here](https://ubc-mds.github.io/group_15_data_wrangling/)

## Contributing

### Setup development environment

`conda env create -f environment.yml`

### Install the package and development dependencies

`pip install -e .[test,dev,docs]`

### To run tests

`pytest --cov=src --cov-branch --cov-report=term-missing`

### build documentation

To build documentation

`quartodoc build`

To preview documentation

`quarto preview`

### deploy documentation

# ADD STUFF HERE

### Github Repo

<https://github.com/UBC-MDS/group_15_data_wrangling>

### Contributors

- Limor Winter
- Shihan Xu
- Zaki Aslam
- Michael Eirikson

## Copyright

- Copyright © 2026 Michael Eirikson.
- Free software distributed under the [MIT License](./LICENSE).
