@staticmethod
def is_null_or_empty(s):
    return s is None or len(s.strip()) == 0
