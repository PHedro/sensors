import re
import unittest

from tempertature_flow.data_generator import _random_params, generate_data_dict, generate_data_points


class GeneratorTestCase(unittest.TestCase):
    def test_generate_data_dict(self):
        result = generate_data_dict()
        self.assertEqual("Sensor", result.get("type"))
        self.assertRegexpMatches(
            result.get("id"),
            r"^[0-9a-f]{8}-[0-9a-f]{4}-4[0-9a-f]{3}-[89ab][0-9a-f]{3}-[0-9a-f]{12}$",
        )
        self.assertIsInstance(result.get("content").get("temperature_f"), float)
        self.assertRegexpMatches(
            result.get("content").get("time_of_measurement"),
            r"^[0-9]{4}-[0-9]{2}-[0-9]{2}T[0-9]{2}:[0-9]{2}:[0-9]{2}\.[0-9]+$",
        )

    def test_random_params(self):
        result = _random_params()
        self.assertRegexpMatches(
            result,
            r"^[0-9a-f]{8}-[0-9a-f]{4}-4[0-9a-f]{3}-[89ab][0-9a-f]{3}-[0-9a-f]{12}$",
        )

    def test_random_params_one_item(self):
        result = _random_params(_array=["expected"], extra_enabled=False)
        self.assertEqual(result, "expected")

    def test_random_params_one_item_extras(self):
        generated = _random_params(_array=["expected"], extra_enabled=True)
        result = generated == "expected" or re.match(
            r"^[0-9a-f]{8}-[0-9a-f]{4}-4[0-9a-f]{3}-[89ab][0-9a-f]{3}-[0-9a-f]{12}$",
            generated
        )
        self.assertTrue(result)

    def test_generate_data_points(self):
        result = next(generate_data_points())
        self.assertRegexpMatches(
            result.get("type"),
            r"^[0-9a-f]{8}-[0-9a-f]{4}-4[0-9a-f]{3}-[89ab][0-9a-f]{3}-[0-9a-f]{12}$",
        )
        self.assertRegexpMatches(
            result.get("id"),
            r"^[0-9a-f]{8}-[0-9a-f]{4}-4[0-9a-f]{3}-[89ab][0-9a-f]{3}-[0-9a-f]{12}$",
        )
        self.assertIsInstance(result.get("content").get("temperature_f"), float)
        self.assertRegexpMatches(
            result.get("content").get("time_of_measurement"),
            r"^[0-9]{4}-[0-9]{2}-[0-9]{2}T[0-9]{2}:[0-9]{2}:[0-9]{2}\.[0-9]+$",
        )
