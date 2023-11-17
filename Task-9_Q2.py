data = [10, 'hello', 22, 'world', 37, '42', 'Guvi']
check_type = lambda x: isinstance(x, int) or isinstance(x, str)
result = all(map(check_type, data))
if result:
    print("All elements are either integers or strings.")
else:
    print("Not all elements are either integers or strings.")
