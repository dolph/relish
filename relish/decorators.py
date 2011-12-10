"""Decorate your objects with serialization hints"""

# decorator factory
def relish(*args, **kwargs):
    def decorator(obj):
        def wrapper():
            obj._relish = kwargs
            return obj()
        return wrapper
    return decorator
