from ecsvdb.type_utils import is_numeric, quote


def csv_to_sql(csv, table, create=True):
    rows = csv.split('\n')

    table_sql = 'CREATE TABLE {} {}'.format(
        table,
        '({})'.format(
            ','.join(
                '{} {}'.format(col.split(':')[0], col.split(':')[1])
                for col in rows[0].split(';')
            )
        )
    )

    insert_sql = ';'.join(
        'INSERT INTO {} {} {}'.format(
            table,
            '({})'.format(
                ','
                .join(col.split(':')[0] for col in rows[0].split(';'))
            ),
            ','.join(
                [
                    'VALUES({})'
                    .format(
                        ','
                        .join(
                            quote(col) if not is_numeric(col) else col
                            for col in row.split(';')
                        )
                    )
                ]
            )
        ) for row in rows[1:] if row
    )

    return (table_sql + ';' if create else '') + insert_sql + ';'
