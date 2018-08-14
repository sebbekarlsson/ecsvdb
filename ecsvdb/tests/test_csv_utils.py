from ecsvdb.csv_utils import csv_to_sql


def test_csv_to_sql():
    contents = ''
    with open('ecsvdb/shards/users.csv') as _file:
        contents = _file.read()
    _file.close()

    assert csv_to_sql(contents, 'users') == 'INSERT INTO users' +\
        ' (id,name,lastname) ' +\
        'VALUES(1,"john","doe"),VALUES(2,"johanna","doe"),' + \
        'VALUES(3,"maria","ericsson"),' +\
        'VALUES(4,"anna","carlsson")'
