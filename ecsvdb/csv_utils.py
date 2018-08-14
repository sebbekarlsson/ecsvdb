from ecsvdb.type_utils import is_numeric, quote


def csv_to_sql(csv, table):
    rows = csv.split('\n')

    return 'INSERT INTO {} {} {}'.format(
        table,
        '({})'.format(','.join(rows[0].split(';'))),
        ','.join(
            [
                'VALUES({})'
                .format(
                    ','
                    .join(
                        quote(col) if not is_numeric(col) else col
                        for col in row.split(';')
                    )
                ) for row in rows[1:] if row
            ]
        )
    ) if rows else None
