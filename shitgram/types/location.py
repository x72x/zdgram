from typing import Union

class Location:
    longitude: float
    latitude: float
    horizontal_accuracy: Union[float, int]
    live_period: int
    heading: int
    proximity_alert_radius: int
