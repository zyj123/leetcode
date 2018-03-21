import time,sys
from asyncio import sleep
def inner_generator():
    i = 0
    j = 0
    while True:
        i = yield j
        j = i+0.5
        # time.sleep(3)
        if i > 10:
            raise StopIteration



def outer_generator():
    print("do something before yield")
    from_inner = 0
    from_outer = 1
    g = inner_generator()
    x = g.send(None)
    print('x=%s'%(x,))
    while 1:
        try:
            from_inner = g.send(from_outer)
            print(from_inner)
            from_outer = yield from_inner
            print(from_outer)
            sys.exit()
        except StopIteration:
            break


def main():
    g = outer_generator()
    g.send(None)
    i = 0
    while 1:
        try:
            i = g.send(i + 1)
            print(i)
        except StopIteration:
            break


if __name__ == '__main__':
    main()
