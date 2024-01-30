

x, y, *z = ('a', 'b', 'c', 'd')
print(z)
print(*z)


def foo(left: 'int', right: 'list') -> int:  # specifying int and list don't force the type
    # pass  # placeholder for future code
    return 5


foo(1,3)
def food(left, right, middle=7):  # always put defaults at the end
    """

    :param left: lower number
    :param right: higher number
    :param middle: something in the middle
    :return: a list of Chris' favourite foods
    """
    pass


# food()

def fook(left, right):
    return left, right, (left+right)/2  # can return an implicit tuple


returned_tuple = fook(2,10)
print(*returned_tuple)

x,y,z = fook(2,10)
print(x,y,z)


# time for args and kwargs
def goo(*args):
    print(f'goo({args})')

p = (1,2,3,4)
goo(p)
goo(1,2,3,4,5,6)


def goop(val1, val2,*tupleizer):
    print(f'goop({val1},{val2},{tupleizer}')


goop(1,2,3,4,5,6)


def hoo(**kvargs):
    print(f'hoo({kvargs})')
    for key in kvargs.keys() :
        print(f'{key} : {kvargs[key]}')
    # for key, value in kvargs !!!! WHY DIDNT WORK??
    # here's the proper syntax:
    for key, value in kvargs.items():
        print(f'{key} : {value}')


hoo(student1='Mathieu',student2='Chris',student3='Taimoor',student4='Bohdan')


# TOPIC: how do you sort a dictionary?

def A():
    yield 1
    yield 2
    yield 3


print(type(A()))
for index, item in enumerate(A()):
    print(f"{index}: {item}")


# yields - NEXT CLASS!!
def backwards(seq) :
    for index in range(1,len(seq)+1):
        yield seq[-index]


sample = (1,2,3,4)
print(backwards(sample))
print("Trying next: ", next(backwards(sample)))

for item in backwards(sample):
    print(item)
