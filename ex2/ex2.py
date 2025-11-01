def multiply_all(*args: int)->int:
    if len(args) == 0:
        return 1

    p=1

    for argc in args:
        p=p*argc

    return p