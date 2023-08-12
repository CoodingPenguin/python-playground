from threading import Thread


class MyThread(Thread):
    def __init__(self, n_max=1000000) -> None:
        Thread.__init__(self)
        self.n_max = n_max

    def run(self) -> None:
        n = 0
        while n < self.n_max:
            n += 1


my_thread = MyThread(n_max=1000000)
