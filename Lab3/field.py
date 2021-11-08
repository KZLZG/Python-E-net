# field(goods, 'title') должен выдавать 'Ковер', 'Диван для отдыха'
# field(goods, 'title', 'price') должен выдавать {'title': 'Ковер', 'price': 2000}, 
# {'title': 'Диван для отдыха', 'price': 5300}

goods =  [              
{ 'title': 'Ковер', 'price': 2000, 'color': 'green' }, 
{ 'title': 'Диван для отдыха', 'price': 5300}
]



#генератор
def field(items, *args):     
    assert len(args) > 0
    args_number = len(args)
    if args_number == 1:
        for diction in items:
               yield diction[args[0]]
    elif args_number > 1:
        sum = {}
        for diction in items:
            for arg in args:
                if diction.get(arg) !=None:
                    sum[arg]=diction.get(arg)
            yield sum


'''
#test_field = field(goods, 'title')
test_field = field(goods, 'title', 'color')
while True:
    try:
        print(next(test_field))
    except StopIteration:
        break

'''