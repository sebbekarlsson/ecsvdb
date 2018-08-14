from ecsvdb.CSVManager import CSVManager


manager = CSVManager()
manager.load('ecsvdb/shards/users.csv')

db = manager.get_db()

points = db.execute('SELECT * FROM users_csv')

manager.save()
