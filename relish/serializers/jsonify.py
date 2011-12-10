import json


def serialize(obj):
    d = _obj_to_dict(obj)
    d = _wrap_dict(obj, d)
    return json.dumps(d)

def deserialize(string, cls):
    d = json.loads(string)
    d = _unwrap_dict(d, cls)
    obj = _dict_to_obj(d, cls)
    return obj

def _wrap_dict(obj, d):
    return {obj.__class__.__name__.lower(): d}

def _unwrap_dict(d, cls):
    assert len(d.keys()) == 1
    return d.get(cls.__name__.lower())

def _obj_to_dict(obj):
    d = dict()
    for attr in dir(obj):
        if True and \
                attr[0] != '_' and \
                not callable(getattr(obj, attr)):
            d[attr] = getattr(obj, attr)
    return d

def _dict_to_obj(d, cls):
    obj = cls()

    for attr in d.keys():
        setattr(obj, attr, d[attr])

    return obj
