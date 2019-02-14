# raise Exception()
# custom Exception
# try except else finally

class CustomExcept(Exception):

    def __init__(self, lengh, atlast):
        self.lengh = lengh
        self.atlast = atlast

    def __str__(self):
        return 'The length that you input is % at last %s ' %(self.lengh, self.atlast)


def except_():
    raise Exception('custom error')

def custom_except():
    raise CustomExcept(10, 20)

def except_deal(func_):
    try:
        func_()
    except Exception as res:
        print('Get except is %s' % res)
    else:
        print('No exception!')
    finally:
        print('Finally run')

if __name__ == "__main__": 
    # except_deal(except_)
    except_deal(custom_except)
    