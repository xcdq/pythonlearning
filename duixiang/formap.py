list_x = [1, 2, 3, 4, 5, 6, 7, 8]
list_y = [1, 2, 3, 4, 5, 6, 7, 8]


def square(x):
    return x*x


# r = map(square, list_x)
# r = map(lambda x: x*x, list_x)
r = map(lambda x, y: x+y, list_x, list_y)
print(list(r))
