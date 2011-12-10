import unittest

from serializers import dummify
from serializers import jsonify


class DummySerializerTests(unittest.TestCase):
    def test_dummy_serializer(self):
        self.assertEquals(dummify.serialize(object()), str())

    def test_dummy_deserializer(self):
        self.assertTrue(isinstance(dummify.deserialize(str()), object))


class SerializerTests(unittest.TestCase):
    class Klass():
        attribute = None

    o = Klass()
    o.attribute = 'value'

    def test_serialize_single_str_attr(self):
        s = jsonify.serialize(self.o)
        self.assertEquals(s, '{"klass": {"attribute": "value"}}')

    def test_deserialize_single_str_attr(self):
        s = '{"klass": {"attribute": "value"}}'
        o = jsonify.deserialize(s, self.Klass)
        self.assertTrue(isinstance(o, self.Klass))
        self.assertEquals(o.attribute, 'value')


class DecoratorTests(unittest.TestCase):
    pass
