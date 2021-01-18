day = 6
switcher = {
    0: 'sunday',
    1: 'monday',
    2: 'tuesday'
}
# day_name = switcher
day_name = switcher.get(day, 'undown')
print(day_name)
