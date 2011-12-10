import unittest

from relish.serializers import dummify
from relish.serializers import jsonify
from relish.decorators import relish

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
    @relish(name='class')
    @relish(attribute={'name': 'value'})
    class Klass():
        attribute = None

    o = Klass()

    @relish(name=None)
    class Nameless():
        attribute = None

    anon = Nameless()
    anon.attribute = 7

    def test_class_decorator(self):
        self.assertEqual(self.o._relish, {'name': 'class', 'attribute': {'name': 'value'}})

    def test_serializing_unwrapped_class(self):
        s = jsonify.serialize(self.anon)
        self.assertEquals(s, '{"attribute": 7}')

    def test_deserializing_unwrapped_class(self):
        s = '{"attribute": 7}'
        o = jsonify.deserialize(s, self.Nameless)
        self.assertTrue(isinstance(o, self.Nameless))
        self.assertEquals(o.attribute, 7)
