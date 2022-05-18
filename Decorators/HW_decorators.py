import time
import random
import requests

def measure_time(func):
    def inner_function(*args, **kwargs):
        start = time.time()
        func(*args, **kwargs)
        end = time.time()
        return end - start

    return inner_function


@measure_time
def some_func(a, b, c, d, e=0, f=2, g="3"):
    time.sleep(a)
    time.sleep(b)
    time.sleep(c)
    time.sleep(d)
    time.sleep(e)
    time.sleep(f)
    return g


some_func(1, 2, 3, 4, e=5, f=6, g="99999")


def function_logging(func):
    def inner_func(*args, **kwargs):
        args_list = args
        kwargs_list = kwargs
        if args_list and kwargs_list:
            print(f"Function {func.__name__} is called with positional arguments: {args_list} and keyword arguments:",
                  ", ".join(f'{key}={value}' for key, value in kwargs_list.items()))
        elif args_list:
            print(f"Function {func.__name__} is called with positional arguments: {args_list}")
        elif kwargs_list:
            print(f"Function {func.__name__} is called with keyword arguments:",
                  ", ".join(f'{key}={value}' for key, value in kwargs_list.items()))
        else:
            print(f"Function {func.__name__} is called with no arguments")
        res_func = func(*args, **kwargs)
        print(f"Function {func.__name__} returns output of type {type(res_func).__name__}")
        return res_func

    return inner_func


@function_logging
def func1():
    return set()


@function_logging
def func2(a, b, c):
    return (a + b) / c


@function_logging
def func3(a, b, c, d=4):
    return [a + b * c] * d


@function_logging
def func4(a=None, b=None):
    return {a: b}


print(func1(), end="\n\n")

print(func2(1, 2, 3), end="\n\n")

print(func3(1, 2, c=3, d=2), end="\n\n")

print(func4(a=None, b=float("-inf")), end="\n\n")


def russian_roulette_decorator(probability=None, return_value=None):
    def decorator(func):
        def inner_func(*args,  **kwargs):
            if random.random() < probability:
                return return_value
            else:
                return func(*args,  **kwargs)
        return inner_func
    return decorator


@russian_roulette_decorator(probability=0.2, return_value="Ooops, your output has been stolen")
def make_request(url):
    return requests.get(url)


for _ in range(10):
    print(make_request("https://google.com"))
