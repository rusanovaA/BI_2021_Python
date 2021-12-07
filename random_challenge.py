import random
import numpy as np
from timeit import default_timer as timer
import matplotlib.pyplot as plt

# 1


time_random = []
i = 1
while i <= 100:
    start = timer()
    rcount = [random.uniform(0, 1) for x in range(i)]
    i += 1
    end = timer()
    time_i = end-start
    time_random.append(time_i)

    time_np = []
    i = 1
    while i <= 100:
        start = timer()
        rcount = np.random.uniform(size=i)
        i += 1
        end = timer()
        time_i = end-start
        time_np.append(time_i)

count = [i for i in range(100)]

plt.figure(figsize=(10, 5))
plt.bar(count, time_random, color='forestgreen', label='Time random')
plt.bar(count, time_np, color='mediumaquamarine', label='Time numpy')
plt.legend()
plt.xlabel('The number of calculated numbers')
plt.ylabel('Time')
plt.show()


# 2


def if_sort(num_list):
    len_list = len(num_list)
    for i in range(1, len_list):
        if num_list[i - 1] <= num_list[i]:
            continue
        else:
            return "Your list is not sorted"
    return "Your list is sorted"


time_random_m = []
time_random_sd = []
i = 2
while i <= 100:
    start = timer()
    rcount = sorted(np.random.randint(0, 100, size=i))
    end = timer()
    time_i_1 = end-start
    start = timer()
    rcount = sorted(np.random.randint(0, 100, size=i))
    end = timer()
    time_i_2 = end-start
    start = timer()
    rcount = sorted(np.random.randint(0, 100, size=i))
    end = timer()
    time_i_3 = end-start
    time_i = [time_i_1, time_i_2, time_i_3]
    time_im = np.mean(time_i)
    time_random_m.append(time_im)
    time_i_sd = np.std(time_i)
    time_random_sd.append(time_i_sd)
    i += 1


array_s = [i for i in range(2, 101)]

plt.figure(figsize=(10, 5))
plt.plot(array_s, time_random_m, color='forestgreen', label='Mean time of 3 runs')
plt.plot(array_s, time_random_sd, color='mediumaquamarine', label='Standart deviation of time of 3 runs')
plt.legend()
plt.xlabel('Number of numbers in the list')
plt.ylabel('Time')
plt.show()


# 3


may_go = [-1, 0, 1]
num_steps = 1500
num_col = num_steps + 1
initial = np.zeros((1, 2))
steps = np.random.choice(a=may_go, size=(num_steps, 2))
path = np.concatenate([initial, steps]).cumsum(0)
start = path[:1]
stop = path[-1:]

plt.figure(figsize=(10, 5))
colors = np.random.rand(num_col)
plt.scatter(path[:, 0], path[:, 1], c=colors, alpha=0.4)
plt.title('Random walk with random colors')
plt.show()


# 4


# There could be your advertisement here. Or my triangle.
# excuse me


# 5


my_text = list(input().split())
final = []
for i in my_text:
    if len(i) > 3:
        mod = list(i[1:-1])
        np.random.shuffle(mod)
        final.append(i[0] + ''.join(mod) + i[-1])
    else:
        final.append(i)
final_str = ' '.join(final)
print(final_str)
