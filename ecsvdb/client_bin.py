import argparse
import sqlite3
from ecsvdb.CSVManager import CSVManager


parser = argparse.ArgumentParser()
parser.add_argument(
    '--dir',
    metavar='d', type=str,
    help='an integer for the accumulator'
)

args = parser.parse_args()


def run():
    manager = CSVManager(args.dir)

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
