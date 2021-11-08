# Генерация целых чисел

def gen_prime(x):
    multiples = []
    results = []
    for i in range(2, x+1):
        if i not in multiples:
            results.append(i)
            for j in range(i*i, x+1, i):
                multiples.append(j)

    return results
def test():
    """Stupid test function"""
    L = []
    for i in range(100):
        L.append(i)

import timeit

# Засекаем время
if __name__ == '__main__':
    start_time = timeit.default_timer()
    test()
    print(timeit.default_timer() - start_time)
    print(timeit.timeit("test()", setup="from __main__ import test"))
    #print(timeit.timeit("gen_prime(3000)", setup="from __main__ import gen_prime"))