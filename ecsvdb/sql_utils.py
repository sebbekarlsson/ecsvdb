from ecsvdb.type_utils import is_numeric


def get_sql_type(value):
    return 'integer' if is_numeric(value) else 'varchar'
