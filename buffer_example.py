MAXBUFFERSIZE = 10

def count(n):
    while n > 0:
        yield "Очередное значение %d \n" % n
        n -= 1
    yield "Счет окончен \n"

chunks = ''
buffered_size = 0
for chunk in count(5):
    for ch in chunk:
        chunks += ''.join(ch)
        buffered_size += 1
        if buffered_size >= MAXBUFFERSIZE:
            chunks += '...'
            print(chunks)
            with open('out.txt', 'a', encoding='utf-8') as f:
                f.write(chunks)
            chunks = ''
            buffered_size = 0
