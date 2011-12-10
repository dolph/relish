Relish: Python Object Serialization
===================================

Serialize your python objects into tasty (human-readable) formats.

- Serialize your python object models to/from JSON, YAML or XML.
- Customize the appearance of the serialized data, e.g. for RESTful consumption.

Examples
--------

    >>> @relish
    ... class Foobar():
    ...    @relish
    ...    my_attribute = 'my_value'
    ...
    >>> x = Foobar()
    >>> jsonify.serialize(x)
    '{"foobar": {"my_attribute": "my_value"}}'
    >>> jsonify.deserialize(_)
    <__main__.Foobar instance at 0x10046cf38>
