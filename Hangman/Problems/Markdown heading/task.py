def heading(letter, level=0):
    if level == 0:
        return "# {}".format(letter)
    elif level < 1:
        return "# {}".format(letter)
    elif level <= 6:
        return int(level) * "#" + " " + letter
    else:
        return "######" + " " + letter
