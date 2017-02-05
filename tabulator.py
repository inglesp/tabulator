def tabulate(data, headers=None, key_order=None):
    if isinstance(data[0], list):
        tabulate_lists(data, headers=headers)
    elif isinstance(data[0], dict):
        tabulate_dicts(data, headers=headers, key_order=key_order)
    else:
        assert False, 'First record in data of unexpected type: {}'.format(type(data[0]))


def tabulate_lists(data, headers=None):
    widths = []
    first_record = True
    for record in data:
        for ix, item in enumerate(record):
            if first_record:
                widths.append(len(str(item)))
            else:
                widths[ix] = max(len(str(item)), widths[ix])
        first_record = False

    if headers is not None:
        if headers == 'first_row':
            for ix, item in enumerate(data[0]):
                if isinstance(item, int):
                    item = str(item).rjust(widths[ix])
                else:
                    item = item.ljust(widths[ix])

                print('| ', end='')
                print(item, end='')
                print(' ', end='')
            print('|')

            data = data[1:]
        else:
            for ix, header in enumerate(headers):
                widths[ix] = max(len(header), widths[ix])

                item = header.ljust(widths[ix])
                print('| ', end='')
                print(item, end='')
                print(' ', end='')
            print('|')

        for width in widths:
            print('+', end='')
            print('-' * (width + 2), end='')
        print('+')

    for record in data:
        for ix, item in enumerate(record):
            if isinstance(item, int):
                item = str(item).rjust(widths[ix])
            else:
                item = item.ljust(widths[ix])

            print('| ', end='')
            print(item, end='')
            print(' ', end='')
        print('|')


def tabulate_dicts(data, headers=None, key_order=None):
    widths = {}
    first_record = True
    for record in data:
        for key, value in record.items():
            if first_record:
                widths[key] = (len(str(value)))
            else:
                widths[key] = max(len(str(value)), widths[key])
        first_record = False

    if headers:
        if headers == 'keys':
            if key_order is None:
                for key in data[0].keys():
                    widths[key] = max(len(key), widths[key])
                    print('| ', end='')
                    print(key.ljust(widths[key]), end='')
                    print(' ', end='')
            else:
                for key in key_order:
                    widths[key] = max(len(key), widths[key])
                    print('| ', end='')
                    print(key.ljust(widths[key]), end='')
                    print(' ', end='')
            print('|')

        else:
            for key, header in zip(key_order, headers):
                widths[key] = max(len(header), widths[key])

                item = header.ljust(widths[key])
                print('| ', end='')
                print(item, end='')
                print(' ', end='')
            print('|')

        if key_order is None:
            for key in data[0].keys():
                print('+', end='')
                print('-' * (widths[key] + 2), end='')
        else:
            for key in key_order:
                print('+', end='')
                print('-' * (widths[key] + 2), end='')
        print('+')

    for record in data:
        if key_order is None:
            for key in data[0].keys():
                value = record[key]
                if isinstance(value, int):
                    value = str(value).rjust(widths[key])
                else:
                    value = value.ljust(widths[key])

                print('| ', end='')
                print(value, end='')
                print(' ', end='')
        else:
            for key in key_order:
                value = record[key]
                if isinstance(value, int):
                    value = str(value).rjust(widths[key])
                else:
                    value = value.ljust(widths[key])

                print('| ', end='')
                print(value, end='')
                print(' ', end='')
        print('|')
