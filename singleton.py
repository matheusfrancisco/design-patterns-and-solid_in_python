"""
Singleton

It's pretty easy to implement a sloppy Singleton.
You just need to hide constructor and implment a
static creation method.

The same class behaves incorrectly in a multithreaded environment. Multiple threads 
can call the creation method simultaneously and get several instances of Singleton class.
"""


from __future__ import annotations
from typing import Optional

class SingletonMeta(type):
    """
    The Singleton class can be implemented in different ways in Python. Some
    possible methods include: base class, decorator, metaclass. We will use the
    metaclass because it is best suited for this purpose.
    """

    _instance: Optional[Singleton] = None

    def __call__(self) -> Singleton:
        if self._instance is None:
            self._instance = super().__call__()
        return self._instance



class Singleton(metaclass=SingletonMeta):
    def logic(self):
        pass



singleton1 = Singleton()
singleton2 = Singleton()


if id(singleton1) == id(singleton2):
    print("Singleton works, both variables contain the same instance.")
else:
    print("Erro")


