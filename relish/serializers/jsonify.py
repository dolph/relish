import json


def serialize(obj):
    """Serialize an object to a string"""
    d = _obj_to_dict(obj)
    d = _wrap_dict(obj, d)
    return json.dumps(d)

def deserialize(string, cls):
    """Deserialize a string, given the class"""
    d = json.loads(string)
    d = _unwrap_dict(d, cls)
    obj = _dict_to_obj(d, cls)
    return obj

def _get_wrapper_name(cls):
    if hasattr(cls, '_relish'):
        name = cls._relish.get('name')
    else:
        name = cls.__name__.lower()

    return name

def _wrap_dict(obj, d):
    """Wrap a dictionary with the class name."""
    name = _get_wrapper_name(obj.__class__)

    if name:
        return {name: d}
    else:
        return d

def _unwrap_dict(d, cls):
    """Unwrap the class name from the dictionary"""
    name = _get_wrapper_name(cls)

    if name:
        return d.get(name)
    else:
        return d

def _obj_to_dict(obj):
    """Walk an object and produce a corresponding dictionary.

    Avoid private attributes and callables.
    """
    d = dict()
    for attr in dir(obj):
        if True and \
                attr[0] != '_' and \
                not callable(getattr(obj, attr)):
            d[attr] = getattr(obj, attr)
    return d

def _dict_to_obj(d, cls):
    """Populate an obj with values from a dictionary."""
    obj = cls()

    for attr in d.keys():
        setattr(obj, attr, d[attr])

    return obj
