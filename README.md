# Tabulator

This is a library that provides a single function, `tabulate()`, for tabulating
and printing lists of lists or lists of dictionaries.

    >>> from tabulator import tabulate
    >>> data = [
    ...     ['England', 53012],
    ...     ['Scotland', 5295],
    ...     ['Wales', 3063],
    ...     ['N. Ireland', 1811],
    ... ]
    >>> tabulate(data, headers=['Country', 'Pop. (000s)'])
    | Country    | Pop. (000s) |
    +------------+-------------+
    | England    |       53012 |
    | Scotland   |        5295 |
    | Wales      |        3063 |
    | N. Ireland |        1811 |

The code in the library is not the best: there's a lot of duplication which
make it hard to follow.

> Exercise: refactor `tabulator.py` to make the code clearer.

`test_tabulator.py` contains a number of test cases that will help you to
ensure your refactoring has not broken the code.  To run the test cases,
install [`pytest`](http://doc.pytest.org/en/latest/):

    $ pip install pytest

and then run:

    $ pytest
