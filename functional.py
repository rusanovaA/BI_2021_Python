def sequential_map(*args):
    num = list(args[-1])
    for arg in args[:-1]:
        num = list((map(arg, num)))
    return num


def consensus_filter(*args):
    num = list(args[-1])
    for arg in args[:-1]:
        num = list((filter(arg, num)))
    return num


def conditional_reduce(fun_1, fun_2, num):
    num = list((filter(fun_1, num)))
    res = num[0]
    if len(num) == 1:
        return num[0]
    if len(num) == 0:
        raise ValueError('Your list is empty')
    for i in range(len(num) - 1):
        res = fun_2(res, num[i + 1])
    return res


def func_chain(*args):


    def sequential_map(num):
        for arg in args:
            num = arg(num)
        return num
    return sequential_map
