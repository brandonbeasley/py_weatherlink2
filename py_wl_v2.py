########################################################################################################################
# WeatherLink API v2 Python Library
# Author: Brandon Beasley
# License: GNU General Public License version 3
# Date: 11/14/2019
# Interpreter: Python 3.8
########################################################################################################################

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

    def signature(self, params={}):
        self.timestamp = int(time.time())

        params['api-key'] = self.api_key
        params['t'] = self.timestamp

        params = collections.OrderedDict(sorted(params.items()))

        payload = ''
        for key in params:
            payload = payload + key + str(params[key])

        return hmac.new(self.api_secret, payload.encode('utf-8'), hashlib.sha256).hexdigest()

    def stations(self, station_ids=[]):
        stations_str = ','.join(station_ids)
        query_params = {
            'api-key': self.api_key,
            'api-signature': self.signature({'station-ids': stations_str} if station_ids else {}),
            't': str(self.timestamp)
        }
        return requests.get(self.API_URL_V2 + 'stations/' + stations_str, params=query_params)

    def nodes(self, node_ids=[]):
        nodes_str = ','.join(node_ids)
        query_params = {
            'api-key': self.api_key,
            'api-signature': self.signature({'node-ids': nodes_str} if node_ids else {}),
            't': str(self.timestamp)
        }
        return requests.get(self.API_URL_V2 + 'nodes/' + nodes_str, params=query_params)

    def sensors(self, sensor_ids=[]):
        sensors_str = ','.join(sensor_ids)
        query_params = {
            'api-key': self.api_key,
            'api-signature': self.signature({'sensor-ids': sensors_str} if sensor_ids else {}),
            't': str(self.timestamp)
        }
        return requests.get(self.API_URL_V2 + 'sensors/' + sensors_str, params=query_params)

    def sensor_activity(self, sensor_ids=[]):

        sensors_str = ','.join(sensor_ids)
        query_params = {
            'api-key': self.api_key,
            'api-signature': self.signature({'sensor-ids': sensors_str} if sensor_ids else {}),
            't': str(self.timestamp)
        }
        return requests.get(self.API_URL_V2 + 'sensor-activity/' + sensors_str, params=query_params)

    def sensor_catalog(self):
        return requests.get(self.API_URL_V2 + 'sensor-catalog?api-key=' + self.api_key + '&api-signature=' +
                            self.signature() + '&t=' + str(self.timestamp))

    def current(self, station_id):
        query_params = {
            'api-key': self.api_key,
            'api-signature': self.signature({'station-id': station_id}),
            't': str(self.timestamp)
        }
        return requests.get(self.API_URL_V2 + 'current/' + str(station_id), params=query_params)

    def historic(self, station_id, start_timestamp, end_timestamp):
        query_params = {
            'api-key': self.api_key,
            'api-signature': self.signature({'station-id': station_id, 'start-timestamp': start_timestamp, 'end-timestamp': end_timestamp}),
            't': str(self.timestamp),
            'start-timestamp': str(start_timestamp),
            'end-timestamp': str(end_timestamp)
        }
        return requests.get(self.API_URL_V2 + 'historic/' + str(station_id), params=query_params)




