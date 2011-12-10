import unittest

from serializers import dummify
from serializers import jsonify


class DummySerializerTests(unittest.TestCase):
    def test_dummy_serializer(self):
        self.assertEquals(dummify.serialize(object()), str())

    def test_dummy_deserializer(self):
        self.assertTrue(isinstance(dummify.deserialize(str()), object))


class JsonSerializerTests(unittest.TestCase):
    class Klass():
        _private = 1

        attribute = None
        things = []

        def method(self):
            pass

        def _private(self):
            pass

        def __str__(self):
            pass

    o = Klass()
    o.attribute = 'value'
    o.things = ['a', 2, 'three']

    def test_serialize(self):
        s = jsonify.serialize(self.o)
        self.assertEquals(s, '{"klass": {"attribute": "value", "things": ["a", 2, "three"]}}')

    def test_deserialize(self):
        s = '{"klass": {"attribute": "value", "things": ["a", 2, "three"]}}'
        o = jsonify.deserialize(s, self.Klass)
        self.assertTrue(isinstance(o, self.Klass))
        self.assertEquals(o.attribute, 'value')
        self.assertEquals(o.things, ["a", 2, "three"])


class DecoratorTests(unittest.TestCase):
    pass
