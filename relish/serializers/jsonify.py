import json


def serialize(obj):
    d = _obj_to_dict(obj)
    return json.dumps(d)

def deserialize(string):
    return json.loads(string)

def _wrap_dict(obj, d):
    return {obj.__class__.__name__.lower(): d}

def _obj_to_dict(obj):
    d = dict([(attr, getattr(obj, attr)) for attr in dir(obj) if attr[0] != '_'])
    return _wrap_dict(obj, d)
