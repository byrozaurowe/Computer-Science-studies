import inspect
import math


class Function(object):
    def __init__(self, fn):
        self.fn = fn


    def __call__(self, *args, **kwargs):
        fn = Namespace.get_instance().get(self.fn, *args)
        return fn(*args, **kwargs)


    def key(self, args=None):
        if args is None:
            args = inspect.getfullargspec(self.fn).args
        return tuple([
        self.fn.__module__,
        self.fn.__class__,
        self.fn.__name__,
        len(args or []),
        ])


class Namespace(object):
    __instance = None


    def __init__(self):
        if self.__instance is None:
            self.function_map = dict()
            Namespace.__instance = self


    @staticmethod
    def get_instance():
        if Namespace.__instance is None:
            Namespace()
        return Namespace.__instance


    def register(self, fn):
        func = Function(fn)
        self.function_map[func.key()] = fn
        return func


    def get(self, fn, *args):
        func = Function(fn)
        return self.function_map.get(func.key(args=args))


def overload(fn):
  return Namespace.get_instance().register(fn)


@overload
def norm(x,y):
    return math.sqrt(x*x + y*y)
 

@overload
def norm(x,y,z):
    return abs(x) + abs(y) + abs(z)


def main():
    print(norm(2,4))
    print(norm(2,3,4))


if __name__ == "__main__":
    main()