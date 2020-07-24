def get_percentage(x, round_digits=None):
    if round_digits == None:
        return (f'{round(x * 100)}%')
    else:
        res = round(x * 100, round_digits)
        return (f'{res}%')
