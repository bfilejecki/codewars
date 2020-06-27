def filter_list(l):
    return [x for x in l if not isinstance(x, str)]

print(filter_list([1,2,'a','b']))