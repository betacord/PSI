from abc import ABC
from typing import Iterable

from domains.air_quality import AirQualityRecord


class IAirQualityRepository(ABC):
    async def get_last_air_quality_params(self, sensor_id: int) -> AirQualityRecord | None:
        pass

    async def get_all_air_quality_params(self, sensor_id: int) -> Iterable[AirQualityRecord] | None:
        pass
