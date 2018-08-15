import sqlite3
import ntpath
import glob
import os
from read_and_close import read_and_close
from ecsvdb.csv_utils import csv_to_sql


class CSVManager(object):

    def __init__(self, path):
        self.path = path
        self.sqlite = None

    def get_csv_files(self):
        return glob.glob(os.path.join(self.path, '*.csv'))

    def get_loaded_tables(self, as_csv_files=False):
        cursor = self.sqlite.cursor()
        tables = self.sqlite.execute(
            'select name from sqlite_master where type = "table";'
        )

        cursor.close()

        return [
            os.path.join(self.path, (table[0]).replace('_', '.'))
            if as_csv_files else table[0]
            for table in tables
        ]

    def get_table_header(self, table):
        cursor = self.sqlite.cursor()

        header = ';'.join([
            col[1] + ':' + col[2]
            for col in cursor.execute('pragma table_info("{}")'.format(table))
        ])

        cursor.close()

        return header

    def get_db(self):
        self.sqlite = sqlite3.connect(':memory:')
        sql = ''

        for filename in self.get_csv_files():
            contents = read_and_close(filename)

            sql += csv_to_sql(
                contents,
                ntpath.basename(filename).replace('.', '_')
            )

        cursor = self.sqlite.cursor()
        cursor.executescript(sql)
        cursor.close()

        return self.sqlite

    def save(self):
        cursor = self.sqlite.cursor()

        for csv_file in self.get_loaded_tables(True):
            table = ntpath.basename(csv_file).replace('.', '_')
            rows = cursor.execute('SELECT * FROM {}'.format(table))

            new_contents = self.get_table_header(table) + '\n'

            for row in rows:
                new_contents += ';'.join([str(r) for r in row]) + '\n'

            with open(
                csv_file + '.csv' if '.csv' not in csv_file else csv_file,
                'w+'
            ) as _file:
                _file.write(new_contents)
            _file.close()

        cursor.close()

        return self.sqlite
