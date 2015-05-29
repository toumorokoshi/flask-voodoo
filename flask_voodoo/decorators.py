def mutates(f):
    """
    TODO: this will label a function as one that mutates data.
    """
    f.mutates = True
    return f


def is_mutates(f):
    return getattr(f, 'mutates', False)
