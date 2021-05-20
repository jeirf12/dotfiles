from functools import reduce
from typing import List, Callable, TypeVar

dollars = ["32$", "15$", "12$", "17$", "20$"]

prices = map(lambda dollar: int(dollar[0:-1]), dollars)
expensive = filter(lambda price: price >=20, prices)
#Primera forma de hacer reduce
#tot = sum(expensive)
#otra forma es
tot = reduce(lambda acum,price: acum + price, expensive, 0);

E = TypeVar('E')
R = TypeVar('R')
A = TypeVar('A')

def Map(iterable: List[E],func:Callable[[E], R]) -> List[R]:
    mapped:List[R]=[]
    for e in iterable:
        mapped.append(func(e))
    return mapped

def Filter(iterable: List[E], func:Callable[[E], bool]) -> List[E]:
    filtered:List[E] = []
    for e in iterable:
        if func(e):
            filtered.append(e)
    return filtered

def Reduce(iterable: List[E], func:Callable[[E, A], A], acum:A) -> A:
    for e in iterable:
        acum = func(acum, e)
    return acum

prices = Map(dollars, lambda dollar: int(dollar[0:-1]))
expensive = Filter(prices,lambda price: price >=20)
tot = Reduce(expensive, lambda acum,price: acum + price, 0);
print(tot)
