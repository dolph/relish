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
        attribute = 'value'
    o = Klass()

    def test_single_str_attr(self):
        s = jsonify.serialize(self.o)
        self.assertEquals(s, '{"klass": {"attribute": "value"}}')

class DeserializerTests(unittest.TestCase):
    pass

class DecoratorTests(unittest.TestCase):
    pass
