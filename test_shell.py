import sqlite3
from ecsvdb.CSVManager import CSVManager


manager = CSVManager('ecsvdb/shards/')

db = manager.get_db()

try:
    while True:
        try:
            x = raw_input('> ')
            response = db.execute(x)

            for item in response:
                print(item)
        except sqlite3.OperationalError as e:
            print(e)
except KeyboardInterrupt:
    pass

manager.save()
