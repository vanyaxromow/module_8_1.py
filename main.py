param1 = ''
param2 = ''

try:
    def add_everything_up(a, b):
        global param1, param2
        param1, param2 = str(a), str(b)
        return round(a + b, 3)


    print(add_everything_up(123.456, 'строка'))
    # print(add_everything_up('яблоко', 4215))
    # print(add_everything_up(123.456, 7))

except TypeError as TE:
    print(f'{param1 + param2}, {TE}')
