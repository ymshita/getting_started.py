def counter():
    count = 0
    def _increment():
        nonlocal count
        count += 1
        return count

    return _increment