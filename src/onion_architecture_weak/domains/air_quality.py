from dataclasses import dataclass
from datetime import datetime


@dataclass
class AirQualityRecord:
    event_time: datetime
    pm10_value: float
