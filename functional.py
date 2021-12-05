def sequential_map(*args):
    num = list(args[-1])
    for arg in args[:-1]:
        res = list((map(arg, num)))
        num = res
    return list(map(int, res))


def consensus_filter(*args):
    num = list(args[-1])
    for arg in args[:-1]:
        res = list((filter(arg, num)))
        num = res
    return list(map(int, res))


def conditional_reduce(fun_1, fun_2, num):
    res = []
    for i in range(len(num)):
        if fun_1(num[i]) is True and fun_1(num[i + 1]) is True:
            res.append(fun_2(num[i], num[i + 1]))
        else:
            continue
    return sum(res)


# I could only come up with non-working functions :(


def func_chain_2(*args):
    return [arg for arg in args]


def func_chain(*args):
    return args
