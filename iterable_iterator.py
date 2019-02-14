# before write coroutine code, begin with iterable .. from  advanced python of middle part
# iterable object: a object that provide __iter__ magic method
# iterator object: a object that provide __iter__ & __next__ magic method
# iter method will call iterable __iter__, next method will call iterator __next__
# for item in Iterable origin is get iterator by iter() func, then call iterator's next until get StopIteration exception, by the way assign func next's value to item(for item in ...)

# iterator use case:  如列表推导式, 当下一个值是通过上一个值推导得出，这样便无需一次性缓存整个数据

from collections.abc import Iterable


# custom iterable object
class MyIterableObj:

    def __init__(self, list_source):
        self.__list = list_source

    def __iter__(self):
        return MyIteratorObj(self.__list)


# custom iterator
class MyIteratorObj:
    def __init__(self, list_data):
        self.__list = list_data
        self.__i = -1

    def __iter__(self):
        return self

    def __next__(self):
        self.__i += 1
        if len(self.__list) > self.__i:
            return self.__list[self.__i]
        else:
            # * Why raise exception no bracket : type in ipython3 it's run ok
            raise StopIteration 


def test(obj):
    res = isinstance(obj, Iterable)
    print('check custom iterable obj is %s' %res)
    _iter = iter(obj)
    while True:
        try:
            res = next(_iter)
            print('custom iterator next val is %s' %res)
        except StopIteration:
            print('loop end!')
            break


if __name__ == "__main__":
    _l = [1, 5, 9]
    test(MyIterableObj(_l))
