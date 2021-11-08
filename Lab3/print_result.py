def print_result(some_func):

        def decorated(*args, **kwargs):

            

            result = some_func(*args, **kwargs)

            print("Run method: " + str(some_func.__name__))

            if type(result) == list:

                for i in result:

                    print(i)

            elif type(result) == dict:

                for key in result:

                    print('{} = {}'.format(key, result.get(key)))   

            else: print(result)

        

            return result



        return decorated





@print_result

def test_1():

    return 1





@print_result

def test_2():

    return 1





@print_result

def test_3(arg):

    return arg





@print_result

def test_4(func):

    return func





if __name__ == '__main__':

    print('!!!!!!!!')

    test_3(1)

    test_4(test_1())

