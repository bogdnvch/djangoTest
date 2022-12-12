import doctest

################
# Lst is Lst #
################

CONTROL_LST = [1, 7, 2, 7, 3, 7, 4, 7]


def lis_is_lst(a: list, b: list, dlt: int = 1) -> None:
    """
    Реализовать тело функции что бы c == CONTROL_LST
    >>> lis_is_lst([7, 7, 7, 7], [4, 2, 1, 3])
    True
    >>> lis_is_lst(["1234"], [7, 7, 7])
    True
    >>> lis_is_lst([1, 4, 3, 7, 2], [])
    True
    """

    def get_value(l: list):
        res = []
        for element in l:
            if hasattr(element, '__iter__') and not (isinstance(element, str) and len(element) == 1):
                res.extend(get_value(element))
            else:
                res.append(int(element))

        return sorted(list(set(res)))

    c = get_value(a + b)
    max_element = c[-1]
    c.remove(max_element)

    new_lst = []
    for i in c:
        new_lst.append(i)
        new_lst.append(max_element)

    c = new_lst
    c *= dlt
    print(c == CONTROL_LST * dlt)


#############
# The Magic #
#############


def cache(func):
    cache_dict = {}

    def wrapper(*args):
        if 'result' not in cache_dict:
            cache_dict['result'] = func(*args)
            print('Result:', cache_dict['result'])
            return cache_dict['result']
        else:
            var = func(*args)
            if var > cache_dict['result']:
                print('Great Result:', var)
            elif var < cache_dict['result']:
                print('Low Result', var)
            else:
                print('Result:', cache_dict['result'])
                return cache_dict['result']
            return var
    return wrapper

@cache
def decorate_me(some_int):
    """
    Написать декоротор для функции(но не изменять саму функцию) что бы при выполнении следующего кода вывод был следущим:
    >>> decorate_me(25)
    'Result: 50'
    >>> decorate_me(196)
    'Great Result: 392'
    >>> decorate_me(2)
    'Low Result: 4'
    """
    return some_int * 2


def dec(func):
    def wrapper(*args):
        res = func(*args)
        print('???')
    return wrapper


@dec
def magic(stall=[]):
    """
    Написать декоротор для функции(но не изменять саму функцию) что бы при выполнении следующего кода вывод был следущим:

    Переменная _ - unresolved reference

    >>> magic()
    ???
    >>> magic()
    ???
    >>> stall = []
    >>> magic(stall)
    ???
    >>> stall = 45
    >>> magic(stall)
    ???
    >>> stall == _
    ???
    """

    unicorn = '🦄'
    if hasattr(stall, 'append') and callable(stall.append):
        stall.append(unicorn)
    elif hasattr(stall, 'add') and callable(stall.add):
        stall.add(unicorn)
    else:
        stall = unicorn

    return stall


################
# Paint It All #
################

# Заставить сработать функцию как это описано в комментарии, изменять сами классы PaintIt{Color} нельзя
from enum import Enum


class Color(Enum):
    BLACK = '⚫'
    RED = '🔴'
    GREEN = '🟢'


# Необходимо вместо этой реализации класс PaintIt написать свою
# PaintIt = type('_', (type,), {'__new__': lambda *a, **_: type.__new__(*a)})('_', (), {})
def func(cls, *args, **kwargs):
    # print(f"{args = }")
    # print(f"{kwargs = }")
    cls.color = kwargs['color'].value
    object.__init_subclass__()


PaintIt = type('PaintIt', (), {
    '__init_subclass__': func,
    '__str__': lambda self: self.color
})


class PaintItBlack(PaintIt, color=Color.BLACK):
    ...


class PaintItGreen(PaintIt, color=Color.GREEN):
    ...


class PaintItRed(PaintIt, color=Color.RED):
    ...


# функцию изменять нельзя
def paint_it_all():
    """
    >>> paint_it_all()
    ⚫ 🟢 🔴
    """
    print(PaintItBlack(), PaintItGreen(), PaintItRed())


###########
# Doctest #
###########


if __name__ == "__main__":
    globs = globals()
    for test in (
            lis_is_lst, decorate_me, magic, paint_it_all
    ):
        # Use context managers here
        name = test.__name__
        line = "#" * (len(name) + 4)
        print(f"{line}\n# {name} #\n{line}\n")
        doctest.run_docstring_examples(test, globs, name=name)
        print()

