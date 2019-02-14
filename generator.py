# generator is a special iterator which still can get value by iter & next
# generator definition : a function which have yield keyword


def test():
     res = (i * 3 for i in range(5))
     print(list(res))


def g_func():
     arg = yield 1000
     print('get param is %s' %arg)
     yield 2000
     return 999


if __name__ == '__main__':
    g = g_func()
    r1 = next(g)
    r2 = g.send('haha')
    # r2 = next(g)
    print(r1)
    print(r2)
    # for i in g_func():
    #    print('for each res is %s' %i)
    try:
        value = next(g)
        print('join try')
        print(value)
    except StopIteration as e:
        # 获取return的返回值
        print(e.value)

    # test()