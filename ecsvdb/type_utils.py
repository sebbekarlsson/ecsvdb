def is_numeric(value):
    try:
        float(value)
        return True
    except:
        return False


def quote(value):
    return '"{}"'.format(value)
