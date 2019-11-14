import unittest
import configparser
from py_wl_v2 import WeatherLink

config = configparser.ConfigParser()
config.read('setup.ini')

wl = WeatherLink(config['API']['ApiKey'], config['API']['ApiSecret'])


class TestApiMethods(unittest.TestCase):

    def test_stations(self):
        test = wl.stations()
        self.assertEqual(test.status_code, 200)

    def test_stations_list(self):
        test = wl.stations([config['API']['StationId'], ])
        self.assertEqual(test.status_code, 200)

    def test_nodes(self):
        test = wl.nodes()
        self.assertEqual(test.status_code, 200)

    def test_nodes_list(self):
        test = wl.nodes(['1234', ])
        self.assertEqual(test.status_code, 403)

    def test_sensors(self):
        test = wl.sensors()
        self.assertEqual(test.status_code, 200)

    def test_sensors_list(self):
        test = wl.sensors([config['API']['SensorId1'], config['API']['SensorId2']])
        self.assertEqual(test.status_code, 200)

    def test_sensor_activity(self):
        test = wl.sensor_activity()
        self.assertEqual(test.status_code, 200)

    def test_sensors_activity_list(self):
        test = wl.sensor_activity([config['API']['SensorId1'], config['API']['SensorId2']])
        self.assertEqual(test.status_code, 200)

    @unittest.skip("Sensor Catalog Test must be explicitly enabled due to dataset size")
    def test_sensor_catalog(self):
        test = wl.sensor_catalog()
        self.assertEqual(test.status_code, 200)

    def test_current(self):
        test = wl.current(config['API']['StationId'])
        self.assertEqual(test.status_code, 200)

    def test_historic(self):
        test = wl.historic(config['API']['StationId'], '1573741114', '1573742114')
        self.assertEqual(test.status_code, 200)


if __name__ == '__main__':
    unittest.main()

