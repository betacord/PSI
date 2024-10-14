import asyncio

from repositories.air_quality_repository import AirQualityRepository
from services.air_quality_service import AirQualityService
from utils import consts


async def main() -> None:
    repository = AirQualityRepository()
    service = AirQualityService(repository=repository)

    last_pm10_index = await service.get_air_quality_index(consts.SENSOR_ID)
    mean_pm10_value = await service.get_mean_params(consts.SENSOR_ID)

    print(f"Current AQI: {last_pm10_index}, average PM10 value: {mean_pm10_value}")


if __name__ == "__main__":
    asyncio.run(main())
