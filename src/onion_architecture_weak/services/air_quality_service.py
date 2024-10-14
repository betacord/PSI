from repositories.air_quality_repository import AirQualityRepository
from services.iair_quality_service import IAirQualityService
from utils.utils import PM10IndexEnum


class AirQualityService(IAirQualityService):
    repository: AirQualityRepository

    def __init__(self, repository: AirQualityRepository) -> None:
        self.repository = repository

    async def get_air_quality_index(self, sensor_id: int) -> str:
        pm10_current_value = await self.repository.get_last_air_quality_params(sensor_id=sensor_id)
        pm10_index_value = PM10IndexEnum.from_pm10_value(pm10_current_value.pm10_value)

        return pm10_index_value
    
    async def get_mean_params(self, sensor_id: int) -> float:
        all_quality_params = await self.repository.get_all_air_quality_params(sensor_id=sensor_id)
        mean_air_quality_params = sum([r.pm10_value for r in all_quality_params if r.pm10_value is not None]) / len(all_quality_params)

        return mean_air_quality_params
