import time

def time_taken(func):
    def decorator():
        print("I am about to call this function")
        start = time.time()
        print("start: ", start)
        func()
        print("I am done calling this function")
        end = time.time()
        print("end: ", end)
        total_time = end - start
        print("This function took {} seconds".format(total_time))

    return decorator


@time_taken
def iterate(n):
    print("Reached here")
    r = []
    for i in range(n):
        r.append(i)

if __name__ == '__main__':

    iterate()