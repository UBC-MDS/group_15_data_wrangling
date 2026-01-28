# MIT License
#
# Copyright (c) 2026 Michael Eirikson
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice (including the next
# paragraph) shall be included in all copies or substantial portions of the
# Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

"""
Add a docstring here for the init module.

This might include a very brief description of the package,
its purpose, and any important notes.
"""

from group_15_data_wrangling.categorical_mode import cat_mode_impute
from group_15_data_wrangling.clean_col_names import clean_col_name
from group_15_data_wrangling.encode_income import encode_income_binary
from group_15_data_wrangling.set_dtypes import set_dtype
from .__version__ import __version__

__all__ = ["cat_mode_impute", "clean_col_name", "encode_income_binary", "set_dtype", "__version__"]