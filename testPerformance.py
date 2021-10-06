import cProfile
import memory_profiler


# 1.442s
@memory_profiler.profile(precision=4)
def list_comprehension(x):
    result = [i * i for i in range(x)]
    return result


# 3.648s
@memory_profiler.profile(precision=4)
def list_append(x):
    result = []
    for i in range(x):
        result.append(i * i)
    return result


# 3.675s
@memory_profiler.profile(precision=4)
def list_extend(x):
    result = []
    result.extend(i * i for i in range(x))
    return


# 3.24s
def for_loop(d_1, d_2):
    result = {}

    for k in d_1:
        result[k] = d_1[k]
    for k in d_2:
        result[k] = d_2[k]

    return result


# 1.36s
def update_method(d_1, d_2):
    result = {}
    result.update(d_1)
    result.update(d_2)
    return result


# 2.464s
def dict_comprehension(d_1, d_2):
    result = {k: v for d in [d_1, d_2] for k, v in d.items()}
    return result


# 1.361s
def dict_kwargs(d_1, d_2):
    result = {**d_1, **d_2}
    return result


# @memory_profiler.profile(precision=4)
def mergefiles():
    import glob
    import os

    # /mnt/d/Users/JHG/Documents/data/vcs/GitHub/kodicowebmodule/

    log_files = [
        file
        for file in os.listdir(
            "d:\\Users\\JHG\\Documents\\data\\vcs\\GitHub\\kodicowebmodule\\"
        )
        if file.endswith(".csv")
    ]
    print(f"files={log_files}")
    # new_file = "newfile.csv"
    # with open(new_file, "ab+") as nf:
    #     for logfile in log_files:
    #         with open(logfile, "rb") as logf:
    #             nf.write(logf.read(201600))


# cProfile.run("list_comprehension(1000000)")
# cProfile.run("list_append(1000000)")
# cProfile.run("list_extend(1000000)")
cProfile.run("mergefiles")