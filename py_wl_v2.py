import time
import hmac
import hashlib
import requests
import collections


class WeatherLink:

    API_URL_V2 = 'https://api.weatherlink.com/v2/'

    def __init__(self, api_key, api_secret):
        self.api_key = api_key
        self.api_secret = api_secret.encode('utf-8')
        self.timestamp = int(time.time())

    def signature(self, station_id=''):
        self.timestamp = int(time.time())

        params = {
            'api-key': self.api_key,
            't': self.timestamp
        }

        if station_id != '':
            params['station-id'] = station_id

        # sort keys in alpha order
        params = collections.OrderedDict(sorted(params.items()))

        payload = ''
        for key in params:
            payload = payload + key + str(params[key])

        payload = payload.encode('utf-8')

        return hmac.new(self.api_secret, payload, hashlib.sha256).hexdigest()

    def stations(self, station_ids=[]):
        # accepts a list of station ids in string format
        if station_ids:
            stations_str = ''
            stations_str.join(station_ids)
            req = requests.get(self.API_URL_V2 + 'stations/' + stations_str + '?api-key=' + self.api_key +
                               '&api-signature=' + self.signature() + '&t=' + str(self.timestamp))
        else:
            req = requests.get(self.API_URL_V2 + 'stations?api-key=' + self.api_key + '&api-signature=' +
                               self.signature() + '&t=' + str(self.timestamp))
        return req

    def nodes(self, node_ids=[]):
        # accepts a list of node ids in string format
        if node_ids:
            nodes_str = ''
            nodes_str.join(node_ids)
            req = requests.get(self.API_URL_V2 + 'nodes/' + nodes_str + '?api-key=' + self.api_key + '&api-signature=' +
                               self.signature() + '&t=' + str(self.timestamp))
        else:
            req = requests.get(self.API_URL_V2 + 'nodes?api-key=' + self.api_key + '&api-signature=' +
                               self.signature() + '&t=' + str(self.timestamp))
        return req

    def sensors(self, sensor_ids=[]):
        # accepts a list of sensor ids in string format
        if sensor_ids:
            sensors_str = ''
            sensors_str.join(sensor_ids)
            req = requests.get(self.API_URL_V2 + 'sensors/' + sensors_str + '?api-key=' + self.api_key +
                               '&api-signature=' + self.signature() + '&t=' + str(self.timestamp))
        else:
            req = requests.get(self.API_URL_V2 + 'sensors?api-key=' + self.api_key + '&api-signature=' +
                               self.signature() + '&t=' + str(self.timestamp))
        return req

    def sensor_activity(self, sensor_ids=[]):
        # accepts a list of sensor ids in string format
        if sensor_ids:
            sensors_str = ''
            sensors_str.join(sensor_ids)
            req = requests.get(self.API_URL_V2 + 'sensor-activity/' + sensors_str + '?api-key=' + self.api_key +
                               '&api-signature=' + self.signature() + '&t=' + str(self.timestamp))
        else:
            req = requests.get(self.API_URL_V2 + 'sensor-activity?api-key=' + self.api_key + '&api-signature=' +
                               self.signature() + '&t=' + str(self.timestamp))
        return req

    def sensor_catalog(self):
        return requests.get(self.API_URL_V2 + 'sensor-catalog?api-key=' + self.api_key + '&api-signature=' +
                            self.signature() + '&t=' + str(self.timestamp))

    def current(self, station_id):
        return requests.get(self.API_URL_V2 + 'current/' + str(station_id) + '?api-key=' + self.api_key +
                            '&api-signature=' + self.signature(station_id) + '&t=' + str(self.timestamp))

    def historic(self, station_id, start_timestamp, end_timestamp):
        return requests.get(self.API_URL_V2 + 'current/' + str(station_id) + '?api-key=' + self.api_key +
                            '&api-signature=' + self.signature(station_id) + '&t=' + str(self.timestamp) +
                            '&start-timestamp=' + str(start_timestamp) + '&end-timestamp=' + str(end_timestamp))


# Create a WeatherLink object using API keys
wl = WeatherLink('your_api_key', 'your_api_secret')

# Get Stations
wl.stations()

# Get Specific Stations (Accepts a list of Station Ids in string format)
wl.stations(['12345', '45678'])

# Get Nodes
wl.nodes()

# Get Specific Nodes (Accepts a list of Node Ids in string format)
wl.nodes(['12345', '45678'])

# Get Sensors
wl.sensors()

# Get Specific Sensors (Accepts a list of Sensor Ids in string format)
wl.sensors(['12345', '45678'])

# Get Sensor activity
wl.sensor_activity()

# Get Specific Sensor activity (Accepts a list of Sensor Ids in string format)
wl.sensor_activity(['12345', '45678'])

# Get Sensor catalog
wl.sensor_catalog()

# Get current conditions for a station
wl.current('12345')

# Get historic conditions for a station
wl.historic('12345', '1573237000', '1573238061')
