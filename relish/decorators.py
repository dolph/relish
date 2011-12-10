"""Decorate your objects with serialization hints"""

# decorator factory
def relish(*args, **kwargs):
    def decorator(obj):
        def wrapper():
            try:
                obj._relish
            except AttributeError:
                obj._relish = {}

            obj._relish.update(**kwargs)
            return obj
        return wrapper()
    return decorator
