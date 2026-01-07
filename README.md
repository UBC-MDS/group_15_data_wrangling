# Welcome to group_15_data_wrangling

|        |        |
|--------|--------|
| Package | [![Latest PyPI Version](https://img.shields.io/pypi/v/group_15_data_wrangling.svg)](https://pypi.org/project/group_15_data_wrangling/) [![Supported Python Versions](https://img.shields.io/pypi/pyversions/group_15_data_wrangling.svg)](https://pypi.org/project/group_15_data_wrangling/)  |
| Meta   | [![Code of Conduct](https://img.shields.io/badge/Contributor%20Covenant-v2.0%20adopted-ff69b4.svg)](CODE_OF_CONDUCT.md) |

*TODO: the above badges that indicate python version and package version will only work if your package is on PyPI.
If you don't plan to publish to PyPI, you can remove them.*

group_15_data_wrangling is a project that (describe what it does here).

## Package Summary

This package aim to simplify the data wrangling for the Adult Census Income dataset found here: https://www.kaggle.com/datasets/uciml/adult-census-income. This will make it easier for someone who want to work with the data to quickly get the dataset in a clean format where they can then start analysis right away.

### Functions

- set_dtype()
  - sets the data types for each column in the dataset to reduce memory requirements
- cat_knn_impute()
  - performs imputation of missing values
- OTHER_FUNC()
- OTHER_FUNC()

### How this package fits into python ecosystem

There is an existant package called `pyjanitor` that has many useful data cleaning routines. These are general purpose and very powerful. Our package is much more focused on cleaning the specific adult census income dataset. In general `pyjanitor` is a much more useful package, but to tidy our specific dataset our functions will probably do the job with less effort.

`pyjanitor`: <https://github.com/pyjanitor-devs/pyjanitor>

## Get started

You can install this package into your preferred Python environment using pip:

```bash
$ pip install group_15_data_wrangling
```

TODO: Add a brief example of how to use the package to this section

To use group_15_data_wrangling in your code:

```python
>>> import group_15_data_wrangling
>>> group_15_data_wrangling.hello_world()
```

## Contributors

- Limor Winter
- Shihan Xu
- Zaki Aslam
- Michael Eirikson

## Copyright

- Copyright © 2026 Michael Eirikson.
- Free software distributed under the [MIT License](./LICENSE).
