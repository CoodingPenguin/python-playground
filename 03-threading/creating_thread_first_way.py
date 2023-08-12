from threading import Thread


def func_4_thread(n_max: int = 1000000) -> None:
    n = 0
    while n < n_max:
        n += 1


my_thread = Thread(target=func_4_thread, args=(10000000,))
my_thread.start()
