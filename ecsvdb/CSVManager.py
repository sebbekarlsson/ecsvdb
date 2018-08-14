import sqlite3
import ntpath
from ecsvdb.csv_utils import csv_to_sql


class CSVManager(object):

    def __init__(self):
        self.csv_files = []
        self.sqlite = None

    def load(self, filename):
        self.csv_files.append(filename)

    def unload(self, filename):
        self.csv_files.remove(filename)

    def get_db(self):
        self.sqlite = sqlite3.connect(':memory:')
        sql = ''

        for filename in self.csv_files:
            contents = ''
            with open(filename) as _file:
                contents = _file.read()
            _file.close()

            sql += csv_to_sql(
                contents,
                ntpath.basename(filename).replace('.', '_')
            )

        cursor = self.sqlite.cursor()
        cursor.executescript(sql)
        cursor.close()

        return self.sqlite

    def save(self):
        if not self.sqlite:
            return None

        cursor = self.sqlite.cursor()

        for csv_file in self.csv_files:
            contents = ''
            with open(csv_file) as _file:
                contents = _file.read()
            _file.close()
            csv_rows = contents.split('\n')

            table = ntpath.basename(csv_file).replace('.', '_')
            rows = cursor.execute('SELECT * FROM {}'.format(table))

            new_contents = csv_rows[0] + '\n'

            for row in rows:
                print(row)
                new_contents += ';'.join([str(r) for r in row]) + '\n'

            with open(csv_file, 'w+') as _file:
                _file.write(new_contents)
            _file.close()
