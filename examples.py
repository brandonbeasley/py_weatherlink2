from py_wl_v2 import WeatherLink
from pprint import pprint

# Responses are returned as Request objects, ( .body .text .json() )


# Create a WeatherLink object using API keys
wl = WeatherLink('api-key', 'api-secret')

# Get Stations
pprint(wl.stations().json())


# Get Specific Stations (Accepts a list of Station Ids in string format)
pprint(wl.stations(['12345', ]).json())


# Get Nodes
pprint(wl.nodes().json())

# Get Specific Nodes (Accepts a list of Node Ids in string format)
pprint(wl.nodes(['1234', ]).json())


# Get Sensors
pprint(wl.sensors().json())


# Get Specific Sensors (Accepts a list of Sensor Ids in string format)
pprint(wl.sensors(['123456', '123457']).json())


# Get Sensor activity
pprint(wl.sensor_activity().json())


# Get Specific Sensor activity (Accepts a list of Sensor Ids in string format)
pprint(wl.sensor_activity(['123456', '123457']).json())


# Get Sensor catalog - USE ONLY AS NEEDED!!! (Very large dataset)
# pprint(wl.sensor_catalog().json())


# Get current conditions for a station
pprint(wl.current('12345').json())


# Get historic conditions for a station
pprint(wl.historic('12345', '1573741114', '1573742114').json())
