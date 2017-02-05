from tabulator import tabulate


def test_tabulate_lists(capsys):
    data = [
        ['England', 53012],
        ['Scotland', 5295],
        ['Wales', 3063],
        ['N. Ireland', 1811],
    ]

    tabulate(data)
    out, err = capsys.readouterr()
    
    expected_out = '''
| England    | 53012 |
| Scotland   |  5295 |
| Wales      |  3063 |
| N. Ireland |  1811 |
'''.lstrip()

    assert out == expected_out


def test_tabulate_lists_with_headers(capsys):
    data = [
        ['England', 53012],
        ['Scotland', 5295],
        ['Wales', 3063],
        ['N. Ireland', 1811],
    ]

    tabulate(data, headers=['Country', 'Pop. (000s)'])
    out, err = capsys.readouterr()
    
    expected_out = '''
| Country    | Pop. (000s) |
+------------+-------------+
| England    |       53012 |
| Scotland   |        5295 |
| Wales      |        3063 |
| N. Ireland |        1811 |
'''.lstrip()

    assert out == expected_out


def test_tabulate_lists_with_first_row_as_headers(capsys):
    data = [
        ['Country', 'Pop. (000s)'],
        ['England', 53012],
        ['Scotland', 5295],
        ['Wales', 3063],
        ['N. Ireland', 1811],
    ]

    tabulate(data, headers='first_row')
    out, err = capsys.readouterr()
    
    expected_out = '''
| Country    | Pop. (000s) |
+------------+-------------+
| England    |       53012 |
| Scotland   |        5295 |
| Wales      |        3063 |
| N. Ireland |        1811 |
'''.lstrip()

    assert out == expected_out


def test_tabulate_dicts(capsys):
    data = [
        {'country': 'England', 'population': 53012},
        {'country': 'Scotland', 'population': 5295},
        {'country': 'Wales', 'population': 3063},
        {'country': 'N. Ireland', 'population': 1811},
    ]

    tabulate(data)
    out, err = capsys.readouterr()
    
    expected_outs = [
        '''
| England    | 53012 |
| Scotland   |  5295 |
| Wales      |  3063 |
| N. Ireland |  1811 |
'''.lstrip(),
        '''
| 53012 | England    |
|  5295 | Scotland   |
|  3063 | Wales      |
|  1811 | N. Ireland |
'''.lstrip()
    ]

    assert out in expected_outs


def test_tabulate_dicts_with_keys_as_headers(capsys):
    data = [
        {'country': 'England', 'population': 53012},
        {'country': 'Scotland', 'population': 5295},
        {'country': 'Wales', 'population': 3063},
        {'country': 'N. Ireland', 'population': 1811},
    ]

    tabulate(data, headers='keys')
    out, err = capsys.readouterr()
    
    expected_outs = [
        '''
| country    | population |
+------------+------------+
| England    |      53012 |
| Scotland   |       5295 |
| Wales      |       3063 |
| N. Ireland |       1811 |
'''.lstrip(),
        '''
| population | country    |
+------------+------------+
|      53012 | England    |
|       5295 | Scotland   |
|       3063 | Wales      |
|       1811 | N. Ireland |
'''.lstrip()
    ]

    assert out in expected_outs


def test_tabulate_dicts_with_key_order(capsys):
    data = [
        {'country': 'England', 'population': 53012},
        {'country': 'Scotland', 'population': 5295},
        {'country': 'Wales', 'population': 3063},
        {'country': 'N. Ireland', 'population': 1811},
    ]

    tabulate(data, key_order=['population', 'country'])
    out, err = capsys.readouterr()
    
    expected_out = '''
| 53012 | England    |
|  5295 | Scotland   |
|  3063 | Wales      |
|  1811 | N. Ireland |
'''.lstrip()

    assert out == expected_out


def test_tabulate_dicts_with_key_order_and_headers(capsys):
    data = [
        {'country': 'England', 'population': 53012},
        {'country': 'Scotland', 'population': 5295},
        {'country': 'Wales', 'population': 3063},
        {'country': 'N. Ireland', 'population': 1811},
    ]

    tabulate(data, key_order=['population', 'country'], headers=['Pop. (000s)', 'Country'])
    out, err = capsys.readouterr()
    
    expected_out = '''
| Pop. (000s) | Country    |
+-------------+------------+
|       53012 | England    |
|        5295 | Scotland   |
|        3063 | Wales      |
|        1811 | N. Ireland |
'''.lstrip()

    assert out == expected_out
