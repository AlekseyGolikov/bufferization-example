import time

def time_decor(func):
    def wrapper(*args):
        start = time.perf_counter()
        func(*args)
        runtime = time.perf_counter() - start
        print('Функция отработала %6.5f' % runtime)
        with open('out.txt', 'a', encoding='utf-8') as file:
            file.write('\n-----Функция отработала %6.5f----- \n' % runtime)
    return wrapper


class Buffer:

    MAXBUFFERSIZE = 10

    def count(self, n):
        while n > 0:
            yield "Очередное значение %d \n" % n
            n -= 1
        yield "Счет окончен \n"

    @time_decor
    def buffer(self, n):
        chunks = ''
        buffered_size = 0
        for chunk in self.count(n):
            for ch in chunk:
                chunks += ''.join(ch)
                buffered_size += 1
                if buffered_size >= Buffer.MAXBUFFERSIZE:
                    chunks += '...'
                    print(chunks)
                    with open('out.txt', 'a', encoding='utf-8') as f:
                        f.write(chunks)
                    chunks = ''
                    buffered_size = 0

n = 5
b = Buffer()
b.buffer(n)