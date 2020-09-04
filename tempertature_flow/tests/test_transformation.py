import unittest

from tempertature_flow.data_transformation import (
    enhance_temperature,
    fahrenheit_to_celsius,
)


class TemperatureTransformationTestCase(unittest.TestCase):
    def test_fahrenheit_to_celsius_32_0(self):
        result = fahrenheit_to_celsius(32)
        expected = 0
        self.assertEqual(expected, result)

    def test_fahrenheit_to_celsius_100_37_7778(self):
        result = fahrenheit_to_celsius(100)
        expected = 37.77777777777778
        self.assertEqual(expected, result)

    def test_fahrenheit_to_celsius_72_22_2222(self):
        result = fahrenheit_to_celsius(72)
        expected = 22.22222222222222
        self.assertEqual(expected, result)

    def test_fahrenheit_to_celsius_90_32_2222(self):
        result = fahrenheit_to_celsius(90)
        expected = 32.22222222222222
        self.assertEqual(expected, result)

    def test_fahrenheit_to_celsius_negative_50_negative_45_5556(self):
        result = fahrenheit_to_celsius(-50)
        expected = -45.55555555555556
        self.assertEqual(expected, result)


class EnhanceTemperatureTestCase(unittest.TestCase):
    def test_enhance_temperature(self):
        result = enhance_temperature(
            {
                "id": "GLOBALLY_UNIQUE_IDENTIFIER",
                "type": "Sensor",
                "content": {
                    "temperature_f": 90,
                    "time_of_measurement": "2019-06-24T15:00:00",
                },
            }
        )
        expected = {
            "id": "GLOBALLY_UNIQUE_IDENTIFIER",
            "type": "Sensor",
            "content": {
                "temperature_f": 90,
                "temperature_c": 32.22222222222222,
                "time_of_measurement": "2019-06-24T15:00:00",
            },
        }
        self.assertEqual(expected, result)

    def test_enhance_temperature_missing_data(self):
        with self.assertRaises(ValueError):
            enhance_temperature(
                {
                    "id": "GLOBALLY_UNIQUE_IDENTIFIER",
                    "type": "Sensor",
                    "content": {"time_of_measurement": "2019-06-24T15:00:00"},
                }
            )
