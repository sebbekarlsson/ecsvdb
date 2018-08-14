from ecsvdb.csv_utils import csv_to_sql


def test_csv_to_sql():
    contents = ''
    with open('ecsvdb/shards/users.csv') as _file:
        contents = _file.read()
    _file.close()

    expected = 'CREATE TABLE users' + \
        ' (id integer,name varchar,lastname varchar);' +\
        'INSERT INTO users (id,name,lastname) VALUES(1,"john","doe");' +\
        'INSERT INTO users (id,name,lastname) VALUES(2,"johanna","doe");' +\
        'INSERT INTO users (id,name,lastname)' + \
        ' VALUES(3,"maria","ericsson");INSERT INTO users (id,name,lastname)' +\
        ' VALUES(4,"anna","carlsson");'

    assert csv_to_sql(contents, 'users') == expected
