import timeit

class cm_timer_1:

    def __init__(self):
        self.start_time = 0
        
    def __enter__(self):
        self.start_time = timeit.default_timer()
        return self.start_time
        
    def __exit__(self,  exp_type, exp_value, traceback):
        if exp_type is not None:
            print(exp_type, exp_value, traceback)
        else:
             return print(timeit.default_timer()-self.start_time)


from contextlib import contextmanager
@contextmanager
def cm_timer_2():
    start_time = timeit.default_timer()
    yield True
    print(timeit.default_timer() - start_time)

'''
with cm_timer_1():
    print('1')


with cm_timer_2():
    print('1')


'''